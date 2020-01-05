
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time



# In[ ]:


def signal():
    f=open("sema.txt","w")
    f.write("p")
    f.close()


# In[ ]:


def wait():
    p='c'
    #c=3
    while(p!='a' or p!='u'):
        #print("abc")
        f=open("sema.txt","r")
        p=f.read(1)
        #print("abc")
        #print(p)
        f.close()
        #c-=1
        if p=='a':
            return 'a'
        if p=='u':
            return 'u'
    return p  


# In[1]:


def case():
    signal()
    z=wait()
    
    print("a person found")
    if z=='a':
        print("ADMIN is Present")
        return 1
    else:
        print("Do you Know that person")
        x=input()
        if x=='Y' or x=='y':
            return 1
        else:
            return 0


# In[ ]:


def IR2():
    sensor = 18
    #buzzer = 18

    #print("enter")

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)
    #GPIO.setup(buzzer,GPIO.OUT)

    #GPIO.output(buzzer,False)
    print("IR2 Sensor open")
    #print("check2")

    try:
        #xmpz=GPIO.input(sensor)
        for i in range(0,50):
            #print("check3")
            if GPIO.input(sensor)==0:
                #GPIO.output(buzzer,True)
                print("Exit Object Detected")
                print(GPIO.input(sensor))
                return 1
                while GPIO.input(sensor)==0:
                      time.sleep(10)
            #else:
            #    GPIO.output(buzzer,False)
        return 0

    except KeyboardInterrupt:
        return 0
        GPIO.cleanup()
        
def IR1(z):
    sensor = 16
    buzzer = 22

    #print("enter")

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN)
    #GPIO.setup(buzzer,GPIO.OUT)

    #GPIO.output(buzzer,False)
    print("IR1 Sensor open")
    #print("check2")

    #buzzer = 22
    #GPIO.setwarnings(False)
    #if(z>0):
    #    GPIO.setup(buzzer,True)
    #else:
    #    GPIO.setup(buzzer,False)

    try:
        #xmpz=GPIO.input(sensor)
        for i in range(0,50):
            #print("check3")
            if GPIO.input(sensor)==0:
                #GPIO.output(buzzer,True)
                print("enter Object Detected")
                l=case()
                print(GPIO.input(sensor))
                return l
                while GPIO.input(sensor)==0:
                      time.sleep(0.2)
            #else:
            #    GPIO.output(buzzer,False)
        return 0

    except KeyboardInterrupt:
        return 0
        GPIO.cleanup()

#def LEDOUT(z):
    

test=10


while True:
    #print("check1")
    #LEDOUT(test)
    test+=IR1(test)
    test-=IR2()
    if test<0:
        test=0
    print(test)
