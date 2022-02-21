import sys
sys.path.append('.')
from src.All_Functions.Send_Message.controller import Email
from src.System.main import Voice

class Sender:

    def __init__(self):
        self.email=Email()
        self.voice=Voice()
    

    def send_message(self):

        try:
            self.email.send_text_message()
            self.voice.say_message('The message was sent!')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def send_file(self):

        try:
            self.email.send_file()
            self.voice.say_message('The message was sent!')
        
        except Exception:
            self.voice.say_message('Error!')