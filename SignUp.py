from dbUsers import *

specialCharacters = """!@\#$%^&*()_+=-[]{};'"/~?.,<> """
spec = 0

class SignUp:


    def dodanieNowegoUzytkownika(self, name, surrname, tableForUsers, dbForUsers, spec):
        if any(iName.isnumeric() for iName in name) or any(cName in specialCharacters for cName in name):
            print("Wprowadź poprawne imię:litery bez cyfer, znaków specjalnych")
        elif len(name) < 2:
            print("Imię użytkownika musi składać się przynajmniej z 2 znaków")
        elif any(iSurr.isnumeric() for iSurr in surrname) or any(
                cSurr in specialCharacters for cSurr in surrname):
            print("Wprowadź poprawne naziwsko: litery bez cyfer, znaków specjalnych")
        elif len(surrname) < 2:
            print("Nazwisko użytkownika musi składać się przynajmniej z 2 znaków")
        else:
            db = dbInitialization(dbForUsers)
            db.create_table(f'CREATE TABLE IF NOT EXISTS {tableForUsers} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text, status text, permissions text)')
            row = db.return_record('users', name, surrname)
            if row is None:
                email = name + "." + surrname + "@firma.com"
                status = "active"
                permissions = "common"
                db.insert('users', name, surrname, email, status, permissions)
                spec = 5
            else:
                spec = 10
        return name, surrname, spec
