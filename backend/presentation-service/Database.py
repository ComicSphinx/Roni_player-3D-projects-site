# @Author: Daniil Maslov (ComicSphinx)

import sqlite3
import os

# Модуль работы с бд - игрушечный.
# Для пром.эксплуатации, скорее всего, его надо будет переделать на что-то более серьезное

class Database():
    database_file_path = "db/database.db"
    presentations_table_name = "presentations"

    def getPresentationById(self, presentation_id, field):
        # TODO: Надо будет переработать этот метод и сделать так, чтобы он возвращал JSON
        # Либо собирать JSON в PresentationService.py
        request = "SELECT "+field+" FROM " + self.presentations_table_name + " WHERE presentation_id =" + str(presentation_id) + " AND active = true"
        presentation = self.executeRequest(self, request)
        return presentation

    def checkDatabaseIsExist(self):
        if (os.path.exists(self.database_file_path)):
            return 1
        else:
            return 0

    def createDB(self):
        output = self.executeRequest(self, "CREATE TABLE " + self.presentations_table_name + " (presentation_id INT, title VARCHAR(60), description VARCHAR(255), description_title VARCHAR(60), first_img VARCHAR(255), second_img VARCHAR(255)," +
                         "third_img VARCHAR(255), fourth_img VARCHAR(255), fifth_img VARCHAR(255), sixth_img VARCHAR(255), seventh_img VARCHAR(255), eight_img VARCHAR(255), active BOOL);")
        print(output)

    def executeRequest(self, request):
        # При введении в пром.эксплуатацию этот метод надо будет сделать безопасным или вырезать. Сейчас его может использовать кто угодно извне
        connection, cursor = self.connectDB(self)
        cursor.execute(request)
        output = cursor.fetchall()
        self.saveAndCloseDB(self, connection)
        return output

    def connectDB(self):
        # подключение настроено только на presentations.db, в дальнейшем
        # надо будет прикрутить аргумент - название таблички
        connection = sqlite3.connect(self.database_file_path)
        cursor = connection.cursor()
        return connection, cursor
    
    def saveAndCloseDB(self, connection):
        connection.commit()
        connection.close()

    def secureInitDB(self):
        if (self.checkDatabaseIsExist(self) == 0):
            self.createDB(self)
            print("database created")