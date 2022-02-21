database_dict={
    "create data base":("створити базу даних","створи нову базу даних","створи базу даних","нова база даних","створи базу","створи нову базу даних"),
    "create full data base":("створити фулл базу","створити повну базу даних","створити базу даних з стовпцями","створити основу бази даних","створи фулл базу даних"),
    "create table":("створити таблицю","створи нову таблицю","створи таблицю в базі даних","створити нову таблицю в базі даних","створи нову таблицю в базі даних","створи нову таблицю в базі"),
    "create column":("створи стовпець","створи новий стовпець","створи стовпці","створити стовпці","створи нові стовпці","створи стовпці в таблиці","створи нові стовпці в таблиці","створи стовпці в базі даних"),
    "add data to column":("додай значення до бази даних","додай значення до таблиці","помісти значення в таблицю","додай значення до стовпця","помісти значення в стовпець","додай нові значення","добав значення","добав нові значення","додати значення до бази даних","помісти нові значення до таблиці"),
    "delete data from column":("видали значення з стовпця","видали значення з таблиці","видали значення з бази даних","видалити значення","видали значення з стовпців"),
    "delete table":("видали таблицю","видали таблицю з бази даних","видали таблицю","видали таблицю з стовпцями"),
    "change name of table":("зміни назву таблиці","зміни ім`я таблиці","редагуй імя таблиці","поміняй назву таблиці","поміняй ім`я таблиці"),
    "change data in column":("зміни значення в таблиці","зміни значення стовпця","змінити значення","поміняй значення в таблиці","відредагуй значення в базі даних","відредагуй значення в таблиці"),
    "change type of column":("зміни тип стовпця","змінити тип стовпця","поміняй тип ствопця","редагуй тип стовпця"),
    "change name of column":("зміни назву стовпця","поміняй назву стовпця","проредагуй назву стовпця","змінити назву стовпця в таблиці"),
    "delete column":("видали cтовпець","видали стовпець з бази даних","видали cтовпець в базі даних","видали стовпець","забери стовпець з бази"),
    "show data in database":("покажи значення бази даних","покажи значення стовпців","виведи всі значення бази даних","покажи таблицю","покажи таблицю бази даних"),
    "close data base":("закрий базу даних")
}

other_command={
    "open_Browser":("відкрий браузер","відкрий google","відкрий вкладку","відкрий нову вкладку","відкрий нову вкладку в google"),
    "open_Chrome":("відкрий chrome","відкрий chrome в новій вкладці","chrome"),
    "open_YouTube":("відкрий youtube","youtube","відкрий youtube в новій вкладці"),
    "open_Program":("відкрий","відкрий програму"),
    "open_CMD":("відкрий консоль","відкрий термінал","відкрий cmd","відкрий командний рядок","покажи cmd","покажи консоль","консоль"),
    "Shutdown":("виключи комп`ютер","виключи комп","вимкни комп`ютер","вируби комп"),
    "Restart":("перезагрузи комп`ютер","перезагрузи комп","перезавнтаж комп`ютер"),
    "get_full_time":("який сьогодні день","який сьогодні рік","скажи сьогоднішню дату","покажи сьогоднішню дату","дата","сьогоднішня дата")
}



import sys
sys.path.append('.')
from src.DataBase.main import DataBase
from src.System.main import Recognizer,Voice
from src.All_Functions.Info_Weather.main import WeatherMap
from src.All_Functions.Other_methods.main import Operator
from src.All_Functions.Send_Message.main import Sender


