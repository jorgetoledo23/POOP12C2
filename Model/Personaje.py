#Class => Clase
#Molde para crear Objetos
#Todos los Objetos creados a partir de ese Model(Class)
#Tendran una misma Estructura
#El mismo Esqueleto

#import Item

class Personaje: #Nombre Molde
    #Atributos => Propiedades => Campos
    Inventario = []

    #Constructor
    def __init__(self, nombre:str, fuerza:int, vida:int):
        self.Nombre = nombre.title()
        self.Vida = vida
        if fuerza >= 0:
            self.Fuerza = fuerza # -100
        else:
            raise TypeError("La fuerza debe ser Mayor a 0")
        self.Oro = 500

    def GetStats(self):
        return f"Nombre: {self.Nombre}, Vida: {self.Vida}, Fuerza: {self.Fuerza}, Oro: {self.Oro}"

    def Atacar(self, objetivo):
        damage = int(self.Fuerza / 10 + 15)
        objetivo.Vida -= damage
    
    def Comprar(self, ItemComprado):
        self.Oro -= ItemComprado.Coste
        self.Vida += ItemComprado.Vida
        self.Fuerza += ItemComprado.Fuerza
        self.Inventario.append(ItemComprado)        


# #Objetos (Instancia de Personaje)
# P1 = Personaje(fuerza=100, vida=1000, nombre="Lee Sin")

# P2 = Personaje("Janna", 10, 500)

# #Generar el Personaje Garen, 2000 de Vida, 50 Fuerza, 1000 de Oro
# P3 = Personaje("gARen", 50, 2000)


# P1.Comprar(Item.ListadoItems[0])
# P3.Comprar(Item.ListadoItems[1])
# P1.Atacar(P3)
# P3.Atacar(P2)



# print(P1.GetStats())
# print(P2.GetStats())
# print(P3.GetStats())

















