entradas= []
edades= []
nombres= []
contador_clientes= 0
contador_estudiantes= 0
contador_adultos_mayores= 0
total_recaudado= 0

def validar_cantidad():
    cantidad_reservas= int(input("Digite la cantidad de reservas: "))
    while cantidad_reservas < 4 or cantidad_reservas > 10:
        cantidad_reservas= int(input("Rango no valido, digite la cantidad de reservas: "))
    return cantidad_reservas

def validar_edad():
    edad_cliente= int(input("Ingrese la edad del cliente: "))
    while edad_cliente < 3 or edad_cliente > 100:
        edad_cliente= int(input("Edad no valida, ingrese la edad nuevamente: "))
    return edad_cliente

def validar_dia():
    dia_funcion= input("Que dia desean reservar: ")
    while dia_funcion != "Lunes" and dia_funcion != "Miercoles" and dia_funcion != "Viernes" and dia_funcion != "Sabado":
        dia_funcion= input("Dia no habil, ingrese el dia correcto: ")
    return dia_funcion

def validar_tipo():
    tipo_entrada= int(input("Digite que tipo de entrada requiere el cliente: "))
    while tipo_entrada < 1 or tipo_entrada > 3:
        tipo_entrada= int(input("Tipo de entrada no existente, digite el tipo correcto "))
    return tipo_entrada

def calcular_precio(tipo_entrada, dia_funcion):
    if tipo_entrada== 1:
        precio= 3000
    elif tipo_entrada == 2:
        precio= 2000
    else:
        precio= 1500
    
    if dia_funcion == "Viernes" or dia_funcion == "Sabado":
        precio= precio + (precio*0.10)
    
    return precio

nombre_pelicula= input("Ingrese el nombre de la pelicula: ")

cantidad_reservas= validar_cantidad()

while contador_clientes < cantidad_reservas:
    nombre_cliente = input("Ingrese el nombre completo del cliente: ")
    nombres.append(nombre_cliente)

    edad_cliente = validar_edad()
    edades.append(edad_cliente)

    dia_funcion = validar_dia()

    tipo_entrada = validar_tipo()
    if tipo_entrada == 2:
        contador_estudiantes= contador_clientes + 1
    if tipo_entrada == 3:
        contador_adultos_mayores= contador_adultos_mayores + 1
    
    precio= calcular_precio(tipo_entrada, dia_funcion)

    total_recaudado = total_recaudado + precio
    entradas.append(precio)

    contador_clientes = contador_clientes + 1 

print("La pelicula es: " , nombre_pelicula)

contador_mostrar= 0
while contador_mostrar < cantidad_reservas:
    print("Nombre: " , nombres[contador_mostrar], "Edad: " , edades[contador_mostrar], "Precio entrada: " , entradas[contador_mostrar])
    contador_mostrar= contador_mostrar + 1

suma= 0
contador_mostrar= 0
while contador_mostrar < cantidad_reservas:
    suma= suma + edades[contador_mostrar]
    contador_mostrar= contador_mostrar + 1

promedio= suma / cantidad_reservas

print("Total recaudado: ", total_recaudado)
print("Promedio edades: ", promedio)
print("Adultos mayores: ", contador_adultos_mayores)

porcentaje= (contador_estudiantes * 100) / cantidad_reservas

if porcentaje > 60:
    print("¡Gran apoyo del público joven!")
