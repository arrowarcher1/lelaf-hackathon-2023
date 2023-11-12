# lelaf-hackathon-2023
# ASL for the Community

## Inspiration
Inspired to bridge the communication gap between deaf individuals and those with hearing, our team developed a solution to make American Sign Language (ASL) learning accessible and interactive. Utilizing image recognition and instant verbal feedback, our project aims to facilitate ASL learning in the Lehigh Valley community.

## What It Does
The project utilizes an image recognition model, trained in Amazon SageMaker, to identify ASL signs from the user's webcam feed. Once a sign is recognized, it translates to its corresponding English letter. This letter is then visually displayed and audibly announced using Amazon Polly, providing real-time feedback for an interactive learning experience.

## How We Built It
Our development process primarily took place on Amazon SageMaker, focusing on training the image recognition model. Following the model development, we integrated a camera feed to use the model for live letter detection. The project also features Amazon Polly for audio output and initially used Turtle Graphics for visual output. The final stage involved combining these components into a cohesive application.

## Challenges We Ran Into
The primary challenge was the time constraint for training our model, which led us to focus on recognizing a subset of the ASL alphabet (letters A, B, and C).

## Accomplishments
We take pride in the successful completion of our project, particularly as it marks our foray into such a multifaceted development process.

## What We Learned
The project was a comprehensive learning journey, especially in aspects of data model training and front-end development – areas previously unfamiliar to us.

## What's Next
The project is in its early stages with ample room for growth. Our immediate goals include expanding the model's recognition capabilities to cover the entire ASL alphabet and enhancing its reliability with additional data. Future enhancements aim to develop a more user-friendly front-end interface.

---

## Technical Overview

### Program Workflow

1. **Webcam Feed Processing**: Capturing live video feed from the user's webcam.
2. **ASL Sign Recognition**: Using Amazon SageMaker's pre-trained model to identify ASL signs from the video frames.
3. **Letter Output**: Translating recognized signs into corresponding English letters.
4. **Display and Audio Feedback**: Utilizing OpenCV for on-screen letter display and Amazon Polly for audio feedback.
5. **Interactive Learning**: An engaging setup for users to learn and practice ASL.

### Technologies Used

- Amazon SageMaker
- Amazon Polly
- OpenCV
- Python (with boto3, pygame)

### Setup and Usage

- Install required libraries: `cv2`, `boto3`, `pygame`.
- Execute the script to start the ASL recognition tool.
- Perform ASL signs in front of the webcam to see and hear the corresponding letter.

### Future Enhancements

- Extend to the full ASL alphabet.
- Improve model accuracy with more data.
- Develop a user-friendly interface.
