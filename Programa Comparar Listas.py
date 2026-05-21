def llenar_lista_uno(lista1):
    print("--- LISTA 1 ---")
    i = 1
    while i <= 10:
        try:
            num = float(input("Digite el numero: "))
            lista1.append(num)
            i = i + 1
        except:
            print("Invalido, solo acepta numeros.")

def llenar_lista_dos(lista2):
    print("\n--- LISTA 2 ---")
    i = 1
    while i <= 10:
        try:
            num = float(input("Digite el numero: "))
            lista2.append(num)
            i = i + 1
        except:
            print("Invalido, solo acepta numeros.")

def comparar(lista1, lista2):
    mayores1 = []
    mayores2 = []
    cont1 = 0
    cont2 = 0
    
    for i in range(10):
        if lista1[i] > lista2[i]:
            mayores1.append(lista1[i])
            cont1 = cont1 + 1
        elif lista2[i] > lista1[i]:
            mayores2.append(lista2[i])
            cont2 = cont2 + 1
            
    return cont1, mayores1, cont2, mayores2

def mostrar(lista1, lista2, cont1, mayores1, cont2, mayores2):
    print("")
    print("==============================")
    print("      REPORTES FINALES")
    print("==============================")
    
    print("Lista 1 Original:", lista1)
    print("Lista 2 Original:", lista2)
    
    print("------------------------------")
    print("Cantidad mayores en Lista 1:", cont1)
    print("Los numeros son:", mayores1)
    
    print("------------------------------")
    print("Cantidad mayores en Lista 2:", cont2)
    print("Los numeros son:", mayores2)
    print("==============================")

# flujo principal
lista1 = []
lista2 = []

llenar_lista_uno(lista1)
llenar_lista_dos(lista2)

cont1, mayores1, cont2, mayores2 = comparar(lista1, lista2)

mostrar(lista1, lista2, cont1, mayores1, cont2, mayores2)