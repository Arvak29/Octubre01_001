import os

def Temperaturas:
    print("--- opción de temperaturas")
    veces=int(input("Cuantas temperaturas ingresa?"))
    for x in range veces:
        tempe=float(input("Ingrese temperaturas: "))
        suma=suma+tempe
    print("El promedio de las temperaturas es: ", round((suma/veces),2))
    tecla=input("Presione una tecla para continuar")

def Personas():
    print ("--- Opción de Datos de Personas ---")
    #ingresar para n personas el nombre y la edad. n debe ser ingresado por teclado
    #mostrar: cuantas personas son mayores de edad y cuantas son menores de edad.

seguir=True
while seguir:
    os.system('cls')
    print ("1. Temperaturas")
    print ("2. Datos de Personas")
    print ("3. Salir ")
    op=int(input("Ingrese opción 1,2,3: "))
    if(op==1):
        Temperaturas()      #invocamos a una función
    if(op==2):
        Personas()          #invocamos a una función
    if(op==3):
        print("Programa Finalizado")
        break