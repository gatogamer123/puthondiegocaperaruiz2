
def obtener_mayor():
    n = int(input("Ingrese la cantidad de datos que desea comparar: "))
    mayor = None
    con = 0
    while con < n:
        dato = int(input(f"Ingrese el dato {con + 1}: "))  
        if mayor is None or dato > mayor:
            mayor = dato
        con += 1
    return mayor
resultado = obtener_mayor()
print("El mayor valor ingresado es:", resultado)
