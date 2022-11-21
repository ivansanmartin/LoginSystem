from SQLConnect import Connect
import hashlib

cur = Connect()

cursor = cur.con.cursor()


class Register:
    def __int__(self):
        self.username = None
        self.password = None
        self.password_confirm = None

    def entry_user_password(self):
        result = hashlib.md5(self.password.encode())
        password = result.hexdigest()
        sql = f"""INSERT INTO USUARIO (username, password, type_user_id) 
                               VALUES ('{self.username}', '{password}', 2);"""
        cursor.execute(sql)
        Connect.con.commit()



