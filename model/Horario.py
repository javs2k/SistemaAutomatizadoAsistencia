import bd

class Horario():
    def __init__(self, codigo, dia = None, hora_inicio = None, hora_final = None,
                 tipo = None, cod_docente = None, cod_clase = None, cod_aula = None):
        self.codigo = codigo
        self.dia = dia 
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.tipo = tipo
        self.cod_docente = cod_docente
        self.cod_clase = cod_clase
        self.cod_aula = cod_aula

    def cargarDatos(self):
        result = bd.getDatosHorario(self.codigo)
        self.dia = result.dia
        self.hora_inicio = result.hora_inicio
        self.hora_final = result.hora_final
        self.tipo = result.tipo
        self.cod_docente = result.cod_docente
        self.cod_clase = result.cod_clase
        self.cod_aula = result.cod_aula