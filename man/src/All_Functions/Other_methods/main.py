import os
import sys
import datetime
import webbrowser
import time
from pynput.keyboard import Key,Controller
sys.path.append('.')
from src.System.main import Voice


class Operator:
    
    def __init__(self):
        self.path=r'C:\Program Files\Google\Chrome\Application\chrome_proxy.exe'
        # self.path_toPrograms=r'C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'
        self.voice=Voice()
        self.keyboard=Controller()


    def turn_off_computer(self):

        try:
            os.system('shutdown /s')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def restart_computer(self):

        try:
            os.system('shutdown -r -f -t 5')
        
        except Exception:
            self.voice.say_message('Error!')

    
    def open_cmd(self):

        try:
            os.system('start')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def open_camera(self):

        try:
            os.system('start microsoft.windows.camera:')

        except Exception:
            self.voice.say_message('Error!')
    

    def take_photo_with_camera(self):

        try:
            os.system('start microsoft.windows.camera:')
            time.sleep(3.5)
            self.keyboard.press(Key.enter)
        
        except Exception:
            self.voice.say_message('Error!')
    

    # def made_screen_of_display(self):
    #     pg.screenshot()


    def open_browser(self):

        try:
            webbrowser.open('https://google.com')
        
        except webbrowser.Error:
            self.voice.say_message('Error!')

        except Exception:
            self.voice.say_message('Error!')

    
    def open_Chrome(self):

        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(self.path))
            webbrowser.get('Chrome').open_new('google.com')
        
        except webbrowser.Error:
            self.voice.say_message('Error!')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def open_youtube(self):

        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(self.path))
            webbrowser.get('Chrome').open_new('youtube.com')
        
        except webbrowser.Error:
            self.voice.say_message('Error!')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def open_socialnetworks_inBrowser(self,name):
        
        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(self.path))
            webbrowser.get('Chrome').open_new(f'{name}.com')
        
        except Exception:
            self.voice.say_message('Error!')
        
        except AttributeError:
            self.voice.say_message('You did not tell name of social networks!')

    
    # def open_program(self,program_name):

    #     try:
    #         os.system(f'cd {self.path_toPrograms}')
        
    #     except AttributeError:
    #         self.voice.say_message('You did not tell program name!')
        
    #     except Exception:
    #         self.voice.say_message('Error!')
    

    def close_program(self,program_name):

        try:
            os.system(f'taskkill /im {program_name}.exe')
        
        except Exception:
            self.voice.say_message('Error!')
        
        except AttributeError:
            self.voice.say_message('You did not tell program name!')


    def find_information_in_browser(self,information):

        try:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(self.path))
            webbrowser.get('Chrome').open_new('https://google.com/search?q='+information)
            time.sleep(0.5)
            self.voice.say_message('Searching...')

        except AttributeError:
            self.voice.say_message('You did not tell what information you want to search!')
        
        except Exception:
            self.voice.say_message('Error!')


    def get_full_time(self):

        try:
            time.sleep(1)
            self.voice.say_message(time.ctime())
        
        except Exception:
            self.voice.say_message('Error!')