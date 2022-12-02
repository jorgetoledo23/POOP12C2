#Ejecutable
from Model.MysqlConnect import DAO
import os
from datetime import datetime
from Model.DetalleVenta import DetalleVenta

dao = DAO()
os.system("cls")
#Generar Menu

while True:
    os.system("cls")
    print("[1] - Vender")
    print("[2] - Ver Historial de Ventas")

    opcion = input("\nSeleccion la opcion: ")

    if(opcion == "1"):
        #Vender
        os.system("cls")
        carroCompra = []
        Total = 0

        #Mostrar Listado de Clientes
        for c in dao.LeerClientes():
            print(c.getInfo())

        #12312312312
        existe = True
        while existe:   
            rutCliente = input("\nIngresa Rut del Cliente: ")
            for c in dao.LeerClientes():
                if(rutCliente == c.getRut()):
                    #Rut Valido
                    existe = False
                    cliente = c
            if(existe):
                print("Rut Invalido!")
        
        os.system("cls")
        agregando = True
        while agregando:
            print(f"Venta para cliente: {cliente.getInfo()}")
            print(f"Fecha: {datetime.now()}\n")
            print(f"Total: $$ { Total }")

            #Mostrar Listado de Clientes
            for c in dao.LeerProductos():
                print(c.getInfo())

            existe = True
            while existe:
                producto = int(input("\nIngrese Codigo de Producto a Vender: "))
                for c in dao.LeerProductos():
                    if(producto == c.getCodigo()):
                        existe = False
                        productoAgregado = c
                if existe:
                    print("Codigo Invalido!")

            
            stock = True
            while stock:
                cantidad = int(input("\nIngrese Cantidad: "))
                if(cantidad > productoAgregado.getStock()):
                    print("Stock Insuficiente! Ingresa Otra Cantidad.")
                else:
                    stock = False
            
            dv = DetalleVenta(1,1, productoAgregado, cantidad, cantidad * productoAgregado.getPrecio())
            carroCompra.append(dv)
            Total += cantidad * productoAgregado.getPrecio()
            respuesta = input("\nProducto Agregado a la Venta! ¿Deseas agregar mas Productos? (S/N): ")
            
            if(respuesta != "S" and respuesta!="s"):
                agregando = False


        os.system("cls")
        print(f"Venta para cliente: {cliente.getInfo()}")
        print(f"Fecha: {datetime.now()}\n")

        print("\nProductos de la Venta")

        for dv in carroCompra:
            print(dv.getShortInfo())


        print(f"\nTotal: $$ { Total }")

        input("Presiona Enter para Finalizar la Venta!")
        dao.InsertarVenta(rutCliente, Total, datetime.now().date(), carroCompra)
        input("Venta generada Existosamente!")
            





