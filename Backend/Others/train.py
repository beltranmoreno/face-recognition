import cv2
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_dataset(dataset_path):
    face_images = []
    face_labels = []

    for person_name in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_dir):
            continue

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
            face_images.append(gray)
            face_labels.append(person_name)

    return face_images, face_labels

def detect_face(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Load the face detection cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the dataset
dataset_path = "/Users/beltranmorenodealboran/Documents/DevProjects/FaceRecognition/resized_dataset"
face_images, face_labels = load_dataset(dataset_path)

# Encode the labels
label_encoder = LabelEncoder()
face_labels = label_encoder.fit_transform(face_labels)

# Train the face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(face_images, face_labels)

# Save the trained model
face_recognizer.save("face_recognizer.xml")
