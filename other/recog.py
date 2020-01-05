
# coding: utf-8

# In[ ]:


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


    

# Close all windows


# In[ ]:

vid_cam = cv2.VideoCapture(0)
def vid():
    # Initialize and start the video frame capture
    
    ADM=0
    UNK=0
    TOT=0
    # Loop
    while TOT<=3:
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
                TOT+=1
                ADM+=1
                
            #If not exist, then it is Unknown

            else:           
                Id1 = "Unknown"
                TOT+=1

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
    
    return ADM
    


# In[ ]:


def signal(a):
    f=open("sema.txt","w")
    if a==1:
        f.write("a")
    else:
        f.write("u")
    f.close()


# In[ ]:


def wait():
    p='c'
    #c=3
    while(p!='p'):
        print("waiting")
        f=open("sema.txt","r")
        p=f.read(1)
        #print("abc")
        #print(p)
        f.close()
        #c-=1


# In[ ]:


while True:    
    wait()
    print("video started")
    x=vid()
    print("video finished")
    a=1
    if x< 2:
        a=0
    signal(a)


# In[ ]:

vid_cam.release()
cv2.destroyAllWindows()

