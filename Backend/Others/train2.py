import os
import cv2
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# Load the dataset and detect faces
def load_dataset():
    # Initialize lists to hold images and labels
    images = []
    labels = []
    # Loop through all the folders in the resized_dataset directory
    for folder in os.listdir('resized_dataset'):
        # Loop through all the images in the folder
        for filename in os.listdir(os.path.join('resized_dataset', folder)):
            # Read the image file
            img = cv2.imread(os.path.join('resized_dataset', folder, filename))
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the face in the image
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            # If a face is detected, append it to the images list and its label to the labels list
            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                face = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (200, 200))
                images.append(face_resized)
                labels.append(folder)

    # Encode the labels
    le = LabelEncoder()
    labels_enc = le.fit_transform(labels)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(images, labels_enc, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, le


# Train the model on the dataset
def train():
    # Load the dataset
    X_train, X_test, y_train, y_test, le = load_dataset()

    # Train the SVM model
    model = SVC(C=1.0, kernel='linear', probability=True)
    model.fit(X_train, y_train)

    # Save the model to a file
    with open('face_recognition_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # Save the label encoder to a file
    with open('labels.pickle', 'wb') as f:
        pickle.dump(le, f)

    print('Training completed successfully')


train()
