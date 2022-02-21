import PySimpleGUI as sg
import time
import sys

sys.path.append('.')

try:
    from src.System.main import Voice

except Exception:
    pass


class Design:

    sg.theme('DarkBlue14')

    def __init__(self):
        self.voice=Voice()

    def text_message(self):

        layout=[
            [sg.Text('Введіть email з якого відправити',font=("Arial, 11")),sg.Input(key='User1')],
            [sg.Text('Введіть пароль до email',font=("Arial, 11")),sg.Input(key='password_user1',password_char='*')],
            [sg.Text('Введіть email на який відправити',font=("Arial, 11")),sg.Input(key='User2')],
            [sg.Text('Введіть тему повідомлення',font=("Arial, 11")),sg.Input(key='SubjectLetter')],
            [sg.Text('Введіть ваше повідомлення',font=("Arial, 11")),sg.Input(key='message')],
            [sg.Button('Відправити',key='SendMessage',size=(22),font=("Arial, 11")),sg.Button('Скасувати',key='exit',size=(22),font=("Arial, 11"))]
        ]

        window=sg.Window('Email',layout,size=(410,180))
            
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='exit':
                    window.close()

                if event=='SendMessage':
                    self.email_from=values.get('User1')
                    self.email_to=values.get('User2')
                    self.password=values.get('password_user1')
                    self.subject=values.get('SubjectLetter')
                    self.message_1=values.get('message')
                    time.sleep(0.2)
                    window.close()
        
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')


    def file_message(self):
        layout=[
            [sg.Text('Введіть email з якого відправити',font=("Arial, 11")),sg.Input(key='User1')],
            [sg.Text('Введіть пароль до email',font=("Arial, 11")),sg.Input(key='password_user1',password_char='*')],
            [sg.Text('Введіть email на який відправити',font=("Arial, 11")),sg.Input(key='User2')],
            [sg.Text('Введіть тему для файлу',font=("Arial, 11")),sg.Input(key='SubjectLetter')],
            [sg.Text("Виберіть шлях файлу",font=("Arial, 11")),sg.Input(key='path_to_file'),sg.FileBrowse('...')],
            [sg.Button('Відправити',key='SendMessage',size=(25),font=("Arial, 11")),sg.Button('Скасувати',key='exit',size=(25),font=("Arial, 11"))]
        ]

        window=sg.Window('Email',layout,size=(570,190))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='exit':
                    window.close()

                if event=='SendMessage':
                    self.email_from=values.get('User1')
                    self.email_to=values.get('User2')
                    self.password=values.get('password_user1')
                    self.subject=values.get('SubjectLetter')
                    self.path_to_file=values.get('path_to_file')
                    time.sleep(0.2)
                    window.close()
        
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')