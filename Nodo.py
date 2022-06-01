from __future__ import annotations
from Aparato import Aparato
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Nodo import Nodo

class Nodo:
    __aparato = None
    __siguiente = None

    def __init__(self, unAparato: Aparato) -> None:
        self.__aparato = unAparato
        self.__siguiente = None
    
    
    def setSiguiente(self, siguiente: Nodo):
        self.__siguiente = siguiente
    
    
    def getSiguiente(self) -> (Nodo | None):
        return self.__siguiente
    
    
    def getAparato(self) -> Aparato:
        return self.__aparato