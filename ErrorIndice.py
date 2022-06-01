class ErrorIndice(IndexError):
    __mensaje = ""

    def __init__(self, *args: object) -> None:
        """
        Excepcion para indices fuera de rango en la interfaz IColeccion
        """
        
        super().__init__(*args)