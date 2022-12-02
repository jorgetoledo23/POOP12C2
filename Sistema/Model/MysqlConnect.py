import mysql.connector
from mysql.connector import errorcode

from Model.Cliente import Cliente
from Model.Producto import Producto

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='root',
                host='localhost',
                database='VentasPython')
            print("Coneccion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)

    def LeerClientes(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM Clientes")
        cursor.execute(consulta)

        listaClientes = []
        for (a,b,c,d) in cursor:
            c = Cliente(a, b, c, d)
            listaClientes.append(c)
        
        return listaClientes

    def LeerProductos(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM Productos")
        cursor.execute(consulta)

        listaProductos = []
        for (a,b,c,d) in cursor:
            c = Producto(a, b, c, d)
            listaProductos.append(c)
        
        return listaProductos

    def InsertarVenta(self, rutCliente, total, fecha, detalle):
        try:
            cursor = self.cnx.cursor()
            add_venta = ("INSERT INTO Ventas (fecha, rutcliente, totalventa) VALUES (%s,%s,%s)")
            data_venta = (fecha, rutCliente, total)
            cursor.execute(add_venta, data_venta)

            ventaid = cursor.lastrowid
            for dv in detalle:
                add_detalle = ("INSERT INTO detalleventa (ventaid, productoid, cantidad, subtotal) VALUES (%s,%s,%s,%s)")
                data_detalle = (ventaid, dv.getProducto().getCodigo(), dv.getCantidad(), dv.getSubtotal())
                cursor.execute(add_detalle, data_detalle)
                #Descontar Stock del Producto Vendido (UPDATE)

            
            self.cnx.commit()
        except:
            print("Ocurrio un Error!")
            self.cnx.rollback()