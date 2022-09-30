from Model.Personaje import Personaje
from Model.Item import Item, ListadoItems

Player1 = Personaje(nombre="Player 1", fuerza=100, vida=100)
Player2 = Personaje(nombre="Player 2", fuerza=100, vida=100)

JugadorTurno = Player1
JugadorEspera = Player2
Turno = 1
ContadorTurnos = 1

while 10>5:

    import os
    os.system("cls")

    print(f"Cantidad de Turnos Jugados: {ContadorTurnos}")
    print(f"Turno: {Turno}\n")

    print(f"Stats Player 1: {Player1.GetStats()}\n")
    print(f"Stats Player 2: {Player2.GetStats()}\n")

    print("[1] - Atacar")
    print("[2] - Comprar")

    opcion = input("\nSelecciona tu Jugada: ")
    
    if opcion == "1":
        JugadorTurno.Atacar(JugadorEspera)
        input("Ataque Exitoso!")

    if opcion == "2":
        os.system("cls")
        id = 1
        for item in ListadoItems:
            print(f"[{id}] - {item.GetStats()}")
            id += 1
        seleccion = int(input("\nSelecciona el Item a Comprar: "))

        JugadorTurno.Comprar(ListadoItems[seleccion - 1])
        input("Compra Exitosa!")

    
    if Turno == 1: 
        Turno = 2 
        JugadorTurno = Player2
        JugadorEspera = Player1
    else: 
        Turno = 1
        JugadorTurno = Player1
        JugadorEspera = Player2

    ContadorTurnos += 1
    input("Turno Finalizado. Presiona Enter para Continuar...")