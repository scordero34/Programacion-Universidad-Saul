print("BIENVENIDO AL AYUDADOR DE TAREAS NUMERO #1 DEL MUNDO")

contador_tareas = 0
tareas_completas = 0

vector_tarea = []
vector_categoria = []

# ---------------- LOGIN ----------------
def login():
    contador_intentos = 0

    usuario1 = "admin"
    contra1 = 123
    usuario2 = "usuario2"
    contra2 = 456
    usuario3 = "usuario3"
    contra3 = 789

    while contador_intentos < 3:
        nombre_usuario = input("Digite el usuario: ")
        contrasena = int(input("Ingrese la contrasena: "))

        if ((nombre_usuario == usuario1 and contrasena == contra1) or (nombre_usuario == usuario2 and contrasena == contra2) or (nombre_usuario == usuario3 and contrasena == contra3)):
            print("Login exitoso")
            return True
        else:
            print("Login fallido")
            contador_intentos += 1

    print("Se alcanzaron los 3 intentos máximos. Programa finalizado.")
    return False


if not login():
    exit()


# ---------------- MODULOS ----------------

def estudio():
    contador_estudio = 1
    cantidad_tareas = int(input("Ingrese la cantidad de tareas a agregar: "))

    while contador_estudio <= cantidad_tareas:
        nombre_tarea = input("Ingrese la tarea: ")
        vector_tarea.append(nombre_tarea)
        vector_categoria.append("Estudio")
        contador_estudio += 1

    return cantidad_tareas


def trabajo():
    contador_trabajo = 1
    cantidad_tareas = int(input("Ingrese la cantidad de tareas a agregar: "))

    while contador_trabajo <= cantidad_tareas:
        nombre_tarea = input("Ingrese la tarea: ")
        vector_tarea.append(nombre_tarea)
        vector_categoria.append("Trabajo")
        contador_trabajo += 1

    return cantidad_tareas


def personal():
    contador_personal = 1
    cantidad_tareas = int(input("Ingrese la cantidad de tareas a agregar: "))

    while contador_personal <= cantidad_tareas:
        nombre_tarea = input("Ingresa el nombre de tu tarea: ")
        vector_tarea.append(nombre_tarea)
        vector_categoria.append("Personal")
        contador_personal += 1

    return cantidad_tareas


def registro_tareas():
    categoria = input("La tarea es de categoría Estudio, Trabajo o Personal? ")

    while categoria != "Estudio" and categoria != "Trabajo" and categoria != "Personal":
        categoria = input("Digite una categoria valida: ")

    if categoria == "Estudio":
        return estudio()
    elif categoria == "Trabajo":
        return trabajo()
    else:
        return personal()


def ver_tareas():
    contador_mostrar = 0

    if contador_tareas == 0:
        print("No hay tareas registradas")
        return 0

    while contador_mostrar < contador_tareas:
        print("Tarea:", vector_tarea[contador_mostrar])
        print("Categoria:", vector_categoria[contador_mostrar])
        print("----------------------")
        contador_mostrar += 1

    completas = int(input("¿Cuantás tareas ya completaste?: "))
    return completas


def informes():
    if contador_tareas == 0:
        print("No hay tareas agregadas")
        return

    porcentaje = (tareas_completas / contador_tareas) * 100
    print("El porcentaje de tareas completadas es de:", porcentaje, "%")

    contador_estudio = 0
    contador_trabajo = 0
    contador_personal = 0
    contador_mostrar = 0

    while contador_mostrar < contador_tareas:
        if vector_categoria[contador_mostrar] == "Estudio":
            contador_estudio += 1
        elif vector_categoria[contador_mostrar] == "Trabajo":
            contador_trabajo += 1
        else:
            contador_personal += 1

        contador_mostrar += 1

    if contador_estudio > contador_trabajo and contador_estudio > contador_personal:
        print("La categoria con más tareas es Estudio con: ", contador_estudio, "tareas")
    elif contador_trabajo > contador_estudio and contador_trabajo > contador_personal:
        print("La categoria con más tareas es la de Trabajo con: ", contador_trabajo, "tareas")
    else:
        print("La categoria con más tareas es Personal con: ", contador_personal, "tareas")


# ---------------- MENU ----------------

while True:
    print("------------1 Registrar tareas------------")
    print("------------2 Ver tareas------------")
    print("------------3 Ver informes------------")
    print("------------4 Salir------------")

    respuesta = int(input("Digite la acción que desea realizar: "))

    if respuesta == 4:
        print("Saliendo del programa... Gracias por preferirnos ;) ")
        break
    elif respuesta == 1:
        contador_tareas += registro_tareas()
    elif respuesta == 2:
        tareas_completas += ver_tareas()
    elif respuesta == 3:
        informes()

    else:
        print("Opción invalida, ingrese de nuevo la acción que desea hacer: ")
