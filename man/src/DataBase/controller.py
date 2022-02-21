import sys
import sqlite3
import time

try:
    sys.path.append('.')
    from src.System.main import Voice
    from src.DataBase.GUI import Design

except ImportError:
    print('Error')

except SystemError:
    print('Error')

except FileNotFoundError:
    print('Error')

except ModuleNotFoundError:
    print('Error')


class Controller:

    def __init__(self):
        self.voice=Voice()
        self.design=Design()


    def create_DataBase(self,name_of_DataBase):

        try:
            # name_Folder=input('Введіть шлях для створення бази даних:::')
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            bd.commit()
            time.sleep(0.2)
            self.voice.say_message('Data base was created!')
            bd.close()
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def create_Table(self,name_of_DataBase,name_of_Table):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_of_Table}(id INTEGER NOT NULL,PRIMARY KEY(id))""")  #створити стоапець без типу для легшої заміни
            bd.commit()
            time.sleep(0.2)
            self.voice.say_message('Table was created!')
            bd.close()
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def create_Column(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()

            for i in range(number):
                self.design.create_Column_2()
                sql.execute(f"ALTER TABLE {name_of_Table} ADD COLUMN {self.design.name_of_Column} {self.design.type_of_Column}")
                bd.commit()
                time.sleep(0.1) 
                self.voice.say_message('Column was created!')

        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def add_data_toColumn(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()

            for i in range(number):
                self.design.add_data_toColumn_2()
                sql.execute(f"INSERT INTO {name_of_Table}({self.design.name_of_Column}) VALUES('')")
                bd.commit()
                sql.execute(f"UPDATE '{name_of_Table}' SET '{self.design.name_of_Column}'='{self.design.data}' WHERE id={self.design.id}")
                bd.commit()
                time.sleep(0.1)
                self.voice.say_message('Data was added to column!')

        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def change_data_in_Column(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()

            for i in range(number):
                self.design.change_data_inColumn_2()
                sql.execute(f"UPDATE '{name_of_Table}' SET '{self.design.name_of_Column}'='{self.design.data}' WHERE id={self.design.id}")
                bd.commit()
                time.sleep(0.1)
                self.voice.say_message('Data was updated!')

        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!') 


    def change_type_of_Column(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()

            for i in range(number):
                self.design.change_type_of_Column_2()
                # sql.execute(f"EXEC sp_rename '{name_of_Table}' ALTER COLUMN {nameColumn} {type_of_Column}")
                sql.execute(f'ALTER TABLE {name_of_Table} ALTER COLUMN {self.design.name_of_Column} {self.design.type_of_Column}')
                bd.commit()
                time.sleep(0.1)
                self.voice.say_message(f'Type of column was changed on {self.design.type_of_Column}')

        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def delete_Data(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()

            for i in range(number):
                self.design.delete_Data_2()
                sql.execute(f"DELETE FROM {name_of_Table} WHERE {self.design.name_of_Column}='{self.design.data}'")
                bd.commit()
                time.sleep(0.1)
                self.voice.say_message('Data was removed from column!')
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def show_DataBase(self):
        name_of_DataBase=input("Введіть назву бази даних:::")
        bd=sqlite3.connect(f'{name_of_DataBase}.bd')
        name_of_Table=input("Введіть назву таблиці:::")
        sql=bd.cursor()
        bd.commit()

        try:
            for i in sql.execute(f"SELECT * FROM {name_of_Table}"):
                print(i) #Доробити нюанси
            
            time.sleep(0.2)
            bd.close()

        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')
    

    def change_name_of_Table(self,name_of_DataBase,name_of_Table,new_name_of_Table):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            sql.execute(f'ALTER TABLE {name_of_Table} RENAME TO {new_name_of_Table}')
            bd.commit()
            time.sleep(0.2)
            self.voice.say_message(f'Table name was changed on {new_name_of_Table}')
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')
    
    
    def delete_Table(self,name_of_DataBase,name_of_Table):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            sql.execute(f'DROP TABLE {name_of_Table}')
            bd.commit()
            time.sleep(0.2)
            self.voice.say_message('Table was removed!')
            bd.close()
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def change_name_of_Column(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            bd.commit()
            
            for i in range(number):
                self.design.change_name_of_Column_2()
                sql.execute(f'ALTER TABLE {name_of_Table} RENAME COLUMN {self.design.name_of_Column} TO {self.design.new_name_of_Column}')
                bd.commit()
                time.sleep(0.2)
                self.voice.say_message('Column name was changed!')
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')

    
    def delete_Column(self,name_of_DataBase,name_of_Table,name_of_Column):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            sql.execute(f'ALTER TABLE {name_of_Table} DROP COLUMN {name_of_Column}')
            bd.commit()
            time.sleep(0.2)
            self.voice.say_message('Column was removed!')
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')


    def create_full_DataBase(self,name_of_DataBase,name_of_Table,number):

        try:
            bd=sqlite3.connect(f'{name_of_DataBase}.bd')
            sql=bd.cursor()
            sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_of_Table}(id INTEGER NOT NULL,PRIMARY KEY(id))""")   #створити стоапець без типу для легшої заміни
            bd.commit()

            for i in range(number):
                self.design.create_Column_2()
                sql.execute(f"ALTER TABLE {name_of_Table} ADD COLUMN {self.design.name_of_Column} {self.design.type_of_Column}")
                bd.commit()
                time.sleep(0.1)
                self.voice.say_message('Column was created!')
        
        except sqlite3.OperationalError:
            self.voice.say_message('Error!')
        
        except AttributeError:
            time.sleep(0.5)
            self.voice.say_message('Enter values!')
        
        except Exception:
            self.voice.say_message('Error!')