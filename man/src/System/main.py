import speech_recognition as sr
import pyttsx3


class Recognizer:

    def __init__(self):
        self.r=sr.Recognizer()
        self.m=sr.Microphone()
        self.voice=Voice()
    
    def recognize_command(self):

        with self.m as source:
            print("Слухаю...")
            audio=self.r.listen(source)

        try:
            command = self.r.recognize_google(audio, language="uk-UK")
            self.command=str(command.lower())
            print("Ви сказали: ",self.command)

        except sr.UnknownValueError:
            self.voice.say_message('Error!')

        except sr.RequestError:
            self.voice.say_message('Error!')


class Voice:

    def __init__(self):
        self.engine=pyttsx3.init()


    def say_message(self,message):

        try:
            self.engine.say(message)
            self.engine.runAndWait()
        
        except Exception as e:
            return None