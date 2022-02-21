import sys
sys.path.append('.')
from src.All_Functions.Info_Weather.GUI import Design

class WeatherMap:

    def __init__(self):
        self.weather=Design()

    def getweather(self,city):

        self.weather.get_weather(city)
    
    def getweatherAllWeek(self,city):

        self.weather.get_weather_all_week(city)

    def getweatherTenDays(self,city):

        self.weather.get_weather_ten_days(city)