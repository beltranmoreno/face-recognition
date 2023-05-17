from flask import Flask, Response
import cv2
import face_recognition
import os
from flask_restful import Api, Resource
from flask_cors import CORS
import time


app = Flask(__name__)
cors = CORS(app)
api = Api(app)

@app.route('/')
def index():
    return "Hello, World!"

def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n'
                   b'Content-Length: ' + str(len(frame_bytes)).encode() + b'\r\n'
                   b'\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.01)  # Adjust the delay between frames as needed

    cap.release()

def generate_frames2():
    cap = cv2.VideoCapture(0)
    # Define the output video parameters
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('video_output.mp4', fourcc, 20.0, (640, 480))

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            out.write(frame)  # Write the frame to the video file
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    out.release()

def generate_feed():
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
                color_box = (0, 255, 0)
                color_label = (0, 255, 0)
            # If no match was found, label the face as unknown
            else:
                label = "Unknown"
                color_box = (0, 0, 255)
                color_label = (0, 0, 255)

            # Draw a box around the face and label it with the person's name
            cv2.rectangle(frame, (left, top), (right, bottom), color_box, 2)
            cv2.putText(frame, label, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color_label, 1)

        # Resize the frame
        max_width = 600
        height, width, _ = frame.shape
        aspect_ratio = width / height
        resized_width = min(max_width, width)
        resized_height = int(resized_width / aspect_ratio)
        resized_frame = cv2.resize(frame, (resized_width, resized_height))
        # Display the resulting image
        # cv2.imshow('Video', resized_frame)

    
        key = cv2.waitKey(10)
        if key == 27:
            break

        ret, buffer = cv2.imencode('.jpg', resized_frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/camera')
def camera_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video')
def video_feed():
    return Response(generate_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

class HelloWorld(Resource):
    def get(self):
        return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
api.add_resource(HelloWorld, '/videos')

class Test(Resource):
    def get(self):
        return {'hello': 'world'}

    
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(debug=True)
