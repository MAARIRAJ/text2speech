import pyttsx3
user =input("Enter the text :")
engine=pyttsx3.init()
engine.say(user)
engine.runAndWait()