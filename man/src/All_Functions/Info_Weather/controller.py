import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('.')
from src.System.main import Voice


class InfoWeather:

    def __init__(self):
        self.voice=Voice()
    

    def get_page(self,city):

        try:
            page=requests.get(url=f'https://ua.sinoptik.ua/погода-{city}')
            global soup
            soup=BeautifulSoup(page.text,'html.parser')
        
        except requests.ConnectionError:
            self.voice.say_message('Error')

        except requests.HTTPError:
            self.voice.say_message('Error')

        except requests.RequestException:
            self.voice.say_message('Error')
    

    def get_weather(self):

        try:

            self.location=soup.find('div',class_='cityName cityNameShort').text
            self.info_about_weather_now=soup.find('div',class_='description').text
            self.temperature=soup.find('p',class_='today-temp').text
            self.min_temperature=soup.find('div',class_='min').text
            self.max_temperature=soup.find('div',class_='max').text
        
        except NameError:
            self.voice.say_message('Error')

        except requests.ConnectionError:
            self.voice.say_message('Error')

        except requests.HTTPError:
            self.voice.say_message('Error')

        except requests.RequestException:
            self.voice.say_message('Error')
        

    def get_weather_all_week(self,city):

        try:
            InfoWeather().get_page(city)

            day_link_1=soup.find('p',class_='day-link').text
            date_1=soup.find('p',class_='date').text
            mounth_1=soup.find('p',class_='month').text
            self.day_1=day_link_1+' '+date_1+' '+mounth_1
            self.temperature_1=soup.find('div',id='bd1').find('div',class_='temperature').text


            day_link_2=soup.find('div',id='bd2').find('a',class_='day-link').text
            data_2=soup.find('div',id='bd2').find('p',class_='date').text
            mounth_2=soup.find('div',id='bd2').find('p',class_='month').text
            self.day_2=day_link_2+' '+data_2+' '+mounth_2
            self.temperature_2=soup.find('div',id='bd2').find('div',class_='temperature').text


            day_link_3=soup.find('div',id='bd3').find('a',class_='day-link').text
            data_3=soup.find('div',id='bd3').find('p',class_='date').text
            mounth_3=soup.find('div',id='bd3').find('p',class_='month').text
            self.day_3=day_link_3+' '+data_3+' '+mounth_3
            self.temperature_3=soup.find('div',id='bd3').find('div',class_='temperature').text


            day_link_4=soup.find('div',id='bd4').find('a',class_='day-link').text
            data_4=soup.find('div',id='bd4').find('p',class_='date').text
            mounth_4=soup.find('div',id='bd4').find('p',class_='month').text
            self.day_4=day_link_4+' '+data_4+' '+mounth_4
            self.temperature_4=soup.find('div',id='bd4').find('div',class_='temperature').text


            day_link_5=soup.find('div',id='bd5').find('a',class_='day-link').text
            data_5=soup.find('div',id='bd5').find('p',class_='date').text
            mounth_5=soup.find('div',id='bd5').find('p',class_='month').text
            self.day_5=day_link_5+' '+data_5+' '+mounth_5
            self.temperature_5=soup.find('div',id='bd5').find('div',class_='temperature').text


            day_link_6=soup.find('div',id='bd6').find('a',class_='day-link').text
            data_6=soup.find('div',id='bd6').find('p',class_='date').text
            mounth_6=soup.find('div',id='bd6').find('p',class_='month').text
            self.day_6=day_link_6+' '+data_6+' '+mounth_6
            self.temperature_6=soup.find('div',id='bd6').find('div',class_='temperature').text


            day_link_7=soup.find('div',id='bd7').find('a',class_='day-link').text
            data_7=soup.find('div',id='bd7').find('p',class_='date').text
            mounth_7=soup.find('div',id='bd7').find('p',class_='month').text
            self.day_7=day_link_7+' '+data_7+' '+mounth_7
            self.temperature_7=soup.find('div',id='bd7').find('div',class_='temperature').text
        
        except NameError:
            self.voice.say_message('Error')

        except requests.ConnectionError:
            self.voice.say_message('Error')

        except requests.HTTPError:
            self.voice.say_message('Error')

        except requests.RequestException:
            self.voice.say_message('Error')
    

    def get_weather_ten_days(self,city):

        try:

            page=requests.get(url=f'https://ua.sinoptik.ua/погода-{city}/10-днів')
            soup=BeautifulSoup(page.text,'html.parser')

            day_link_1=soup.find('p',class_='day-link').text
            date_1=soup.find('p',class_='date').text
            mounth_1=soup.find('p',class_='month').text
            self.day_1=day_link_1+' '+date_1+' '+mounth_1
            self.temperature_1=soup.find('div',id='bd1').find('div',class_='temperature').text


            day_link_2=soup.find('div',id='bd2').find('a',class_='day-link').text
            data_2=soup.find('div',id='bd2').find('p',class_='date').text
            mounth_2=soup.find('div',id='bd2').find('p',class_='month').text
            self.day_2=day_link_2+' '+data_2+' '+mounth_2
            self.temperature_2=soup.find('div',id='bd2').find('div',class_='temperature').text


            day_link_3=soup.find('div',id='bd3').find('a',class_='day-link').text
            data_3=soup.find('div',id='bd3').find('p',class_='date').text
            mounth_3=soup.find('div',id='bd3').find('p',class_='month').text
            self.day_3=day_link_3+' '+data_3+' '+mounth_3
            self.temperature_3=soup.find('div',id='bd3').find('div',class_='temperature').text


            day_link_4=soup.find('div',id='bd4').find('a',class_='day-link').text
            data_4=soup.find('div',id='bd4').find('p',class_='date').text
            mounth_4=soup.find('div',id='bd4').find('p',class_='month').text
            self.day_4=day_link_4+' '+data_4+' '+mounth_4
            self.temperature_4=soup.find('div',id='bd4').find('div',class_='temperature').text


            day_link_5=soup.find('div',id='bd5').find('a',class_='day-link').text
            data_5=soup.find('div',id='bd5').find('p',class_='date').text
            mounth_5=soup.find('div',id='bd5').find('p',class_='month').text
            self.day_5=day_link_5+' '+data_5+' '+mounth_5
            self.temperature_5=soup.find('div',id='bd5').find('div',class_='temperature').text


            day_link_6=soup.find('div',id='bd6').find('a',class_='day-link').text
            data_6=soup.find('div',id='bd6').find('p',class_='date').text
            mounth_6=soup.find('div',id='bd6').find('p',class_='month').text
            self.day_6=day_link_6+' '+data_6+' '+mounth_6
            self.temperature_6=soup.find('div',id='bd6').find('div',class_='temperature').text


            day_link_7=soup.find('div',id='bd7').find('a',class_='day-link').text
            data_7=soup.find('div',id='bd7').find('p',class_='date').text
            mounth_7=soup.find('div',id='bd7').find('p',class_='month').text
            self.day_7=day_link_7+' '+data_7+' '+mounth_7
            self.temperature_7=soup.find('div',id='bd7').find('div',class_='temperature').text


            day_link_8=soup.find('div',id='bd8').find('a',class_='day-link').text
            data_8=soup.find('div',id='bd8').find('p',class_='date').text
            mounth_8=soup.find('div',id='bd8').find('p',class_='month').text
            self.day_8=day_link_8+' '+data_8+' '+mounth_8
            self.temperature_8=soup.find('div',id='bd8').find('div',class_='temperature').text


            day_link_9=soup.find('div',id='bd9').find('a',class_='day-link').text
            data_9=soup.find('div',id='bd9').find('p',class_='date').text
            mounth_9=soup.find('div',id='bd9').find('p',class_='month').text
            self.day_9=day_link_9+' '+data_9+' '+mounth_9
            self.temperature_9=soup.find('div',id='bd9').find('div',class_='temperature').text


            day_link_10=soup.find('div',id='bd10').find('a',class_='day-link').text
            data_10=soup.find('div',id='bd10').find('p',class_='date').text
            mounth_10=soup.find('div',id='bd10').find('p',class_='month').text
            self.day_10=day_link_10+' '+data_10+' '+mounth_10
            self.temperature_10=soup.find('div',id='bd10').find('div',class_='temperature').text
        
        except NameError:
            self.voice.say_message('Error')

        except requests.ConnectionError:
            self.voice.say_message('Error')

        except requests.HTTPError:
            self.voice.say_message('Error')

        except requests.RequestException:
            self.voice.say_message('Error')
        
        except AttributeError:
            self.voice.say_message('Error')