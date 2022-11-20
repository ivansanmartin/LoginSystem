import hashlib
from SQLConnect import Connect
from LoginAccount import validate_entry  # obtener lista de usuarios y contrasenas

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
        changue_type()
    elif option == "2":
        exit()


def changue_type():
    user_changue = str(input("Ingrese el nombre de usuario para cambiar el tipo: "))
    options = ["1", "2"]
    for i in validate_entry():
        if i[0] != user_changue:
            print("Has ingresado un usuario que no existe en el sistema.")

        elif i[0] == user_changue:

            print("""
            Ingrese el tipo de usuario que quiera establecer.
            
            (Admin | User)
            
            """)

            type_user = str(input(": "))
            if type_user == "Admin":
                cursor.execute(f"""UPDATE USUARIO SET TYPE_USER_ID = 2 WHERE USERNAME = '{user_changue}';""")
                Connect.con.commit()
                print(f"El tipo de usuario de {user_changue} ha sido establecido como Admin")
                menu_root()
            elif type_user == "User":
                cursor.execute(f"""UPDATE USUARIO SET TYPE_USER_ID = 1 WHERE USERNAME = '{user_changue}';""")
                Connect.con.commit()
                print(f"El tipo de usuario de {user_changue} ha sido establecido como User")
                menu_root()

        print("""
                  1. Ver lista de usuario
                  2. Salir
                  """)
        view_users = str(input(": "))

        while view_users not in options:
            print("Has ingresado una opcion que no existe.")
            view_users = str(input(": "))

        if view_users == "1":
            for users in validate_entry():
                print(users[0])
            changue_type()
