from SQLConnect import Connect
import hashlib

cur = Connect()
cursor = cur.con.cursor()


class UserLogin:
    def __init__(self):
        self.username = None
        self.password_entry = None

    def validate_entry(self):
        sql = """SELECT username, password FROM USUARIO;"""
        result = hashlib.md5(self.password_entry.encode())
        self.password_entry = result.hexdigest()
        cursor.execute(sql)
        datos = cursor.fetchall()

        for i in datos:
            if i[0] == self.username and i[1] == self.password_entry:
                print("Sesión inciada correctamente!")
                break
            elif i[0] != self.username or i[0] != self.password_entry:
                print("Contraseña o usuario incorrectos!")
                break

