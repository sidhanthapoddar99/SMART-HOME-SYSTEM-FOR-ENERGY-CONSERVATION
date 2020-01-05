# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
vid_cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    _, im =vid_cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.3,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x,y), (x+w,y+h), (255,0,0), 2)

        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])

        # Check the ID if exist 
        id1=""
        if(Id[1] >= 75):
            Id1 = "ADMIN"
        #If not exist, then it is Unknown
        
        else:           
            Id1 = "Unknown"
        
        print(Id1)


        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
