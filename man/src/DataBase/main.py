import sys
sys.path.append('.')
from src.DataBase.GUI import Design
from src.DataBase.controller import Controller
from src.System.main import Voice

class DataBase:
    
    def __init__(self):
        self.data_base=Controller()
        self.voice=Voice()
        self.design=Design()
    

    def create_DataBase(self):

        try:
            self.design.create_DataBase()
            self.data_base.create_DataBase(self.design.name_of_DataBase)
        
        except Exception as e:
            self.voice.say_message('Error!')
            print(e)


    def create_Table(self):

        try:
            self.design.create_Table()
            self.data_base.create_Table(self.design.name_of_DataBase,self.design.name_of_Table)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def create_Column(self):

        try:
            self.design.create_Column_1()
            self.data_base.create_Column(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def rename_Table(self):

        try:
            self.design.change_name_of_Table()
            self.data_base.change_name_of_Table(self.design.name_of_DataBase,self.design.name_of_Table,self.design.new_name_of_Table)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def rename_Column(self):
        
        try:
            self.design.change_name_of_Column_1()
            self.data_base.change_name_of_Column(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def change_type_Column(self):

        try:
            self.design.change_type_of_Column_1()
            self.data_base.change_type_of_Column(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def delete_Table(self):

        try:
            self.design.delete_Table()
            self.data_base.delete_Table(self.design.name_of_DataBase,self.design.name_of_Table)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def delete_Column(self):

        try:
            self.design.delete_Column()
            self.data_base.delete_Column(self.design.name_of_DataBase,self.design.name_of_Column)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def add_data_toColumn(self):

        try:
            self.design.add_data_toColumn_1()
            self.data_base.add_data_toColumn(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def change_data_inColumn(self):

        try:
            self.design.change_data_inColumn_1()
            self.data_base.change_data_in_Column(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def delete_data_fromColumn(self):

        try:
            self.design.delete_Data_1()
            self.data_base.delete_Data(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')


    def show_fullTable(self):

        try:
            self.data_base.show_DataBase()
        
        except Exception as e:
            self.voice.say_message('Error!')


    def create_full_DataBase(self):

        try:
            self.design.create_full_DataBase()
            self.data_base.create_full_DataBase(self.design.name_of_DataBase,self.design.name_of_Table,self.design.number)
        
        except Exception as e:
            self.voice.say_message('Error!')
    

    def delete_DataBase(self):
        pass