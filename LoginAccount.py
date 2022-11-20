from SQLConnect import Connect
import hashlib

cur = Connect()
cursor = cur.con.cursor()


def validate_entry():
    sql = """SELECT username, password FROM USUARIO;"""
    cursor.execute(sql)
    datos = cursor.fetchall()

    return datos





