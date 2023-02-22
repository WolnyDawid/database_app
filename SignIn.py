from dbUsers import *


class SignIn:

    def logowanie(self, name, surrname, tableForUsers, dbForUsers):
        db = dbInitialization(dbForUsers)
        db.create_table(f'CREATE TABLE IF NOT EXISTS {tableForUsers} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text, status text, permissions text)')
        row = db.return_record('users', name, surrname)
        print(row)