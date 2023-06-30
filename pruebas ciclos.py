# def usuario():
#     numeromin=int(input('escriba numero: '))
#     numeromax:int(input('escriba numero: '))
#     for i in range(numeromin,20):
#         print(i)
# usuario()
def solicitar_inicio():
    while True:
        try:
            inicio = int(input("Ingrese el valor de inicio: "))
            return inicio
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")

def solicitar_final(inicio):
    while True:
        try:
            final = int(input("Ingrese el valor de final: "))
            if final > inicio:
                return final
            else:
                print("¡Error! El valor final debe ser mayor que el valor de inicio.")
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")

inicio = solicitar_inicio()
final = solicitar_final(inicio)

for i in range(inicio, final+1):
    print(i)

       


