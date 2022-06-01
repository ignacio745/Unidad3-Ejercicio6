from Aparato import Aparato

class Heladera(Aparato):
    __litros = 0
    __freezer = False
    __ciclica = False

    def __init__(self, marca: str, modelo: str, color: str, paisFabricacion: str, precioBase: str, litros: int, freezer: bool, ciclica: bool) -> None:
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__litros = litros
        self.__freezer = freezer
        self.__ciclica = ciclica
    

    def __str__(self) -> str:
        cadena = "Tipo de aparato: Heladera\n"
        cadena += super().__str__()
        cadena += "Capacidad: {0} litros\n".format(self.__litros)
        cadena += "Freezer: {0}\n".format(["No", "Si"][self.__freezer])
        cadena += "Ciclica: {0}".format(["No", "Si"][self.__ciclica])
        return cadena
    

    def getImporte(self) -> float:
        importe = self.getPrecioBase()
        if self.__freezer:
            importe += self.getPrecioBase() * 0.05
        else:
            importe += self.getPrecioBase() * 0.01
        if self.__ciclica:
            importe += self.getPrecioBase() * 0.1
        return importe
    

    def toJSON(self) -> dict:
        d = super().toJSON()
        d["__atributos__"]["litros"] = self.__litros
        d["__atributos__"]["freezer"] = self.__freezer
        d["__atributos__"]["ciclica"] = self.__ciclica
        return d