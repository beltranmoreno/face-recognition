import cv2

# Load trained face recognition model
model_path = "face_recognizer.xml"
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(model_path)

# Load pre-trained face detection model
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # Load label encoder
# labels = {}
# with open('labels.pickle', 'rb') as f:
#     labels = {v:k for k,v in pickle.load(f).items()}

# Start video capture from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Recognize faces
    for (x, y, w, h) in faces:
        # Extract face region from the frame
        face = gray[y:y+h, x:x+w]

        # Recognize the face using the trained model
        label, confidence = face_recognizer.predict(face)

        # Draw a rectangle around the face and display the label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (x, y-10)
        font_scale = 1
        color = (0, 255, 0)  # green
        thickness = 2
        text = label
        if confidence[1]<500:
  
           cv2.putText(frame, '% s - %.0f' % (label[confidence[0]], confidence[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else:
          cv2.putText(frame, 'not recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
  
        cv2.putText(frame, str(text), org, font, font_scale, color, thickness)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
