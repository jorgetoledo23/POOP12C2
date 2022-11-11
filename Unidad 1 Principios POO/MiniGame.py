from Model.Personaje import Personaje
from Model.Item import Item, ListadoItems

Player1 = Personaje(nombre="Player 1", fuerza=100, vida=100)
Player2 = Personaje(nombre="Player 2", fuerza=100, vida=100)

JugadorTurno = Player1
JugadorEspera = Player2
Turno = 1
ContadorTurnos = 1


Ganador = None

while True:

    TurnoExitoso = True
    import os
    os.system("cls")

    print(f"Cantidad de Turnos Jugados: {ContadorTurnos}")
    print(f"Turno: {Turno}\n")

    print(f"\nStats Player 1: {Player1.GetStats()}")
    print("Inventario:")
    for item in Player1.GetInvetario():
        print(item.GetNombre())


    print(f"\nStats Player 2: {Player2.GetStats()}")
    print("Inventario: ")
    for item in Player2.GetInvetario():
        print(item.GetNombre())

    print("\n[1] - Atacar")
    print("[2] - Comprar")

    opcion = input("\nSelecciona tu Jugada: ")
    
    if opcion == "1":
        JugadorTurno.Atacar(JugadorEspera)
        input("Ataque Exitoso!")
        if JugadorEspera.GetVida() <= 0:
            Ganador = JugadorTurno

    if opcion == "2":

        if len(JugadorTurno.GetInvetario()) >=6:
            print("No Puedes Comprar mas Items!")
            TurnoExitoso = False
        else:
            os.system("cls")
            id = 1
            for item in ListadoItems:
                print(f"[{id}] - {item.GetStats()}")
                id += 1
            seleccion = int(input("\nSelecciona el Item a Comprar: "))

            while (seleccion <= 0 or seleccion > len(ListadoItems)):
                print("Seleccion Invalida!")
                seleccion = int(input("\nSelecciona el Item a Comprar: "))

            JugadorTurno.Comprar(ListadoItems[seleccion - 1])
            input("Compra Exitosa!")

    if opcion == "3":
        os.system("cls")
        id = 1
        for item in JugadorTurno.GetInvetario():
            print(f"[{id}] - {item.GetStats()}")
            id += 1
        seleccion = int(input("\nSelecciona el Item a Vender: "))

        while (seleccion <= 0 or seleccion > len(JugadorTurno.GetInvetario())):
            print("Seleccion Invalida!")
            seleccion = int(input("\nSelecciona el Item a Vender: "))

        JugadorTurno.Vender(JugadorTurno.GetInvetario()[seleccion - 1])
        input("Venta Exitosa!")

    if opcion == "4":
        ff = input("Estas Seguro de Rendirte? (S/N): ")
        if ff=="S":
            Ganador = JugadorEspera
        else:
            TurnoExitoso = False


    if Ganador != None:
        break
    if TurnoExitoso:
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


os.system("cls")
print("Juego Terminado!!!")
print(f"El Ganador es: {Ganador.GetStats()}")
