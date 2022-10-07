from Model.Item import Item


class Personaje: #Nombre Molde

    def __init__(self, nombre:str, fuerza:int, vida:int):
        self.__Nombre = nombre.title()
        self.__Vida = vida
        if fuerza >= 0:
            self.__Fuerza = fuerza # -100
        else:
            raise TypeError("La fuerza debe ser Mayor a 0")
        self.__Oro = 1000
        self.__Inventario = []

    def obtenerOro(self):
        return self.__Oro / 2

    def setearOro(self, NuevaCantidadOro):
        if NuevaCantidadOro > 0:
            self.__Oro = NuevaCantidadOro
        else: 
            raise TypeError("Oro No Valido")

    def GetStats(self):
        return f"Nombre: {self.__Nombre}\nVida: {self.__Vida}\nFuerza: {self.__Fuerza}\nOro: {self.__Oro}"

    def Atacar(self, objetivo):
        damage = int(self.__Fuerza / 10 + 15)
        objetivo.__Vida -= damage
    
    def Comprar(self, ItemComprado:Item):
        self.__Oro -= ItemComprado.GetCoste()
        self.__Vida += ItemComprado.GetVida()
        self.__Fuerza += ItemComprado.GetFuerza()
        self.__Inventario.append(ItemComprado)

    def GetVida(self):
        return self.__Vida #100 50 0 -10


    def GetInvetario(self):
        return self.__Inventario
