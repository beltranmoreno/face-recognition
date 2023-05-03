import cv2, sys, numpy, os
from deepface import DeepFace
datasets = 'datasets_live'
# datasets = 'resized_dataset'

  
print('Recognizing...')
  
# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (300, 300)
  
# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
  
# Part 2: Use fisherRecognizer on camera stream
webcam = cv2.VideoCapture(0)
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    result = DeepFace.verify(gray, '/Users/beltranmorenodealboran/Documents/DevProjects/FaceRecognition/datasets_live/Beltran/5.png')
    print(result)
    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        # Try to recognize the face
        prediction = model.predict(face_resize)
        # cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
  
        if prediction[1]<100:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(im, '% s - %.0f' % (names[prediction[0]], prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
        else:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(im, 'Unknown', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
  
    cv2.imshow('FaceRecognize', im)
      
    key = cv2.waitKey(10)
    if key == 27:
        break