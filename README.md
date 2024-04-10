# Face-Recognition-using-DeepFace
DeepFace is a Python library for deep learning-based face analysis, recognition, and manipulation. It provides functionalities for face detection, facial attribute analysis, face recognition, facial similarity calculation, and more.
This project is made in Google Colab Environment in which DeepFace is being used for face verification. Specifically, it is used to verify whether a detected face in each frame of the video matches a reference face (ref.jpg). Here's a breakdown of how it works:

Face Detection: The script captures frames from the video (or live camera feed if you were running it locally) and detects faces using OpenCV's cv2.VideoCapture and related functions.

Face Verification: For each detected face, it passes the frame containing the face and the reference face (ref.jpg) to DeepFace's verify function. This function compares the detected face with the reference face and determines whether they are the same person.

Result Visualization: Based on the result of the face verification, the script displays "MATCH!" or "Not MATCH!" on each frame of the video to indicate whether the detected face matches the reference face.

This functionality relies on DeepFace's pre-trained deep learning models for face recognition and similarity calculation. It's worth noting that DeepFace internally uses pre-trained models such as VGG-Face, OpenFace, and FaceNet to perform its tasks.

In Google Colab, you can use DeepFace as long as it's installed and compatible with the Python environment provided by Colab. You may need to install DeepFace using pip if it's not already installed:

!pip install deepface

Once installed, you can import and use DeepFace in your Colab notebook as demonstrated in your provided script. Just make sure you've uploaded the necessary reference image and video to your Google Drive and modify the paths accordingly in the script.
