from Aparato import Aparato

class Televisor(Aparato):
    __tipoPantalla = ""
    __pulgadas = 0
    __tipoDefinicion = ""
    __conexionInternet = False

    def __init__(self, marca: str, modelo: str, color: str, paisFabricacion: str, precioBase: str, tipoPantalla: str, pulgadas: float, tipoDefinicion: str, conexionInternet: bool) -> None:
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = tipoDefinicion
        self.__conexionInternet = conexionInternet
    

    def getTipoPantalla(self):
        return self.__tipoPantalla
    
    def getPulgadas(self):
        return self.__pulgadas
    
    def getTipoDefinicion(self):
        return self.__tipoDefinicion
    
    def getConexionInternet(self):
        return self.__conexionInternet
    
    
    def __str__(self):
        cadena = "Tipo de aparato: Televisor\n"
        cadena += super().__str__()
        cadena += "Tipo de pantalla: {0}\n".format(self.__tipoPantalla)
        cadena += "Pulgadas: {0}\n".format(self.__pulgadas)
        cadena += "Tipo de definicion: {0}\n".format(self.__tipoDefinicion)
        cadena += "Conexion a internet: {0}".format(["No", "Si"][self.__conexionInternet])
        return cadena
    

    def getImporte(self) -> float:
        importe = self.getPrecioBase()
        if self.getTipoDefinicion() == "SD":
            importe += self.getPrecioBase() * 0.01
        elif self.getTipoDefinicion() == "HD":
            importe += self.getPrecioBase() * 0.02
        elif self.getTipoDefinicion() == "FULL HD":
            importe += self.getPrecioBase() * 0.03
        if self.getConexionInternet():
            importe += self.getPrecioBase() * 0.1
        return importe
    

    def toJSON(self) -> dict:
        d = super().toJSON()
        d["__atributos__"]["tipoPantalla"] = self.__tipoPantalla
        d["__atributos__"]["pulgadas"] = self.__pulgadas
        d["__atributos__"]["tipoDefinicion"] = self.__tipoDefinicion
        d["__atributos__"]["conexionInternet"] = self.__conexionInternet
        return d