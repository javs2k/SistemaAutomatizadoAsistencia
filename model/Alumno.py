import bd

class Alumno():
    def __init__(self, codigo, nombre = None, fecha_nacimiento = None, ciclo = None, especialidad = None):
        self.codigo = codigo
        self.nombre = nombre 
        self.fecha_nacimiento = fecha_nacimiento
        self.ciclo = ciclo
        self.especialidad = especialidad

    def cargarDatos(self):
        result = bd.getDatosAlumno(self.codigo)
        self.nombre = result.nombre
        self.fecha_nacimiento = result.fec_nacimiento
        self.ciclo = result.ciclo
        self.especialidad = result.especialidad

    def registrarAsistencia(self, cod_h_c):
        bd.registraAsistencia(self.codigo, cod_h_c)
