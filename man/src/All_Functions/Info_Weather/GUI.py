import time
import sys
import PySimpleGUI as sg

sys.path.append('.')
try:
    from src.All_Functions.Info_Weather.controller import InfoWeather

except ImportError:
    print('Помилка!')


class Design:

    sg.theme('DarkBlue14')

    def __init__(self):
        self.weather=InfoWeather()


    def get_weather(self,city):
        
        self.weather.get_page(city)
        self.weather.get_weather()
        
        layout=[
            [sg.Text('Місто:',font=('Times New Roman',12)),sg.Text(key='name_of_city',font=("Arial, 11"))],
            [sg.Text('На сьогодні:',font=('Times New Roman',12)),sg.Text(key='info_about_weather',font=("Arial, 11"))],
            [sg.Text('Температура:',font=('Times New Roman',12)),sg.Text(key='temperature',font=("Arial, 11"))],
            [sg.Text('Min температура:',font=('Times New Roman',12)),sg.Text(key='min_temperature',font=("Arial, 11"))],
            [sg.Text('Max температура:',font=('Times New Roman',12)),sg.Text(key='max_temperature',font=("Arial, 11"))],
            [sg.Button('Закрити',key='Close',size=(21),font=("Arial, 12")),sg.Button('Оновити',key='Update',size=(21),font=("Arial, 12"))]
        ]

        window=sg.Window(title='Погода',layout=layout,size=(560,185))

        while True:
            event,values=window.read()

            if event==sg.WIN_CLOSED:
                break

            if event=='Close':
                time.sleep(0.2)
                window.close()
            
            if event=='Update':
                window['name_of_city'].update(self.weather.location)
                window['info_about_weather'].update(self.weather.info_about_weather_now)
                window['temperature'].update(self.weather.temperature)
                window['min_temperature'].update(self.weather.min_temperature)
                window['max_temperature'].update(self.weather.max_temperature)


    def get_weather_all_week(self,city):

        self.weather.get_page(city)
        self.weather.get_weather_all_week(city)

        layout=[
            [sg.Text('',key='day_1',font=('Times New Roman',12)),sg.Text('',k='info_1',justification='right',size=(100,1))],
            [sg.Text('',key='day_2',font=('Times New Roman',12)),sg.Text('',k='info_2',justification='right',size=(100,1))],
            [sg.Text('',key='day_3',font=('Times New Roman',12)),sg.Text('',k='info_3',justification='right',size=(100,1))],
            [sg.Text('',key='day_4',font=('Times New Roman',12)),sg.Text('',k='info_4',justification='right',size=(100,1))],
            [sg.Text('',key='day_5',font=('Times New Roman',12)),sg.Text('',k='info_5',justification='right',size=(100,1))],
            [sg.Text('',key='day_6',font=('Times New Roman',12)),sg.Text('',k='info_6',justification='right',size=(100,1))],
            [sg.Text('',key='day_7',font=('Times New Roman',12)),sg.Text('',k='info_7',justification='right',size=(100,1))],
            [sg.Button('Закрити',key='Close',size=(22),font=("Arial, 12")),sg.Button('Оновити',key='Show',size=(22),font=("Arial, 12"))]
        ]

        window=sg.Window('Погода на тиждень',layout,size=(450,250))

        while True:
            event,values=window.read()

            if event==sg.WIN_CLOSED:
                break

            if event=='Close':
                window.close()

            if event=='Show':
                window['day_1'].update(self.weather.day_1)
                window['info_1'].update(self.weather.temperature_1)
                window['day_2'].update(self.weather.day_2)
                window['info_2'].update(self.weather.temperature_2)
                window['day_3'].update(self.weather.day_3)
                window['info_3'].update(self.weather.temperature_3)
                window['day_4'].update(self.weather.day_4)
                window['info_4'].update(self.weather.temperature_4)
                window['day_5'].update(self.weather.day_5)
                window['info_5'].update(self.weather.temperature_5)
                window['day_6'].update(self.weather.day_7)
                window['info_6'].update(self.weather.temperature_7)
                window['day_7'].update(self.weather.day_7)
                window['info_7'].update(self.weather.temperature_7)



    def get_weather_ten_days(self,city):

        self.weather.get_weather_ten_days(city)

        layout=[
            [sg.Text('',key='day_1',font=('Times New Roman',12)),sg.Text('',k='info_1',justification='right',size=(100,1))],
            [sg.Text('',key='day_2',font=('Times New Roman',12)),sg.Text('',k='info_2',justification='right',size=(100,1))],
            [sg.Text('',key='day_3',font=('Times New Roman',12)),sg.Text('',k='info_3',justification='right',size=(100,1))],
            [sg.Text('',key='day_4',font=('Times New Roman',12)),sg.Text('',k='info_4',justification='right',size=(100,1))],
            [sg.Text('',key='day_5',font=('Times New Roman',12)),sg.Text('',k='info_5',justification='right',size=(100,1))],
            [sg.Text('',key='day_6',font=('Times New Roman',12)),sg.Text('',k='info_6',justification='right',size=(100,1))],
            [sg.Text('',key='day_7',font=('Times New Roman',12)),sg.Text('',k='info_7',justification='right',size=(100,1))],
            [sg.Text('',key='day_8',font=('Times New Roman',12)),sg.Text('',k='info_8',justification='right',size=(100,1))],
            [sg.Text('',key='day_9',font=('Times New Roman',12)),sg.Text('',k='info_9',justification='right',size=(100,1))],
            [sg.Text('',key='day_10',font=('Times New Roman',12)),sg.Text('',k='info_10',justification='right',size=(100,1))],
            [sg.Button('Закрити',key='Close',size=(22),font=("Arial, 12")),sg.Button('Оновити',key='Show',size=(22),font=("Arial, 12"))]
        ]

        window=sg.Window('Погода на 10 днів',layout,size=(450,335))

        while True:
            event,values=window.read()

            if event==sg.WIN_CLOSED:
                break

            if event=='Close':
                window.close()

            if event=='Show':
                window['day_1'].update(self.weather.day_1)
                window['info_1'].update(self.weather.temperature_1)
                window['day_2'].update(self.weather.day_2)
                window['info_2'].update(self.weather.temperature_2)
                window['day_3'].update(self.weather.day_3)
                window['info_3'].update(self.weather.temperature_3)
                window['day_4'].update(self.weather.day_4)
                window['info_4'].update(self.weather.temperature_4)
                window['day_5'].update(self.weather.day_5)
                window['info_5'].update(self.weather.temperature_5)
                window['day_6'].update(self.weather.day_7)
                window['info_6'].update(self.weather.temperature_7)
                window['day_7'].update(self.weather.day_7)
                window['info_7'].update(self.weather.temperature_7)
                window['day_8'].update(self.weather.day_8)
                window['info_8'].update(self.weather.temperature_8)
                window['day_9'].update(self.weather.day_9)
                window['info_9'].update(self.weather.temperature_9)
                window['day_10'].update(self.weather.day_10)
                window['info_10'].update(self.weather.temperature_10)