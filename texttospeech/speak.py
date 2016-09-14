import pyttsx
import time

engine = pyttsx.init()

engine.setProperty('rate', 100)



voices = engine.getProperty('voices')

for voice in voices:
	print str(voice.id)   

engine.setProperty('voice', 'english-us')
engine.say('Danger')
engine.runAndWait()
