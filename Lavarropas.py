from Aparato import Aparato

class Lavarropas(Aparato):
    __capacidad = 0
    __velCentrifugado = 0
    __cantProgramas = 0
    __tipoCarga = ""

    def __init__(self, marca: str, modelo: str, color: str, paisFabricacion: str, precioBase: str, capacidad: int, velCentrifugado: int, cantProgramas: int, tipoCarga: str) -> None:
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__capacidad = capacidad
        self.__velCentrifugado = velCentrifugado
        self.__cantProgramas = cantProgramas
        self.__tipoCarga = tipoCarga
    
    def getCapacidad(self) -> int:
        return self.__capacidad
    
    def getVelocidadCentrifugado(self) -> int:
        return self.__velCentrifugado

    def getCantProgramas(self) -> int:
        return self.__cantProgramas
    
    def getTipoCarga(self) -> str:
        return self.__tipoCarga
    

    def __str__(self) -> str:
        cadena = "Tipo de aparato: Lavarropas\n"
        cadena += super().__str__()
        cadena += "Capacidad: {0} Kg\n".format(self.__capacidad)
        cadena += "Velocidad de centrifugado: {0} rpm\n".format(self.__velCentrifugado)
        cadena += "Cantidad de programas: {0}\n".format(self.__cantProgramas)
        cadena += "Tipo de carga: {0}".format(self.__tipoCarga)
        return cadena
    

    def getImporte(self) -> float:
        importe = self.getPrecioBase()
        if self.__capacidad <= 5:
            importe += self.getPrecioBase() * 0.01
        else:
            importe += self.getPrecioBase() * 0.03
        return importe

    

    def toJSON(self) -> dict:
        d = super().toJSON()
        d["__atributos__"]["capacidad"] = self.__capacidad
        d["__atributos__"]["velCentrifugado"] = self.__velCentrifugado
        d["__atributos__"]["cantProgramas"] = self.__cantProgramas
        d["__atributos__"]["tipoCarga"] = self.__tipoCarga
        return d