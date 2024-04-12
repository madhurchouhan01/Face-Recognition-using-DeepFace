import cv2
from deepface import DeepFace

def process_image(filepath):
    ref_img = cv2.imread(filepath)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret , frame = cap.read()

    try:
        if DeepFace.verify(frame, ref_img.copy())['verified']:
            return "MATCH!"
        else:
            return "Not MATCH!"
    except ValueError:
        return "Error processing image"
