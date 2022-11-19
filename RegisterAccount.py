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
        print(result.hexdigest())
        cursor.execute(
            f"""INSERT INTO USUARIO (USERNAME, PASSWORD, TYPE_USER_ID) VALUES ('{self.username}', '{result.hexdigest()}', 1)""")
        Connect.con.commit()
        cursor.close()


