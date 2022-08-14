#Imports
import speech_recognition as sr
import time
import keyboard
from PIL import Image
import cv2
import os

#Initialize proceeding and 
r = sr.Recognizer()
proceed = "Y"     


with sr.Microphone() as source:
    while (proceed != "N"):
        print("Speak:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            text = text.split()
            
            for i in text:
                if (os.path.exists(r"Images\{}.jpg".format(i))):
                    #get and show the image
                    im = Image.open(r"Images\{}.jpg".format(i))
                    im.show()

                    #wait and then close the image
                    time.sleep(5)
                    keyboard.send("ctrl+w")
                
                elif (os.path.exists(r"Clips\{}.mp4".format(i))):
                    #get and show the visual recording
                   cap= cv2.VideoCapture(r"Clips\{}.mp4".format(i))

                   fps= int(cap.get(cv2.CAP_PROP_FPS))

                   if cap.isOpened() == False:
                       print("Error File Not Found")

                   while cap.isOpened():
                       ret,frame= cap.read()

                       if ret == True:

                           time.sleep(1/fps)

                           cv2.imshow('frame', frame)

                           if cv2.waitKey(1) & 0xFF == ord('q'):
                               break

                       else:
                           break


                   cap.release()
                   cv2.destroyAllWindows()
                else:
                    x = list(i)
                    for j in x:
                        cap= cv2.VideoCapture(r"LettersNumbers\{}.mp4".format(j))

                        fps= int(cap.get(cv2.CAP_PROP_FPS))

                        if cap.isOpened() == False:
                            print("Error File Not Found")

                        while cap.isOpened():
                            ret,frame= cap.read()

                            if ret == True:

                                time.sleep(1/fps)

                                cv2.imshow('frame', frame)

                                if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break

                            else:
                                break


                        cap.release()
                        cv2.destroyAllWindows()     
        except:
            print("audio input unrecognizable")
        
        proceed = input("would you like to continue Y/N?")
        proceed = proceed.upper()

      