class Dispatcher:

    def __init__(self):
        self.database=DataBase()
        self.recognizer=Recognizer()
        self.voice=Voice()
        self.weather=WeatherMap()
        self.operator=Operator()
        self.sender=Sender()
    

    def do_command(self):

        #DataBase
        for _ in database_dict.get('create data base'):
            if _==self.recognizer.command:
                self.database.create_DataBase()
        
        for _ in database_dict.get('create full data base'):
            if _==self.recognizer.command:
                self.database.create_full_DataBase()

        for _ in database_dict.get('create table'):
            if _==self.recognizer.command:
                self.database.create_Table()
        
        for _ in database_dict.get('create column'):
            if _==self.recognizer.command:
                self.database.create_Column()
        
        for _ in database_dict.get('add data to column'):
            if _==self.recognizer.command:
                self.database.add_data_toColumn()
        
        for _ in database_dict.get('delete data from column'):
            if _==self.recognizer.command:
                self.database.delete_data_fromColumn()
        
        for _ in database_dict.get('delete table'):
            if _==self.recognizer.command:
                self.database.delete_Table()
        
        for _ in database_dict.get('change name of table'):
            if _==self.recognizer.command:
                self.database.rename_Table()
        
        for _ in database_dict.get('change data in column'):
            if _==self.recognizer.command:
                self.database.change_data_inColumn()
        
        for _ in database_dict.get('change type of column'):
            if _==self.recognizer.command:
                self.database.change_type_Column()
        
        for _ in database_dict.get('change name of column'):
            if _==self.recognizer.command:
                self.database.rename_Column()
        
        for _ in database_dict.get('delete column'):
            if _==self.recognizer.command:
                self.database.delete_Column()
        
        for _ in database_dict.get('show data in database'):
            if _==self.recognizer.command:
                self.database.show_fullTable()
        

        #Get weather
        if 'знайди погоду в' in self.recognizer.command:
            new_command=self.recognizer.command.replace('знайди погоду в','')
            self.weather.getweather(new_command)
        
        elif 'знайди погоду у' in self.recognizer.command:
            new_command=self.recognizer.command.replace('знайди погоду у','')
            self.weather.getweather(new_command)
        
        elif 'пошукай погоду в місті' in self.recognizer.command:
            new_command=self.recognizer.command.replace('пошукай погоду в місті','')
            self.weather.getweather(new_command)
        
        elif 'покажи погоду в місті' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду в місті','')
            self.weather.getweather(city=new_command)
        
        elif 'покажи погоду на тиждень в' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду на тиждень в','')
            self.weather.getweatherAllWeek(new_command)
        
        elif 'покажи погоду на 7 днів в' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду на 7 днів в','')
            self.weather.getweatherAllWeek(new_command)
        
        elif 'покажи погоду на 7 днів в місті' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду на 7 днів в місті','')
            self.weather.getweatherAllWeek(new_command)
        
        elif 'покажи погоду на 10 днів в' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду на 10 днів в','')
            self.weather.getweatherTenDays(new_command)
        
        elif 'покажи погоду на 10 днів в місті' in self.recognizer.command:
            new_command=self.recognizer.command.replace('покажи погоду на 10 днів в місті','')
        

        elif 'відправ повідомлення' in self.recognizer.command or 'надішли повідомлення' in self.recognizer.command:
            self.sender.send_message()
            
        elif 'відправ файл' in self.recognizer.command or 'відправ файл на пошту' in self.recognizer.command:
            self.sender.send_file()
        


        #Other mathods
        for _ in other_command.get('open_Browser'):
            if _==self.recognizer.command:
                self.operator.open_browser()
        
        for _ in other_command.get('open_Chrome'):
            if _==self.recognizer.command:
                self.operator.open_Chrome()
        
        for _ in other_command.get('open_YouTube'):
            if _==self.recognizer.command:
                self.operator.open_youtube()

        if 'закрий' in self.recognizer.command:
            new_command=self.recognizer.command.replace('закрий','')
            self.operator.close_program(new_command)
        
        for _ in other_command.get('open_CMD'):
            if _==self.recognizer.command:
                self.operator.open_cmd()
        
        for _ in other_command.get('Shutdown'):
            if _==self.recognizer.command:
                self.operator.turn_off_computer()
        
        for _ in other_command.get('Restart'):
            if _==self.recognizer.command:
                self.operator.restart_computer()
        
        for _ in other_command.get('get_full_time'):
            if _==self.recognizer.command:
                self.operator.get_full_time()
        
        if 'погугли в інтернеті про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('погугли в інтернеті про','')
            self.operator.find_information_in_browser(new_command)
        
        elif 'знайди' in self.recognizer.command:
            new_command=self.recognizer.command.replace('знайди','')
            self.operator.find_information_in_browser(new_command)
        
        elif 'знайди про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('знайди про')
            self.operator.find_information_in_browser(new_command)

        elif 'пошукай в інтернеті про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('пошукай в інтернеті про','')
            self.operator.find_information_in_browser(new_command)

        elif 'пошукай про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('пошукай про','')
            self.operator.find_information_in_browser(new_command)

        elif 'погугли про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('погугли про','')
            self.operator.find_information_in_browser(new_command)

        elif 'погугли в інтернеті про' in self.recognizer.command:
            new_command=self.recognizer.command.replace('погугли в інтернеті про','')
            self.operator.find_information_in_browser(new_command)



if __name__=="__main__":

    while True:
        run=Dispatcher()
        run.recognizer.recognize_command()
        run.do_command()