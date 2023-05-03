import face_recognition
import os
import cv2

# Path to the directory containing the face images
dataset_path = "datasets_live"

# List all the subdirectories in the dataset directory
person_names = os.listdir(dataset_path)

# Initialize arrays to store the face encodings and labels
known_face_encodings = []
known_face_labels = []

# Loop through each person's directory
for person_name in person_names:
    # Create the full path to the person's directory
    person_dir = os.path.join(dataset_path, person_name)
    # Loop through all the image files in the person's directory
    for filename in os.listdir(person_dir):
        # Create the full path to the image file
        image_path = os.path.join(person_dir, filename)
        # Load the image file into a numpy array
        image = face_recognition.load_image_file(image_path)
        # Find the face encoding for the image
        face_encoding = face_recognition.face_encodings(image)[0]
        # Add the face encoding and label to the arrays
        known_face_encodings.append(face_encoding)
        known_face_labels.append(person_name)

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)

# Loop forever
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in the current frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Try to match the face with a known person
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # If a match was found, use the first match and get the label
        if True in matches:
            first_match_index = matches.index(True)
            label = known_face_labels[first_match_index]
        # If no match was found, label the face as unknown
        else:
            label = "Unknown"

        # Draw a box around the face and label it with the person's name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, label, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # Resize the frame
    max_width = 500
    height, width, _ = frame.shape
    aspect_ratio = width / height
    resized_width = min(max_width, width)
    resized_height = int(resized_width / aspect_ratio)
    resized_frame = cv2.resize(frame, (resized_width, resized_height))
    # Display the resulting image
    cv2.imshow('Video', resized_frame)

    # If the 'q' key is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
