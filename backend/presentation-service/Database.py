# @Author: Daniil Maslov (ComicSphinx)

import sqlite3
import os

# Модуль работы с бд - игрушечный.
# Для пром.эксплуатации, скорее всего, его надо будет переделать на что-то более серьезное

class Database():
    database_file_path = "db/database.db"
    presentations_table_name = "presentations"

    # TODO: Зарефакторить этот метод (вместе с getPresentationsList)
    # row[0] чтобы очистить от лишних скобок, убрать список
    def getPresentationById(self, presentationId, field):
        request = "SELECT "+field+" FROM " + self.presentations_table_name + " WHERE presentationId =" + str(presentationId) + " AND active = true"
        connection, cursor = self.connectDB(self)
        for row in cursor.execute(request):
            presentation = row[0]
        self.saveAndCloseDB(self, connection)
        return presentation

    def getPresentationsList(self, field):
        request = "SELECT "+field+" FROM " + self.presentations_table_name + " WHERE active = true"
        presentation = self.executeRequest(self, request)
        return presentation

    def checkDatabaseIsExist(self):
        if (os.path.exists(self.database_file_path)):
            return 1
        else:
            return 0

    def createDB(self):
        output = self.executeRequest(self, "CREATE TABLE " + self.presentations_table_name + " (presentationId INT, title VARCHAR(60), description VARCHAR(255), descriptionTitle VARCHAR(60), firstImage VARCHAR(255), secondImage VARCHAR(255)," +
                         "thirdImage VARCHAR(255), fourthImage VARCHAR(255), fifthImage VARCHAR(255), sixthImage VARCHAR(255), seventhImage VARCHAR(255), eightImage VARCHAR(255), mainImage VARCHAR(255), active BOOL);")
        
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