from tkinter import font


try:
    import PySimpleGUI as sg
    import time
    import sys
    sys.path.append('.')
    from src.System.main import Voice

except ImportError :
    print('Error!')

except SystemError:
    print('Error!')


class Design:
    sg.theme('DarkBlue14')

    def __init__(self):
        self.voice=Voice()

    def create_DataBase(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Button('Створити',key='-button-',size=(14),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(14),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(300,75))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()

                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def create_Table(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Button('Створити',key='-button-',size=(16),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(17),font=("Arial, 11"))]
        ]
                                                                                                                                                                                                  
        window=sg.Window('DataBase',layout,size=(350,100))
        
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')


    def create_Column_1(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість стовпців, яку створити',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('ОК',key='-button-',size=(19),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(19),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(400,120))
        
        while True:
            
            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                    break
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
                
            except ValueError:
                self.voice.say_message('Enter value!')
                
            except KeyError:
                self.voice.say_message('Error!')
            
            except Exception:
                self.voice.say_message('Error!')


    def create_Column_2(self):

        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='name_of_column')],
            [sg.Text('Виберіть тип стовпця',font=("Arial, 11")),sg.Combo(['TEXT','REAL','INTEGER','NULL','BLOB','NUMERIC'], key='type_of_column')],
            [sg.Button('Створити',key='-button-',size=(15),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(15),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(300,95))

        while True:

            try:
                event,values_1=window.read()
                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                        
                if event=='-button-':
                    self.name_of_Column=values_1.get('name_of_column')
                    self.type_of_Column=values_1.get('type_of_column')
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')

    
    def delete_Table(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Button('Видалити',key='-button-',size=(15),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(15),font=("Arial, 11"))]
        ]
        
        window=sg.Window('DataBase',layout,size=(300,100))
        
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def delete_Column(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Button('Видалити',key='-button-',size=(15),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(15),font=("Arial, 11"))]
        ]
        
        window=sg.Window('DataBase',layout,size=(300,125))
        
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.name_of_Column=values.get('Column_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_name_of_Table(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть нову назву таблиці',font=("Arial, 11")),sg.Input(key='new_table_name')],
            [sg.Button('Змінити',key='-button-',size=(15),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(15),font=("Arial, 11"))]
        ]
        
        window=sg.Window('DataBase',layout,size=(300,125))
        
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.new_name_of_Table=values.get('new_table_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_name_of_Column_1(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість стовпців,яку модифікувати',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('ОК',key='-button-',size=(24),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(24),font=("Arial, 11"))]
        ]
        
        window=sg.Window('DataBase',layout,size=(500,125))
        
        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_name_of_Column_2(self):

        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Text('Введіть нову назву стовпця',font=("Arial, 11")),sg.Input(key='new_column_name')],
            [sg.Button('Змінити',size=(20),font=("Arial, 11"),key='-button-'),sg.Button('Скасувати',size=(20),font=("Arial, 11"),key='Cancel')]
        ]

        window=sg.Window('DataBase',layout,size=(400,100))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_Column=values.get('Column_name')
                    self.new_name_of_Column=values.get('new_column_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')

    
    def add_data_toColumn_1(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість значень, яку додати',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('ОК',key='-button-',size=(20),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(20),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(400,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')


    def add_data_toColumn_2(self):
        
        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Text('Введіть значення яке потрібно додати',font=("Arial, 11")),sg.Input(key='Value_name')],
            [sg.Text('Введіть id для значення',font=("Arial, 11")),sg.Input(key='-id-')],
            [sg.Button('Додати',size=(18),font=("Arial, 11"),key='-button-'),sg.Button('Скасувати',size=(18),font=("Arial, 11"),key='Cancel')]
        ]

        window=sg.Window('DataBase',layout,size=(350,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_Column=values.get('Column_name')
                    self.data=values.get('Value_name')
                    self.id=int(values.get('-id-'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_data_inColumn_1(self):
        
        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість значень, яку модифікувати',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('ОК',key='-button-',size=(22),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(22),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(450,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_data_inColumn_2(self):
        
        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Text('Введіть id для вашого значення',font=("Arial, 11")),sg.Input(key='-id-')],
            [sg.Text('Введіть нове значення',font=("Arial, 11")),sg.Input(key='Value_name')],
            [sg.Button('Змінити',key='-button-',size=(18),font=("Arial, 11")),sg.Button('Скасувати',size=(18),font=("Arial, 11"),key='Cancel')]
        ]

        window=sg.Window('DataBase',layout,size=(330,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_Column=values.get('Column_name')
                    self.data=values.get('Value_name')
                    self.id=int(values.get('-id-'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')

    
    def change_type_of_Column_1(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість стовпців,яку модифікувати',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('OK',key='-button-',size=(22),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(22),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(450,125))

        while True:

            try:
                event,values=window.read()
                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                        
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def change_type_of_Column_2(self):

        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Text('Виберіть тип стовпця',font=("Arial, 11")),sg.Combo(['TEXT','REAL','INTEGER','NULL','BLOB','NUMERIC'], key='type_of_column')],
            [sg.Button('Змінити',size=(18),font=("Arial, 11"),key='-button-'),sg.Button('Скасувати',size=(18),font=("Arial, 11"),key='Cancel')]
        ]

        window=sg.Window('DataBase',layout,size=(330,100))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_Column=values.get('Column_name')
                    self.type_of_Column=values.get('type_of_column')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def delete_Data_1(self):

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість значень, яку видалити',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('ОК',key='-button-',size=(18),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(18),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(350,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def delete_Data_2(self):

        layout=[
            [sg.Text('Введіть назву стовпця',font=("Arial, 11")),sg.Input(key='Column_name')],
            [sg.Text('Введіть значення, яке видалити',font=("Arial, 11")),sg.Input(key='Value_name')],
            [sg.Button('Видалити',size=(18),font=("Arial, 11"),key='-button-'),sg.Button('Скасувати',size=(18),font=("Arial, 11"),key='Cancel')]
        ]

        window=sg.Window('DataBase',layout,size=(330,100))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_Column=values.get('Column_name')
                    self.data=values.get('Value_name')
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')
    

    def create_full_DataBase(self): 

        layout=[
            [sg.Text('Введіть назву бази даних',font=("Arial, 11")),sg.Input(key='DataBase_name')],
            [sg.Text('Введіть назву таблиці',font=("Arial, 11")),sg.Input(key='Table_name')],
            [sg.Text('Введіть кількість стовпців, яку створити',font=("Arial, 11")),sg.Input(key='number')],
            [sg.Button('Створити',key='-button-',size=(18),font=("Arial, 11")),sg.Button('Скасувати',key='Cancel',size=(18),font=("Arial, 11"))]
        ]

        window=sg.Window('DataBase',layout,size=(350,125))

        while True:

            try:
                event,values=window.read()

                if event==sg.WIN_CLOSED:
                    break

                if event=='Cancel':
                    window.close()
                
                if event=='-button-':
                    self.name_of_DataBase=values.get('DataBase_name')
                    self.name_of_Table=values.get('Table_name')
                    self.number=int(values.get('number'))
                    time.sleep(0.2)
                    window.close()
            
            except KeyError:
                self.voice.say_message('Error!')
            
            except ValueError:
                self.voice.say_message('Enter value!')
            
            except Exception:
                self.voice.say_message('Error!')