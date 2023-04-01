import speech_recognition as sr
import pyttsx3

f1=open("t.txt","w+")
data=f1.read()
if data=="":
    f1.close()
    f1=open("t.txt","a+")

r=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
mic = sr.Microphone()
r.energy_threshold=1900

with mic as source:
    print("Give Input:",end=" ")
    r.adjust_for_ambient_noise(source)
    voice=r.listen(source)
    x=r.recognize_google(voice,language='en-US',key=None)
print(x)
for i in x:
    f1.write(i)
data=f1.read()
print(data)