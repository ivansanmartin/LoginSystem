from RegisterAccount import Register
from LoginAccount import UserLogin
from SQLConnect import Connect
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
    
    \t Has ingresado sesion como administrador.
    
    \t Bienvenido...
    
    
    """)

    print("""

        \t1. Ver lista de usuarios.
        \t2. Ver lista de comentarios.

        """)

    option = str(input("Ingrese una opcion: "))


def menu_usuario_normal():
    print(f"""

        \t Has ingresado sesion como usuario.

        \t Bienvenido...


        """)

    # Opciones

    print("""
    
    \t1. Ver mis comentarios.
    \t2. Hacer comentario.
    
    """)

    option = str(input("Ingrese una opcion: "))


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
    login = UserLogin()
    login.username = str(input('Nombre de usuario: '))
    login.password_entry = str(input("Contrasena: "))

    login.validate_entry()


def login_principal():
    options = ["1", "2"]
    print('''

    \t Iniciando programa...

    Por favor seleccione una opcion
    
    1. Iniciar sesion
    2. Registrarme


    ''')

    input_option = str(input(": "))

    while input_option not in options:
        print("Has ingresado una opcion incorrecta, vuelve a intentarlo.")
        input_option = str(input(": "))

    if input_option == "1":
        login_user_member()
    elif input_option == "2":
        register_new_user()


if __name__ == '__main__':
    # cur.execute("""INSERT INTO TYPE_USER (NOMBRE) VALUES ("Admin"), ("User")""")
    # create_table_users()
    # create_table_type_user()
    login_principal()