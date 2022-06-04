from Aparato import Aparato
from Heladera import Heladera
from Lavarropas import Lavarropas
from Televisor import Televisor
from IColeccion import IColeccion
from Nodo import Nodo
from zope.interface import implementer


@implementer(IColeccion)
class ColeccionAparatos:
    __comienzo = None
    __actual = None
    __tope = 0

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = self.__comienzo
        self.__tope = 0

    
    def agregarElemento(self, elemento: Aparato):
        """
        Agrega un aparato al final de la coleccion
        """

        unNodo = Nodo(elemento)
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unNodo)
        self.__tope += 1
    

    def insertarElemento(self, elemento: Aparato, pos: int):
        """
        Inserta un aparato en la posicion indicada, 
        desplazando los aparatos siguientes una posicion a la derecha
        """
        
        insertado = False
        unNodo = Nodo(elemento)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
            insertado = True
        else:
            if self.__comienzo != None:
                i = 1
                aux = self.__comienzo
                while aux.getSiguiente() != None and i < pos:
                    aux = aux.getSiguiente()
                    i += 1
                if i == pos:
                    unNodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(unNodo)
                    insertado = True
                else:
                    raise IndexError("Indice fuera de rango")
        self.__tope += 1
        return insertado
    
    
    def mostrarElemento(self, pos: int) -> None:
        unNodo = None
        if pos == 0:
            if self.__comienzo == None:
                raise(IndexError("Indice fuera de rango"))
            unNodo = self.__comienzo
        else:
            i = 1
            if self.__comienzo == None:
                raise(IndexError("Indice fuera de rango"))
            unNodo = self.__comienzo.getSiguiente()
            while i < pos and unNodo.getSiguiente() != None:
                i += 1
                unNodo = unNodo.getSiguiente()
            if i < pos:
                raise(IndexError("Indice fuera de rango"))
        unAparato = unNodo.getAparato()
        print(unAparato)
    

    def __iter__(self):
        return self
    

    def __next__(self) -> Aparato:
        if self.__actual == None:
            self.__actual = self.__comienzo
            raise StopIteration
        else:
            unAparato = self.__actual.getAparato()
            self.__actual = self.__actual.getSiguiente()
            return unAparato


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[unAparato.toJSON() for unAparato in self]
        )
        return d