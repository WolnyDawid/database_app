import sqlite3


class dbInitialization:
    def __init__(self, dbForUsers):
        self.var = None
        self.logInInformation = None
        self.connection = sqlite3.connect(dbForUsers)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, tableForUsers, *values):
        self.cursor.execute(f'INSERT INTO {tableForUsers} (name, surrname, email, status, permissions) VALUES (?,?,?,?,?)', values)
        self.connection.commit()

    def return_record(self, tableForUsers, *existingValues):
        self.cursor.execute(f'SELECT * FROM {tableForUsers} WHERE name= ? and surrname= ?', existingValues)
        self.var = self.cursor.fetchone()
        return self.var