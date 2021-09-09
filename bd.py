import pyodbc
from model.Curso import Curso
from model.Horario import Horario
import time

server = 'LAPTOP-HRRGPP3L\SQLEXPRESS'
database = 'ASISTENCIA_DB2'

# Conexión a la bd
def conectar():
    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';' +
            'DATABASE='+ database +';' + 
            'Trusted_Connection=yes;'
        )
        return conexion
        # OK! conexión exitosa
    except Exception as e:
        # Capturar error
        print("Ocurrió un error al conectar a SQL Server: ", e)

# Consulta general
def consulta(string, tupla = None):
    conn = conectar()
    cur = conn.cursor()
    if tupla:
        cur.execute(string, tupla)
    else:
        cur.execute(string)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

####### CONSULTAS FRECUENTES #######

def listar_cursos():
    cursos = consulta("SELECT * FROM CURSO")
    response = []
    for curso in cursos:
        c = Curso(curso.cod_curso, curso.nom_curso, curso.creditos, curso.especialidades, curso.observacion)
        response.append(c)
    return response

def listar_nombre_docentes():
    result = consulta("SELECT nombre FROM DOCENTE")
    response = [i[0] for i in result]
    return response

def num_clases_semanal(clase):
    return len(consulta("SELECT dia FROM horario_clase where cod_clase = (?)", (clase,)))

def alumnos_matriculados(clase):
    result = consulta("SELECT cod_alumno FROM matriculado where cod_curso_seccion = (?)", (clase,))
    response = [i[0] for i in result]
    return response

def num_alum_matriculados(clase):
    return len(alumnos_matriculados(clase))

def obtener_cod_clase(cod_horario_clase):
    result = consulta("SELECT cs.cod_clase FROM CURSO_SECCION cs, HORARIO_CLASE hc WHERE cs.cod_clase ="
                 " hc.cod_clase and hc.cod_horario_clase = (?)", (cod_horario_clase,))
    reponse = result[0]

def busquedaPorNombre(clase, bus):
    c = consulta("SELECT al.cod_alumno FROM matriculado m, ALUMNO al where m.cod_alumno = al.cod_alumno and cod_curso_seccion = (?) and "
                    "al.nombre LIKE (?)", (clase, "%"+bus+"%"))
    ae = [i[0] for i in c]
    return ae

def consultaCiclo(clase, dia):
    return consulta("SELECT cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h WHERE a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) "
                    "and h.dia LIKE (?)", (clase,"%"+dia+"%", ))

def consultaMensual(clase, mes, dia):
    return consulta("SELECT cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h WHERE a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) "
                "and DATEPART(month, a.fecha_m)=(?) AND h.dia LIKE (?)", (clase, mes,"%"+dia+"%",))

def consultaSemanal(clase, semana, bus):
    return consulta("SELECT a.cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h, ALUMNO al WHERE a.cod_alumno = al.cod_alumno and al.nombre LIKE "
                                "(?) and a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and DATEPART(week, a.fecha_m)<=(?)",
                                ("%"+bus+"%",clase, semana,))

def consultaClase(clase, semana, dia, bus):
    return consulta("SELECT a.cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h, ALUMNO al WHERE a.cod_alumno = al.cod_alumno and al.nombre LIKE (?) "
                    "and a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and DATEPART(week, a.fecha_m)=(?) and h.dia = (?)",
                                ("%" + bus + "%", clase, semana,dia,))

def getSecciones(cod_curso):
    result = consulta("SELECT cs.cod_clase FROM curso_seccion cs, horario_clase hc WHERE cs.cod_clase = hc.cod_clase and cs.cod_curso = (?)", (cod_curso,))
    secciones = [i[0] for i in result]
    return secciones

def getNombres(cod_alumnos):
    names = []
    for i in cod_alumnos:
        result = consulta("SELECT nombre FROM ALUMNO WHERE cod_alumno=(?)", (str(i),))
        names.append(result[0][0])
    return names

