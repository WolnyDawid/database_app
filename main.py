from SignUp import *

dbForUsers = "usersDatabase.db"
tableForUsers = "users"
dbForThings = "thingsDatabase.db"
tableForThings = "things"
permision = 0


def logowanie(name, surrname, tableForUsers, dbForUsers, status_):
    db = dbInitialization(dbForUsers)
    db.create_table(f'CREATE TABLE IF NOT EXISTS {tableForUsers} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text, status text, permissions text)')
    row = db.return_record('users', name, surrname)
    if row is None:
        print('chujnia1')
        status_ = 'error'
    elif "common" in row:
        print('tak to jest common')
        status_ = 'common'
    elif "admin" in row:
        print('tak to jest common')
        status_ = 'admin'
    else:
        print('chujnia2')
    return name, surrname, status_


def log(tableForUsers_, dbForUsers_):
    status = ''
    # existingUserName = input("Podaj imię użytkownika: ")
    # existingUserSurrname = input("Podaj nazwisko: ")
    existingUserName = 'qwerty'
    existingUserSurrname = 'qwerty'
    user = logowanie(existingUserName, existingUserSurrname, tableForUsers_, dbForUsers_, status)
    if 'error' in user[2]:
        permision = 0
    elif 'common' in user[2]:
        permision = 1
    elif 'admin' in user[2]:
        permision = 2
    return existingUserName, existingUserSurrname, permision


def reg(tableForUsers_, dbForUsers_):
    newUserName = 'qwerty' #input("Podaj imię użytkownika: ")
    newUserSurrname = 'qwerty' #input("Podaj nazwisko: ")
    SignUp().dodanieNowegoUzytkownika(newUserName, newUserSurrname, tableForUsers_, dbForUsers_, spec)


_log = log(tableForUsers, dbForUsers)
print(_log[0], _log[1], _log[2])
reg(tableForUsers, dbForUsers)

