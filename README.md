# lelaf-hackathon-2023
README
ASL for the Community
Inspiration
Our team was inspired to create a solution that facilitates communication between deaf individuals and those with hearing. We aimed to make American Sign Language (ASL) learning accessible and straightforward for everyone in the Lehigh Valley. The combination of image recognition and instant verbal feedback in our project opens the door for easy ASL learning.

What It Does
The project leverages an image recognition model trained in Amazon SageMaker to identify ASL signs captured by the user's webcam. The identified sign is translated into its corresponding English letter, which is then visually displayed and audibly spoken using Amazon Polly. This real-time feedback mechanism provides an interactive learning experience.

How We Built It
The development of our program was primarily conducted on Amazon SageMaker. We worked collaboratively to train the image recognition model. Post-training, we developed a camera feed application that utilized the model to recognize and output letters. This was complemented by integrating Amazon Polly for voice output and initially using Turtle Graphics for letter visualization. The final step involved integrating these components into a cohesive application.

Challenges We Ran Into
A significant challenge was training our image recognition model within a limited time frame. To manage this, we focused on a subset of the ASL alphabet (letters A, B, and C), allowing us to train the model effectively with a substantial amount of data for each letter.

Accomplishments
We are proud of successfully completing the project, especially considering the scale and the novelty of such an endeavor for our team. Although the project scope was adjusted, the final product met our satisfaction.

What We Learned
The project was a substantial learning experience, particularly in training data models. We gained insights into the extensive data and time required for training an effective model. Additionally, we learned about front-end development, a new area for all team members.

What's Next
This project is in its early stages and has considerable potential for growth. Immediate improvements include expanding support to the entire ASL alphabet and enhancing detection reliability with more data. Future enhancements also involve developing a more user-friendly front-end interface.

Technical Overview
Program Workflow
Webcam Feed Processing: The program captures a continuous video feed from the user's webcam.

ASL Sign Recognition: Frames from the video feed are processed and analyzed using a pre-trained model in Amazon SageMaker, which identifies ASL signs.

Letter Output: The identified sign is converted to its corresponding English letter.

Display and Audio Feedback: The letter is displayed on the screen using OpenCV, and simultaneously, the letter is spoken out loud using Amazon Polly, providing immediate verbal feedback.

Interactive Learning: This setup offers an interactive learning experience for users to practice and understand ASL.

Technologies Used
Amazon SageMaker for training the image recognition model.
Amazon Polly for text-to-speech conversion.
OpenCV for video feed capture and display functionalities.
Python and associated libraries (boto3, pygame) for backend processing and audio playback.
Setup and Usage
Ensure all required libraries (cv2, boto3, pygame) are installed.
Run the script to start the ASL recognition and feedback tool.
Place your hand in front of the webcam and make ASL signs for A, B, or C to see the program in action.
Future Enhancements
Extend support to the entire ASL alphabet.
Improve recognition accuracy with more training data.
Develop a user-friendly front-end interface.