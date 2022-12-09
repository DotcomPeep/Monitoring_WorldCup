# testing the library
import pyttsx3

engine = pyttsx3.init()

engine.say("Salve")
engine.say('vamos ver se isso realmente funciona')

engine.runAndWait()