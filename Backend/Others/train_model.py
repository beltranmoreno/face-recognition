import cv2
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder


# Load pre-trained face detection model
face_detector = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")

# Load images and corresponding labels
def load_dataset(dataset_path):
    faces = []
    labels = []
    for label_name in os.listdir(dataset_path):
        label_path = os.path.join(dataset_path, label_name)
        for image_name in os.listdir(label_path):
            image_path = os.path.join(label_path, image_name)
            image = cv2.imread(image_path)
            face, confidence = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label_name)
    return faces, labels

# Detect faces in an image using the pre-trained model
def detect_face(image):
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_detector.setInput(blob)
    detections = face_detector.forward()
    if len(detections) > 0:
        i = np.argmax(detections[0, 0, :, 2])
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            face = image[startY:endY, startX:endX]
            return face, confidence
    return None, None

# Load dataset
dataset_path = "/Users/beltranmorenodealboran/Documents/DevProjects/FaceRecognition/resized_dataset"
faces, labels = load_dataset(dataset_path)

# Convert labels to integers
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

# Train face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, labels)

# Save model
model_path = "/Users/beltranmorenodealboran/Documents/DevProjects/FaceRecognition/model"
face_recognizer.write(model_path)
