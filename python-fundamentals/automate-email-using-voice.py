import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3 
listener=sr.Recognizer()
tts=pyttsx3.Engine()
def talking_tom(text):
   tts.say(text)
   tts.runAndWait()

def mic():
   with sr.Microphone() as source:
     print("I am all ears........")
     voice=listener.listen(source)
     data=listener.recognize_google(voice)
     print(data)
     return data.lower()
dict={"jojo":"f2022332020@umt.edu.pk"}

def send_mail(reciever,subject, body,):
   server=smtplib.SMTP("smtp.gmail.com",587)
   server.starttls()
   server.login("tehreemghulamnabi03@gmail.com","tjfh ywlr xvnr ryqd")
   email=EmailMessage()
   email['From']="tehreemghulamnabi03@gmail.com"
   email['To']=reciever
   email["Subject"]=subject
   email.set_content(body)
   server.send_message(email)
def main_code():
   talking_tom("To whom do you want to send the email")
   name= mic()
   reciever= dict[name]
   talking_tom("Tell the subject of the email")
   subject=mic()
   talking_tom("Tell the body of the email")
   body=mic()
   send_mail(reciever,subject, body)
   print("Your email is being sent")
main_code()
   
