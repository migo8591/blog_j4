users = []
email = input("Ingrese su email: ")
users.append(email)
print(users)
print("Email guardado")
print("""
:::::::::::::::
:::::::::::::::
:::::::::::::::""")
i = True
while i:
    option = int(input("¿Quieres iniciar session? Yes:1 No:2  "))
    
    if option == 1:
        email2 = input("Ingrese su email: ")
        def get_user(email2):
            for user in users: 
                if user == email2:
                    i = False
                    print("Session iniciada")

                else:
                    print("Correo no registrado o digitado erroneamente.")
                    i = True
            return i
        get_user(email2)
    elif option == 2:
        i = False


# Un callback en programación es una función que se pasa como argumento a otra función y se ejecuta después de que se completa una operación. Los callbacks son muy útiles para manejar tareas asíncronas, como operaciones de entrada/salida o temporizadores.

# Aquí tienes un ejemplo sencillo en Python:
def saludo(nombre):
    print(f"Hola, {nombre}!")

def ejecutar_callback(callback, nombre):
    callback(nombre)

# Usamos la función 'saludo' como callback
ejecutar_callback(saludo, "Carlos")

# En este ejemplo, la función saludo se pasa como un callback a la función ejecutar_callback. Cuando ejecutar_callback se ejecuta, llama a saludo con el argumento nombre.

# ¿Te gustaría saber más sobre cómo se usan los callbacks en otros contextos?