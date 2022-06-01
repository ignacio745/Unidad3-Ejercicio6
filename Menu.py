from ColeccionAparatos import ColeccionAparatos
from Aparato import Aparato
from Heladera import Heladera
from Lavarropas import Lavarropas
from Televisor import Televisor
from IngresadorTeclado import IngresadorTeclado
from IColeccion import IColeccion
from typing import List



class Menu:
    __switcher = None
    __ingresador = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
        
    

    def opcion(self, unaColeccionAparatos: ColeccionAparatos,op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op in ('1', '2', '3'):
            func(IColeccion(unaColeccionAparatos))
        elif op in ('4', '5', '6'):
            func(unaColeccionAparatos)
        else:
            func()
    
    
    def salir(self):
        print('Usted salio del programa')
    

    def ingresarAparato(self) -> Aparato:
        unAparato = None

        tipoAparato = self.__ingresador.inputOpcion("Seleccione el tipo de aparato", ["Televisor", "Heladera", "Lavarropas"])
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        color = input("Ingrese el color: ")
        paisFabricacion = input("Ingrese el pais de fabricacion: ")
        precioBase = self.__ingresador.inputFloat("Ingrese el precio base, en caso de incluir decimales usar un punto: ", "El precio base debe ser un numero entero o decimal positivo, reintente: ")
        while precioBase < 0:
            precioBase = self.__ingresador.inputFloat("El precio base debe ser un numero entero o decimal positivo, reintente: ", "El precio base debe ser un numero entero o decimal positivo, reintente: ")
        
        if tipoAparato == "Televisor":
            tipoPantalla = self.__ingresador.inputOpcion("Ingrese el tipo de pantalla", ["crt", "vga", "svga", "plasma", "lcd", "led", "Touch Screen", "MultiTouch"])
            pulgadas = self.__ingresador.inputFloat("Ingrese las pulgadas, en caso de incluir decimales usar un punto: ")
            tipoDefinicion = self.__ingresador.inputOpcion("Ingrese el tipo de definicion", ["SD", "HD", "FULL HD"])
            conexionInternet = self.__ingresador.inputOpcion("Indique si el televisor tiene conexion a internet", ["Si", "No"])
            conexionInternet = conexionInternet == "Si"
            unAparato = Televisor(marca, modelo, color, paisFabricacion, precioBase, tipoPantalla, pulgadas, tipoDefinicion, conexionInternet)
        
        elif tipoAparato == "Heladera":
            litros = self.__ingresador.inputInt("Ingrese la capacidad en litros: ")
            freezer = self.__ingresador.inputOpcion("Indique si la heladera cuenta con freezer", ["Si", "No"])
            freezer = freezer == "Si"
            ciclica = self.__ingresador.inputOpcion("Indique si la heladera es ciclica", ["Si", "No"])
            ciclica = ciclica == "Si"
            unAparato = Heladera(marca, modelo, color, paisFabricacion, precioBase, litros, freezer, ciclica)
        
        elif tipoAparato == "Lavarropas":
            capacidad = self.__ingresador.inputInt("Ingrese la capacidad de lavado en Kgs: ")
            velCentrifugado = self.__ingresador.inputOpcion("Ingrese la velocidad de centrifugado", ["600 rpm", "1200 rpm"])
            velCentrifugado = 600 if velCentrifugado == "600 rpm" else 1200
            cantProgramas = self.__ingresador.inputInt("Ingrese la cantidad de programas: ", "El dato debe ser un entero positivo, reintente: ")
            while cantProgramas < 1:
                cantProgramas = self.__ingresador.inputInt("El dato debe ser un entero positivo, reintente: ", "El dato debe ser un entero positivom, reintente: ")
            tipoCarga = self.__ingresador.inputOpcion("Ingrese el tipo de carga", ["Frontal", "Superior"])
            unAparato = Lavarropas(marca, modelo, color, paisFabricacion, precioBase, capacidad, velCentrifugado, cantProgramas, tipoCarga)
        
        return unAparato




    def opcion1(self, unaColeccionAparatos: IColeccion):
        insertado = False
        unAparato = self.ingresarAparato()
        posicion = self.__ingresador.inputInt("Ingrese la posicion en la que desea insertar el aparato: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
        while not insertado:
            try:
                unaColeccionAparatos.insertarElemento(unAparato, posicion)
            except IndexError:
                posicion = self.__ingresador.inputInt("[ERROR] La posicion ingresada no es valida, reintente: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
            else:
                insertado = True
            print("Aparato insertado")



    def opcion2(self, unaColeccionAparatos: IColeccion):
        unAparato = self.ingresarAparato()
        unaColeccionAparatos.agregarElemento(unAparato)



    def opcion3(self, unaColeccionAparatos: IColeccion):
        posicion = self.__ingresador.inputInt("Ingrese la posicion del aparato que desea mostrar: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
        mostrado = False
        while not mostrado:
            try:
                unaColeccionAparatos.mostrarElemento(posicion)
            except IndexError:
                posicion = self.__ingresador.inputInt("[ERROR] La posicion ingresada no es valida, reintente: ", "[ERROR] La posicion ingresada no es valida, reintente: ")
            else:
                mostrado = True


    
    def opcion4(self, unaColeccionAparatos: ColeccionAparatos):
        cantHeladeras = cantLavarropas = cantTelevisores = 0
        for unAparato in unaColeccionAparatos:
            if isinstance(unAparato, Heladera) and unAparato.getMarca().lower() == "philips":
                cantHeladeras += 1
            if isinstance(unAparato, Lavarropas) and unAparato.getMarca().lower() == "philips":
                cantLavarropas += 1
            if isinstance(unAparato, Televisor) and unAparato.getMarca().lower() == "philips":
                cantTelevisores += 1
        print("La cantidad de aparatos de la marca Philips son: ")
        print("Heladeras: {0}".format(cantHeladeras))
        print("Lavarropas: {0}".format(cantLavarropas))
        print("Televisores: {0}".format(cantTelevisores))
        print("Total: {0}".format(cantHeladeras + cantLavarropas + cantTelevisores))



    def opcion5(self, unaColeccionAparatos: ColeccionAparatos):
        print("Las marcas de los lavarropas que tienen carga superior son: ")
        marcas:List[str] = []
        for unAparato in unaColeccionAparatos:
            if isinstance(unAparato, Lavarropas) and unAparato.getMarca().lower() not in [unaMarca.lower() for unaMarca in marcas] and unAparato.getTipoCarga() == "Superior":
                marcas.append(unAparato.getMarca())
        marcas.sort()
        for unaMarca in marcas:
            print(unaMarca)



    def opcion6(self, unaColeccionAparatos: ColeccionAparatos):
        print("{0:<15}{1:<15}{2:<20}{3:>20}".format("Aparato", "Marca", "Pais de fabricacion", "Importe de venta"))
        for unAparato in unaColeccionAparatos:
            print("{0:<15}{1:<15}{2:<20}{3:20.2f}".format(unAparato.getTipo(), unAparato.getMarca(), unAparato.getPaisFabricacion(), unAparato.getImporte()))



    def ejecutarMenu(self, unaColeccionAparatos: ColeccionAparatos):
            opcion = "0"
            while opcion != "7":
                print("Ingrese la opcion deseada")
                print("[1] Insertar un aparato en una posicion determinada")
                print("[2] Agregar un aparato a la coleccion")
                print("[3] Mostrar un objeto dada una posicion de la lista")
                print("[4] Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea Philips")
                print("[5] Mostrar la marca de todos los lavarropas que tienen carga superior")
                print("[6] Mostrar marca, pais de fabricacion e importe de venta de todos los aparatos a la venta")
                print("[7] Guardar y salir")
                opcion = input("--> ")  
                self.opcion(unaColeccionAparatos, opcion)