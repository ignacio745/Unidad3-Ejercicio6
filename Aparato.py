from abc import ABC
import abc

class Aparato(ABC):
    __marca = ""
    __modelo = ""
    __color = ""
    __paisFabricacion = ""
    __precioBase = ""

    def __init__(self, marca: str, modelo: str, color: str, paisFabricacion: str, precioBase: str) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFabricacion = paisFabricacion
        self.__precioBase = precioBase
    
    @abc.abstractmethod
    def __str__(self) -> str:
        cadena = "Marca: {0}\n".format(self.__marca)
        cadena += "Modelo: {0}\n".format(self.__modelo)
        cadena += "Color: {0}\n".format(self.__color)
        cadena += "Pais de origen: {0}\n".format(self.__paisFabricacion)
        cadena += "Precio Base: {0}\n".format(self.__precioBase)
        return cadena
    

    def getMarca(self) -> str:
        return self.__marca
    
    def getModelo(self) -> str:
        return self.__modelo
    
    def getColor(self) -> str:
        return self.__color
    
    def getPaisFabricacion(self) -> str:
        return self.__paisFabricacion
    
    def getPrecioBase(self) -> float:
        return self.__precioBase

    def getTipo(self) -> str:
        return self.__class__.__name__
    
    @abc.abstractmethod
    def getImporte(self) -> float:
        pass

    @abc.abstractmethod
    def toJSON(self) -> dict:
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                paisFabricacion = self.getPaisFabricacion(),
                precioBase = self.getPrecioBase()
            )
        )
        return d