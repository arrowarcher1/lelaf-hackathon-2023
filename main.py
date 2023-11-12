import cv2
import boto3
import json
import collections
import time
import pygame

# Initialize Polly and SageMaker clients
sagemaker_runtime = boto3.client('sagemaker-runtime', region_name='us-east-1')
polly_client = boto3.client('polly', region_name='us-east-1')

# Initialize pygame for audio
pygame.mixer.init()

# Define class names and other variables
class_names = ['A', 'B', 'C', 'None']
predictions = collections.deque(maxlen=100)  # Adjust based on your webcam's frame rate
start_time = time.time()
should_speak = True  # Flag to control speech

# Define the preprocess_frame function
def preprocess_frame(frame):
    # Add preprocessing steps here
    # Example: resize
    processed_frame = cv2.resize(frame, (224, 224))
    return processed_frame

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Preprocess the frame
    processed_frame = preprocess_frame(frame)

    # Convert the frame to the required format (e.g., byte array)
    _, buffer = cv2.imencode('.jpg', processed_frame)
    byte_frame = buffer.tobytes()

    # Send the frame to SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName='jumpstart-ftc-tf-ic-swin-base-patch4-window7-224',
        ContentType='application/x-image',
        Body=byte_frame
    )
    
    # Parse the response
    result = json.loads(response['Body'].read().decode())

    # Extract probabilities from the response
    probabilities = result.get('probabilities', [])

    # Find the index of the max probability
    max_index = probabilities.index(max(probabilities))

    # Map the index to the class name
    predicted_class = class_names[max_index]

    # Store the prediction
    predictions.append(predicted_class)

    if time.time() - start_time >= 5:
        if predictions and should_speak:
            # Find the most common prediction
            most_common_prediction = collections.Counter(predictions).most_common(1)[0][0]
            print(f"Most common prediction in the last 5 seconds: {most_common_prediction}")

            # Call Amazon Polly to synthesize speech
            response = polly_client.synthesize_speech(
                Text=most_common_prediction,
                OutputFormat='mp3',
                VoiceId='Joanna'
            )

            # Save the audio stream to an MP3 file
            if "AudioStream" in response:
                with open('speech.mp3', 'wb') as file:
                    file.write(response['AudioStream'].read())

                # Play the audio file
                pygame.mixer.music.load('speech.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

            # Reset the flags and predictions
            should_speak = False
            predictions.clear()
            start_time = time.time()

    elif time.time() - start_time < 5 and not should_speak:
        should_speak = True

    # Display the frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV window
cap.release()
cv2.destroyAllWindows()