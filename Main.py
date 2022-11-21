from RegisterAccount import Register
from LoginAccount import validate_entry
from SQLConnect import Connect
from Root import table_root, menu_root
from Comments import create_comment, view_comments
import hashlib

cur = Connect()

cur = cur.con.cursor()


def create_table_users():
    cur.execute("""CREATE TABLE IF NOT EXISTS USUARIO (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                        USERNAME VARCHAR(256) NOT NULL, 
                                                        PASSWORD VARCHAR(256) NOT NULL, 
                                                        TYPE_USER_ID INT NOT NULL);""")


def create_table_type_user():
    cur.execute("""CREATE TABLE IF NOT EXISTS TYPE_USER (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            NOMBRE VARCHAR2(40) NOT NULL);""")
    Connect.con.commit()


def menu_admin():
    print(f"""
    
    \t Admin menu.
    
    \t Bienvenido...
    """)

    print("""
        \t1. Ver lista de usuarios.
        \t2. Ver lista de comentarios.

        """)

    option = str(input("Ingrese una opcion: "))


def menu_usuario_normal(username):
    print(f"""

        \t User menu.

        \t Bienvenido {username}...
        """)
    # Obtener id de usuario.

    sql = f"""SELECT id FROM USUARIO WHERE username = '{username}'"""
    cur.execute(sql)

    datos = cur.fetchall()

    user_id = 0
    for user_extract_id in datos:
        user_id = user_extract_id[0]

    # Opciones

    print("""
    \t1. Hacer comentario.
    \t2. Ver mis comentarios.
    \t3. Logout.
    
    """)

    option = str(input("Ingrese una opcion: \n"))

    while option not in ["1", "2", "3"]:
        print("Has ingresado una opcion que no existe, vuelve a intentarlo")
        option = str(input("Ingrese una opcion: "))

    if option == "1":
        comment = str(input("Escribe el comentario: "))
        print("\nHas hecho un comentario correctamente\n.")
        create_comment(comment, user_id)
        menu_usuario_normal(username)

    elif option == "2":
        view_comments(user_id)

        print("\n1. Volver atras\n")
        back = str(input(": "))

        while back not in ["1"]:
            print("Ingresa una opcion correcta.\n")
            back = str(input(": "))
        if back == "1":
            menu_usuario_normal(username)
    elif option == "3":
        login_principal()


def register_new_user():
    min_pass_len = 7
    register = Register()
    print("""
    \t Tu contraseña debe tener almenos una mayuscula y 
    \t ser mayor a 7 caracteres.
    
    """)
    register.username = str(input("Ingresa tu nombre de usuario: "))
    register.password = str(input("Ingrese su contrasena: "))
    register.password_confirm = str(input("Confirme contrasena: "))

    # Validar confirmación de contraseña

    while register.password_confirm != register.password:
        print("Las contrasenas no coinciden, vuelve a ingresar las contrasenas.")
        register.password = str(input("Ingrese su contrasena nuevamente: "))
        register.password_confirm = str(input("Confirme contrasena: "))

    # Validar largo de contraseña

    while len(register.password) < min_pass_len:
        print(f"La contraseña debe tener un minimo de {min_pass_len} caracteres")
        register.password = str(input("Ingrese su contrasena nuevamente: "))
        register.password_confirm = str(input("Confirme contrasena: "))

    # Validar si existe o no algun caracter en mayuscula.

    for i in range(0, len(register.password)):
        if register.password[0].islower():
            print("ERROR! Debes tener al menos un caracterer en mayuscula")
            register.password = str(input("Ingrese su contrasena nuevamente: "))
            register.password_confirm = str(input("Confirme contrasena: "))
    register.entry_user_password()


def login_user_member():
    username = str(input("Ingrese su nombre de usuario: "))
    password_entry = str(input("Ingrese su contrasena: "))

    result = hashlib.md5(password_entry.encode())
    password_entry = result.hexdigest()

    # Obtener tabla usuario
    sql = f"SELECT * FROM USUARIO WHERE USERNAME == '{username}'"
    cur.execute(sql)

    datos = cur.fetchall()

    for i in validate_entry():
        if i[0] == username and i[1] == password_entry:
            for user in datos:
                if user[3] == 1:
                    print("Sesion iniciada")
                    menu_admin()
                else:
                    menu_usuario_normal(username)
            break

        elif i[0] != username and i[1] != password_entry:
            print("Contrasena o usuario incorrectos")
            login_principal()
            break
    return username


def login_root():
    root_username = str(input("root user: "))
    root_password = str(input("root pass: "))

    password = hashlib.md5(root_password.encode())
    root_password = password.hexdigest()
    for i in table_root():
        if i[0] == root_username and i[1] == root_password:
            print("Iniciado como usuario root.")
            menu_root()

        else:
            login_principal()


def login_principal():
    options = ["1", "2", "3"]
    print('''

    \t Menu principal...

    Por favor seleccione una opcion
    
    1. Iniciar sesion
    2. Registrarme
    
    
    
    ----------------------
    
    3. root


    ''')

    input_option = str(input(": "))

    while input_option not in options:
        print("Has ingresado una opcion incorrecta, vuelve a intentarlo.")
        input_option = str(input(": "))

    if input_option == "1":
        login_user_member()
    elif input_option == "2":
        register_new_user()
    elif input_option == "3":
        login_root()


if __name__ == '__main__':
    # cur.execute("""INSERT INTO TYPE_USER (NOMBRE) VALUES ("Admin"), ("User")""")
    # create_table_users()
    # create_table_type_user(
    login_principal()