def num_asist_por_alumno(cod_alumno,cod_h_c):
    c = consulta("SELECT cod_asistencia FROM asistencia where cod_alumno = (?) and cod_horario_clase= (?)", (cod_alumno,cod_h_c,))
    return len(c)
    
def datos_alumno(cod_alumno):
    datos=[]
    c = consulta("SELECT * FROM ALUMNO where cod_alumno = (?)", (cod_alumno,))
    nombre = [i[1] for i in c]
    edad = [i[2] for i in c]
    ciclo = [i[3] for i in c]
    espec = [i[4] for i in c]
    datos=[nombre[0],edad[0],ciclo[0],espec[0]]
    return datos

# Función que valida el inicio de sesión al sistema
def valida_usuario(cod_docente, clave):
    result = consulta("SELECT 1 FROM DOCENTE WHERE cod_docente = (?) and clave = (?)", (cod_docente, clave,))
    if result:
        return True
    else: 
        return False

def allCursos():
    a = consulta("SELECT nom_curso FROM CURSO")
    lis = [i[0] for i in a]
    return lis

def allDocentes():
    a = consulta("SELECT nombre FROM DOCENTE")
    lis = [i[0] for i in a]
    return lis

def getNombreDocente(codigoDocente = None):
    if codigoDocente:
        result = consulta("SELECT nombre FROM DOCENTE WHERE cod_docente = (?)", (codigoDocente,))
        return result[0].nombre
    else:
        result = consulta("SELECT nombre FROM DOCENTE")
        return [i.nombre for i in result]

def getClaseActualDocente(codigoDocente):
    ha = int(time.strftime("%H")) #consigo la hora actual ej: son las 13.08 ha = 13
    day = time.strftime("%A") #consigo el dia ej: hoy es 08/07/2019 day = "Monday"
    result = consulta("SELECT * FROM HORARIO_CLASE WHERE dia=(?) AND hora_inicio<=(?) "+
                        "AND hora_final>(?) AND cod_docente = (?)", 
                        (day, ha, ha, codigoDocente))
    if result:
        horario = Horario(result[0].cod_horario_clase)
        horario.cargarDatos()
        return horario
    else:
        return None

def getDatosHorario(cod_horario_clase):
    result = consulta("select * from HORARIO_CLASE where cod_horario_clase = (?)", (cod_horario_clase))
    return result[0]

def getSeccionesDocente(codigoDocente):
    result = consulta("SELECT DISTINCT cod_clase FROM HORARIO_CLASE WHERE cod_docente = (?)", (codigoDocente))
    response = [i.cod_clase for i in result]
    return response

def getCodigoAlumnoCompleto(id):
    result = consulta("select cod_alumno from ALUMNO where cod_alumno LIKE (?);", (str(id)+'%',))
    if result:
        return result[0].cod_alumno
    else:
        return None

def getDatosAlumno(cod_alumno):
    result = consulta("select * from ALUMNO where cod_alumno = (?)", (cod_alumno))
    return result[0]

def consultarAsistencia(cod_alumno, cod_horario_clase):
    dia = str(time.strftime("20%y-%m-%d"))
    resultados= consulta('SELECT cod_alumn FROM ASISTENCIA WHERE cod_horario_clase = (?) AND fecha_m = (?) AND cod_alumno = (?) ', 
                                                (cod_horario_clase , dia, cod_alumno))
    if resultados:
        return True
    else:
        return False

def registraAsistencia(cod_alumno, cod_horario_clase):
    hora_entrada = time.strftime("%H:%M:%S")
    fecha_entrada = str(time.strftime("20%y-%m-%d"))
    consulta('INSERT INTO ASISTENCIA (cod_alumno, cod_horario_clase, hora_m, fecha_m) VALUES ((?),(?),(?),(?))',
                                        (str(cod_alumno), cod_horario_clase, hora_entrada, fecha_entrada,))