import bd

class Docente():
    def __init__(self, codigo, nombre = None, secciones = []):
        self.codigo = codigo
        self.nombre = nombre 
        self.secciones = secciones

    def cargarDatos(self):
        self.nombre = bd.getNombreDocente(self.codigo)
        self.secciones = bd.getSeccionesDocente(self.codigo)

    def claseActual(self):
        return bd.getClaseActualDocente(self.codigo)