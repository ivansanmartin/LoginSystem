import hashlib
from SQLConnect import Connect

cur = Connect()

cursor = cur.con.cursor()


def table_root():
    sql = "SELECT name, password FROM ROOT;"

    cursor.execute(sql)

    datos = cursor.fetchall()

    return datos


def menu_root():
    options_list = ["1", "2"]
    print("""
    
             ROOT
    
    1. Cambiar tipo de usuario
    2. Logout
    
    
    """)
    option = str(input(": "))

    while option not in options_list:
        print("Has ingresado un opcion que no existe, vuelve a intentarlo.")
        option = str(input(": "))

    if option == "1":
        change_type()
    elif option == "2":
        exit()


def list_users():
    sql = """SELECT username FROM USUARIO;"""
    datos = cursor.execute(sql)
    for user_list in datos.fetchall():
        print(user_list[0])


def change_type():
    user_change = str(input("Ingrese el nombre de usuario para cambiar el tipo: "))
    sql = """SELECT username FROM USUARIO;"""
    datos = cursor.execute(sql)

    users_db = list()

    for i in datos.fetchall():
        users_db.append(i[0])

    if user_change in users_db:
        print("""

        Escriba el tipo de usuario que desea establecer

        Admin | User

        """)
        print(users_db)
        type_user = str(input(": "))

        if type_user == "Admin":
            sql = f"""UPDATE USUARIO SET TYPE_USER_ID = 1 WHERE USERNAME = '{user_change}'"""
            cursor.execute(sql)
            Connect.con.commit()
            print(f"El usuario \"{user_change}\" ahora es administrador!")
            menu_root()
        elif type_user == "User":
            sql = f"""UPDATE USUARIO SET TYPE_USER_ID = 2 WHERE USERNAME = '{user_change}'"""
            cursor.execute(sql)
            Connect.con.commit()
            print(f"El usuario \"{user_change}\" ahora es usuario!")
            menu_root()

    elif user_change not in users_db:
        print("""

                    El usuario no ha sido encontrado!

                    1. Ver lista de usuarios
                    2. Logout



                    """)
        option = str(input(": "))

        while option not in ["1", "2"]:
            print("Opcion no valida (1 | 2)")
            option = str(input(": "))

        if option == "1":
            list_users()
            menu_root()
