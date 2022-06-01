from ObjectEncoder import ObjectEncoder
from Menu import Menu


if __name__ == "__main__":
    unObjectEncoder = ObjectEncoder()
    unMenu = Menu()
    d = unObjectEncoder.leerJSONArchivo("aparatoselectronicos.json")
    unaColeccionAparatos = unObjectEncoder.decodificarDiccionario(d)
    unMenu.ejecutarMenu(unaColeccionAparatos)
    d = unaColeccionAparatos.toJSON()
    unObjectEncoder.guardarJSONArchivo(d, "aparatoselectronicos.json")