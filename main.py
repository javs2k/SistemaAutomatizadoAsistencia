# Importando librerías
import os
import winsound
import wx
import wx.grid
import bd
import cv2
from views import InicioSesion, Menu, SeleccionClase, SeleccionReporte
from views.Reportes import ReporteSemanal, ReporteAlumno, Asistencia, Resumen, RankingCiclo, RankingMensual, ListaInvitados
from model.Docente import Docente
from model.Alumno import Alumno
import time
import pyzbar.pyzbar as pyzbar
import webbrowser as wb

class Controller:
    def __init__(self, app):
        self.ven_login()

    def ven_login(self):
        # Vista
        self.login = InicioSesion.ven_inicio_sesion(None, "Iniciar sesión")
        # Eventos
        self.login.b_entrar.Bind(wx.EVT_BUTTON, self.ValidarSesion)
        self.login.tc_clave.Bind(wx.EVT_TEXT_ENTER, self.ValidarSesion)
        self.login.b_salir.Bind(wx.EVT_BUTTON, self.Salir)
        self.login.b_qr.Bind(wx.EVT_BUTTON, self.QR)
        # Mostrar
        self.login.Show()

    def ven_menu(self):
        # Vista
        self.menu = Menu.ven_menu_principal(None, "Menú principal", self.secc)
        # Eventos
        self.menu.b_marcar_asistencia.Bind(wx.EVT_BUTTON, self.MarcarAsistencia)
        self.menu.b_reportes.Bind(wx.EVT_BUTTON, self.Reporte)
        self.menu.b_cerrar_sesion.Bind(wx.EVT_BUTTON, self.CerrarSesion)
        # Mostrar
        self.menu.Show()

    def ven_seleccion_clase(self):
        # Vista
        self.seleccionClase = SeleccionClase.ven_clases_habilitadas(None, "Clases habilitadas", self.docente.secciones)
        # Eventos
        self.seleccionClase.lista.Bind(wx.EVT_LISTBOX, self.SeleccionClase)

    def ven_seleccion_reporte(self):
        # Vista
        self.seleccionReporte = SeleccionReporte.ven_seleccion_reporte(None, "Selecciona reporte", self.claseSeleccionada)
        # Eventos
        self.seleccionReporte.m_bpButton4.Bind(wx.EVT_BUTTON, self.r1)
        self.seleccionReporte.m_bpButton5.Bind(wx.EVT_BUTTON, self.r2)
        self.seleccionReporte.m_bpButton6.Bind(wx.EVT_BUTTON, self.r3)
        self.seleccionReporte.m_bpButton7.Bind(wx.EVT_BUTTON, self.r4)
        self.seleccionReporte.m_bpButton8.Bind(wx.EVT_BUTTON, self.r5)
        self.seleccionReporte.m_bpButton9.Bind(wx.EVT_BUTTON, self.r6)
        self.seleccionReporte.m_button1.Bind(wx.EVT_BUTTON, self.CerrarVenReporte)
    
    def ven_reporte_semanal(self):
        # Vista
        self.reporteSemanal = ReporteSemanal.ven_reporte_semanal(None, "Reporte semanal", self.claseSeleccionada)
        # Eventos
        self.reporteSemanal.table.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ReporteAlumno )
        self.reporteSemanal.bexcel.Bind(wx.EVT_BUTTON, self.ExcelSemanal)
        self.reporteSemanal.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirSemanal)
        self.reporteSemanal.choicesS.Bind(wx.EVT_CHOICE, self.Actualizar)
        self.reporteSemanal.tc3.Bind(wx.EVT_TEXT, self.Actualizar)
        self.reporteSemanal.choicesA.Bind(wx.EVT_RADIOBOX, self.Actualizar)

    def ven_reporte_alumno(self):
        # Vista
        self.reporteAlumno = ReporteAlumno.ven_reporte_alumno(None, "Reporte de alumno", self.claseSeleccionada, self.codAlumnoSeleccionado)
        # Eventos
        self.reporteAlumno.bexcel.Bind(wx.EVT_BUTTON, self.ExcelAlumno)
        self.reporteAlumno.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirAlumno)

    def ven_asistencia(self):
        # Vista
        self.asistencia = Asistencia.ven_asistencia(None, "Asistencia", self.claseSeleccionada)
        # Eventos
        self.asistencia.bexcel.Bind(wx.EVT_BUTTON, self.ExcelAsistencia)
        self.asistencia.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirAsistencia)
        self.asistencia.m_choice1.Bind(wx.EVT_CHOICE, self.FiltroAsistencia)
        self.asistencia.m_choice2.Bind(wx.EVT_CHOICE, self.FiltroAsistencia)
        self.asistencia.m_radioBox5.Bind(wx.EVT_RADIOBOX, self.FiltroAsistencia)
        self.asistencia.m_textCtrl2.Bind(wx.EVT_TEXT, self.FiltroAsistencia)

    def ven_resumen(self):
        # Vista
        self.resumen = Resumen.ven_resumen(None, "Resumen general", self.claseSeleccionada)
        # Eventos
        self.resumen.bexcel.Bind(wx.EVT_BUTTON, self.ExcelResumen)
        self.resumen.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirResumen)

    def ven_ranking_ciclo(self):
        # Vista
        self.rankingCiclo = RankingCiclo.ven_ranking_ciclo(None, "Ranking del ciclo", self.claseSeleccionada)
        # Eventos
        self.rankingCiclo.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ReporteAlumnoRankingCiclo )
        self.rankingCiclo.bexcel.Bind(wx.EVT_BUTTON, self.ExcelRankingCiclo)
        self.rankingCiclo.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirRankingCiclo)
        self.rankingCiclo.m_choice2.Bind(wx.EVT_CHOICE, self.FiltroRankingCiclo)

    def ven_ranking_mensual(self):
        # Vista
        self.rankingMensual = RankingMensual.ven_ranking_mensual(None, "Ranking mensual", self.claseSeleccionada)
        # Eventos
        self.rankingMensual.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ReporteAlumnoRankingMensual )
        self.rankingMensual.bexcel.Bind(wx.EVT_BUTTON, self.ExcelRankingMensual)
        self.rankingMensual.bimprimir.Bind(wx.EVT_BUTTON, self.ImprimirRankingMensual)
        self.rankingMensual.m_choice1.Bind(wx.EVT_CHOICE, self.FiltroRankingMensual)
        self.rankingMensual.m_choice2.Bind(wx.EVT_CHOICE, self.FiltroRankingMensual)

    def ven_invitados(self):
        # Vista
        self.invitados = ListaInvitados.ven_invitados(None, "Lista de invitados", self.claseSeleccionada)
        # Eventos
        self.invitados.bexcel.Bind(wx.EVT_BUTTON, self.ExcelInvitados)
        self.invitados.bimprimirBind(wx.EVT_BUTTON, self.ImprimirInvitados)

    def GoToMenu(self, codDocente):
        # Inicializamos el perfil del docente
        self.docente = Docente(codDocente)
        self.docente.cargarDatos()
        # Buscamos si tiene una clase ahora
        self.clase_actual = self.docente.claseActual()
        if self.clase_actual:
            self.cod_h_c = self.clase_actual.codigo #obtenemos el cod de horario_clase actual
            self.secc = self.clase_actual.cod_clase #obtenemos el cod de la clase ej: BMA01V
        else: # en caso de no encontrarse:
            self.cod_h_c = 0
            self.secc = "AULA LIBRE"
        # Cerramos la interfaz de login
        self.login.Close() 
        # Inicializamos la interfaz menú prinicipal
        self.ven_menu()

    def ValidarSesion(self, event):
        # Obtenemos el código y la clave digitada
        codigoDocente = str(self.login.tc_codigo.GetValue())
        clave = str(self.login.tc_clave.GetValue())
        # Verificamos datos insertados
        if bd.valida_usuario(codigoDocente, clave):
            self.GoToMenu(codigoDocente)
        else:
            wx.MessageDialog(self.login, "Clave y usuario incorrecto!", "Aviso", wx.OK | wx.ICON_WARNING).ShowModal()

    def Salir(self, event):
        self.login.Close()

    def QR(self, event):
        # Iniciar captura de video
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read() # Captura fotograma
            decodedObjects = pyzbar.decode(frame) # Detecta y decodifica el codigo QR ej.: 123456789/12345678
            for obj in decodedObjects: # Recorremos las decodificaciones
                codpas = str(obj.data)
                if len(codpas) != 21:
                    continue
                codpas = codpas[2:20].split('/') # Validamos el formato requerido
                if len(codpas) == 2 and bd.valida_usuario(codpas[0], codpas[1]):
                    self.GoToMenu(codpas[0])
                    cap.release()
                    cv2.destroyAllWindows()
                    return
                else:
                    wx.MessageDialog(self.login, "Código QR incorrecto", "Aviso", wx.OK | wx.ICON_WARNING).ShowModal()
            cv2.imshow("Frame", frame) # Mostramos el fotograma
            # Opción para cancelar la operación presionando "Esc"
            key = cv2.waitKey(1) 
            if key == 27:
                break
        # Cerramos la ventana de validación QR     
        cap.release()
        cv2.destroyAllWindows()

    def CerrarSesion(self, event):
        self.menu.Close()
        self.ven_login()

    def Reporte(self, event):
        self.ven_seleccion_clase()

    def MarcarAsistencia(self, evt):
        if self.secc != "AULA LIBRE":       
            # Verifica si la data ya está entrenada
            fname = "recognizer/trainingData.yml"
            if not os.path.isfile(fname):
                wx.MessageDialog(self.menu, "No se encontró data entranada!", "Aviso", wx.OK | wx.ICON_WARNING).ShowModal()
                exit(0)
            # Realiza el reconocimiento facial
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Carga el modelo para detectar rostros
            cap = cv2.VideoCapture(0) # Capturas 0: Selección de cámara
            recognizer = cv2.face.LBPHFaceRecognizer_create() # Crea el modelo de reconocimiento facial
            recognizer.read(fname) # Carga a través del modelo ya entrenado .yml
            inicio_de_tiempo = time.time() # Inicia a registrar el tiempo
            tiempo_espera = 30 # Indica el tiempo máximo de desuso
            while True:
                tiempo_transcurrido = time.time() - inicio_de_tiempo # Almacena el tiempo transcurrido (en segundos)
                if (tiempo_transcurrido >= tiempo_espera):
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    wx.MessageDialog(self.menu, "Tiempo de espera excedido!", "Error",
                                        wx.OK | wx.ICON_WARNING).ShowModal()
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                _, img = cap.read() # Obtiene el fotograma
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convierte imagen a blanco y negro
                faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detecta los rostros
                for (x, y, w, h) in faces: # Recorre los rostros detectados
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3) # Dibuja un rectángulo al rostro detectado
                    id, conf = recognizer.predict(gray[y:y + h, x:x + w]) # Obtiene al alumno reconocido
                    img = self.procesarAlumno(x, y, w, h, id, conf, img) # Función donde se procesa al alumno
                cv2.imshow('Face Recognizer', img) # Muestra imagen
                # Opción para salir de la ventana presionando "esc" o "q"
                k = cv2.waitKey(30) & 0xff
                r = cv2.waitKey(1) & 0xFF
                if k == 27 or r == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        else:
            wx.MessageDialog(self.menu, "No hay aula donde marcar asistencia!", "Error",
                                wx.OK | wx.ICON_WARNING).ShowModal()

    def procesarAlumno(self, x, y, w, h, id, conf, img):
        
        cod_alumno = bd.getCodigoAlumnoCompleto(str(id)) # Otiene el código completo
        print(str(id) + " " + str(cod_alumno) + " " + str(conf))
        if conf < 50 and cod_alumno:
            self.alumno = Alumno(cod_alumno).cargarDatos() # Instancia la clase Alumno
            # Marca al alumno como reconocido
            cv2.putText(img, 'Reconocido', (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 255, 0), 2)
            # Verifica si el alumno ya registró su asistencia
            if bd.consultarAsistencia(self.alumno.codigo, self.clase_actual.codigo):
                wx.MessageDialog(self.menu, "Asistencia ya registrada!", "Error",
                                    wx.OK | wx.ICON_WARNING).ShowModal()
                print("Asistencia ya registrada")
            else:
                #registra en la tabla asistencia all lo relativo al marcado de asistencia
                self.alumno.registrarAsistencia(self.clase_actual.codigo)
                if (self.alumno.codigo in self.clase_actual.alumnos_matriculados):
                    wx.MessageDialog(self.menu, "Asistencia correctamente registrada!", "Aviso",
                                        wx.OK | wx.ICON_WARNING).ShowModal()
                else:
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    wx.MessageDialog(self.menu, "Usted será registrado como alumno invitado!", "Aviso",
                                        wx.OK | wx.ICON_WARNING).ShowModal() 
        else:
            cv2.putText(img, 'No se reconoce', (x + 2, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)
        return img

    def r1(self, evt):
        self.ven_reporte_semanal()

    def ReporteAlumno(self, event):
        row = event.GetRow()
        cod_alum = self.reporteSemanal.table.GetCellValue(row, 0)
        self.codAlumnoSeleccionado = cod_alum
        self.ven_reporte_alumno()

    def ExcelSemanal(self, event):
        wb.open_new(r'.\excel\ASISTENCIA POR SEMANA.xlsx')
        
    def ImprimirSemanal(self, event):
        nombre_archivo='.\excel\ASISTENCIA POR SEMANA.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")

    def ExcelAlumno(self, event):
        wb.open_new(r'.\excel\REPORTE POR ALUMNO.xlsx')
        
    def ImprimirAlumno(self, event):
        nombre_archivo='.\excel\REPORTE POR ALUMNO.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")
        
    def Actualizar(self, event):
        bus = str(self.reporteSemanal.tc3.GetValue())
        semana_string = self.reporteSemanal.choicesS.GetStringSelection()
        semana = int(semana_string[7:])
        selection = self.reporteSemanal.choicesA.GetStringSelection()
        if (selection==u"Asistencia"):
            salida = ReporteSemanal.asistencia(self.claseSeleccionada, semana, bus)
        else:
            salida = ReporteSemanal.inasistencia(self.claseSeleccionada, semana, bus)
        self.reporteSemanal.table.ClearGrid()
    
        registros_exc=[]
        porcentaje=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.reporteSemanal.table.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.reporteSemanal.table.SetCellValue(i, 1, "%s" % salida[i][1])
            # añadimos la tercera columna
            self.reporteSemanal.table.SetCellValue(i, 2, "%s" % salida[i][2])
            # añadimos la cuarta columna
            self.reporteSemanal.table.SetCellValue(i, 3, "%s" % salida[i][3])
            porcentaje=porcentaje + [(salida[i][3])]
            registros_exc = registros_exc + [(salida[i][0],salida[i][1],salida[i][2],salida[i][3])]
        #GENERAMOS EL REPORTE EXCEL
        ReporteSemanal.report_asist_semana(self.claseSeleccionada,registros_exc,porcentaje)
        event.Skip()
    
    def r2(self, evt):
        self.ven_asistencia()

    def ExcelAsistencia(self, event):
        wb.open_new(r'.\excel\ASISTENCIA POR HORARIOS.xlsx')

    def ImprimirAsistencia(self, event):
        nombre_archivo='.\excel\ASISTENCIA POR HORARIOS.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")

    def FiltroAsistencia(self, event):
        bus = str(self.asistencia.m_textCtrl2.GetValue())
        semana_string = self.asistencia.m_choice1.GetStringSelection()
        dia_string = self.asistencia.m_choice2.GetStringSelection()
        x = dia_string.split()
        dia = x[0]
        semana = int(semana_string[7:])
        selection = self.asistencia.m_radioBox5.GetStringSelection()
        if (selection == u"Asistencia"):
            salida = Asistencia.asistencia(self.claseSeleccionada, semana, dia, bus)
        else:
            salida = Asistencia.inasistencia(self.claseSeleccionada, semana, dia, bus)

        self.asistencia.m_grid1.Destroy()

        self.asistencia.m_grid1 = wx.grid.Grid(self.asistencia, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,0)
        self.asistencia.m_grid1.CreateGrid(len(salida), 2)
        self.asistencia.m_grid1.SetColLabelValue(0, 'Codigo')
        self.asistencia.m_grid1.SetColLabelValue(1, 'Nombre')
        self.asistencia.m_grid1.EnableEditing(False)
        self.asistencia.m_grid1.EnableGridLines(True)
        self.asistencia.m_grid1.EnableDragGridSize(False)
        self.asistencia.m_grid1.SetMargins(0, 0)

        registros_exc=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.asistencia.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.asistencia.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            #Escribimos los datos en el excel
            registros_exc = registros_exc + [(salida[i][0],salida[i][1])]
        
        #GENERAMOS EL REPORTE EXCEL
        Asistencia.report_asist_horario(self.claseSeleccionada,registros_exc)

        # Columns
        self.asistencia.m_grid1.AutoSizeColumns()
        self.asistencia.m_grid1.EnableDragColMove(False)
        self.asistencia.m_grid1.EnableDragColSize(True)
        self.asistencia.m_grid1.SetColLabelSize(40)
        self.asistencia.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.asistencia.m_grid1.AutoSizeRows()
        self.asistencia.m_grid1.EnableDragRowSize(True)
        self.asistencia.m_grid1.SetRowLabelSize(80)
        self.asistencia.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        
        #connected events
        self.asistencia.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.reporteAlumnoAsistencia )

        # Cell Defaults
        self.asistencia.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.asistencia.bSizer4.Add(self.asistencia.m_grid1, 0, wx.ALL, 5)
        
        self.asistencia.SetSizer(self.asistencia.bSizer4)
        self.asistencia.Layout()

        event.Skip()

    def reporteAlumnoAsistencia(self, event):
        row = event.GetRow()
        cod_alum = self.asistencia.m_grid1.GetCellValue(row,0)
        self.codAlumnoSeleccionado = cod_alum
        self.ven_reporte_alumno()

    def r3(self, evt):
        self.ven_resumen()
    
    def ExcelResumen(self, event):
        wb.open_new(r'.\excel\RESUMEN SEMANAL DE ASISTENCIAS.xlsx')
        
    def ImprimirResumen(self, event):
        nombre_archivo='.\excel\RESUMEN SEMANAL DE ASISTENCIAS.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")

    def r4(self, evt):
        self.ven_ranking_ciclo()

    def FiltroRankingCiclo(self, event):
    
        dia_string = self.rankingCiclo.m_choice2.GetStringSelection()
        if (dia_string != "Todos"):
            x = dia_string.split()
            dia = x[0]
        else:
            dia = ""

        salida = RankingCiclo.asistencia(self.claseSeleccionada, dia)

        self.rankingCiclo.m_grid1.Destroy()

        self.rankingCiclo.m_grid1 = wx.grid.Grid(self.rankingCiclo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.rankingCiclo.m_grid1.CreateGrid(len(salida), 3)
        self.rankingCiclo.m_grid1.SetColLabelValue(0, 'Codigo')
        self.rankingCiclo.m_grid1.SetColLabelValue(1, 'Nombre')
        self.rankingCiclo.m_grid1.SetColLabelValue(2, 'Nro. de Asistencias')
        self.rankingCiclo.m_grid1.EnableEditing(False)
        self.rankingCiclo.m_grid1.EnableGridLines(True)
        self.rankingCiclo.m_grid1.EnableDragGridSize(False)
        self.rankingCiclo.m_grid1.SetMargins(0, 0)
        
        registros_exc=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.rankingCiclo.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.rankingCiclo.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            # añadimos la tercera columna
            self.rankingCiclo.m_grid1.SetCellValue(i, 2, "%s" % salida[i][2])
            #ESCRIBIMOS LOS DATOS EN EL EXCEL
            registros_exc = registros_exc + [(salida[i][0],salida[i][1],salida[i][2])]
            
        #GENERAMOS EL REPORTE EXCEL
        RankingCiclo.report_ranking1(self.claseSeleccionada,registros_exc)

        # Columns
        self.rankingCiclo.m_grid1.AutoSizeColumns()
        self.rankingCiclo.m_grid1.EnableDragColMove(False)
        self.rankingCiclo.m_grid1.EnableDragColSize(True)
        self.rankingCiclo.m_grid1.SetColLabelSize(40)
        self.rankingCiclo.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.rankingCiclo.m_grid1.AutoSizeRows()
        self.rankingCiclo.m_grid1.EnableDragRowSize(True)
        self.rankingCiclo.m_grid1.SetRowLabelSize(80)
        self.rankingCiclo.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        
        #connected events
        self.rankingCiclo.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ReporteAlumnoRankingCiclo )


        # Cell Defaults
        self.rankingCiclo.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.rankingCiclo.bSizer4.Add(self.rankingCiclo.m_grid1, 0, wx.ALL, 5)
        

        self.rankingCiclo.SetSizer(self.rankingCiclo.bSizer4)
        self.rankingCiclo.Layout()


        event.Skip() 

    def ReporteAlumnoRankingCiclo(self, event):
        row = event.GetRow()
        cod_alum = self.rankingCiclo.m_grid1.GetCellValue(row, 0)
        self.codAlumnoSeleccionado = cod_alum
        self.ven_reporte_alumno()
        
    def ExcelRankingCiclo(self, event):
        wb.open_new(r'.\excel\RANKING DEL CICLO.xlsx')
    
    def ImprimirRankingCiclo(self, event):
        nombre_archivo='.\excel\RANKING DEL CICLO.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")

    def r5(self, evt):
        self.ven_ranking_mensual()
    
    def FiltroRankingMensual(self, event):
        mes_string = self.rankingMensual.m_choice1.GetStringSelection()
        dia_string = self.rankingMensual.m_choice2.GetStringSelection()
        if (dia_string != "Todos"):
            x = dia_string.split()
            dia = x[0]
        else:
            dia = ""

        mes = int(mes_string[4:])

        salida = RankingMensual.asistencia(self.claseSeleccionada, mes, dia)

        self.rankingMensual.m_grid1.Destroy()

        self.rankingMensual.m_grid1 = wx.grid.Grid(self.rankingMensual, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.rankingMensual.m_grid1.CreateGrid(len(salida), 3)
        self.rankingMensual.m_grid1.SetColLabelValue(0, 'Codigo')
        self.rankingMensual.m_grid1.SetColLabelValue(1, 'Nombre')
        self.rankingMensual.m_grid1.SetColLabelValue(2, 'Nro. de Asistencias')
        self.rankingMensual.m_grid1.EnableEditing(False)
        self.rankingMensual.m_grid1.EnableGridLines(True)
        self.rankingMensual.m_grid1.EnableDragGridSize(False)
        self.rankingMensual.m_grid1.SetMargins(0, 0)
        
        registros_exc=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.rankingMensual.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.rankingMensual.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            # añadimos la tercera columna
            self.rankingMensual.m_grid1.SetCellValue(i, 2, "%s" % salida[i][2])
            #ESCRIBIMOS LOS DATOS EN EL EXCEL
            registros_exc = registros_exc + [(salida[i][0],salida[i][1],salida[i][2])]
            
        #GENERAMOS EL REPORTE EXCEL
        RankingMensual.report_ranking2(self.claseSeleccionada,registros_exc)
        
        # Columns
        self.rankingMensual.m_grid1.AutoSizeColumns()
        self.rankingMensual.m_grid1.EnableDragColMove(False)
        self.rankingMensual.m_grid1.EnableDragColSize(True)
        self.rankingMensual.m_grid1.SetColLabelSize(40)
        self.rankingMensual.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.rankingMensual.m_grid1.AutoSizeRows()
        self.rankingMensual.m_grid1.EnableDragRowSize(True)
        self.rankingMensual.m_grid1.SetRowLabelSize(80)
        self.rankingMensual.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        
        #connected events
        self.rankingMensual.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ReporteAlumnoRankingMensual )

        # Cell Defaults
        self.rankingMensual.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.rankingMensual.bSizer4.Add(self.rankingMensual.m_grid1, 0, wx.ALL, 5)

        self.rankingMensual.SetSizer(self.rankingMensual.bSizer4)
        self.rankingMensual.Layout()

        event.Skip()
        
    def ReporteAlumnoRankingMensual(self, event):
        row = event.GetRow()
        cod_alum = self.rankingMensual.m_grid1.GetCellValue(row, 0)
        self.codAlumnoSeleccionado = cod_alum
        self.ven_reporte_alumno()

    def ExcelRankingMensual(self, event):
        wb.open_new(r'.\excel\RANKING MENSUAL.xlsx')
        
    def ImprimirRankingMensual(self, event):
        nombre_archivo='.\excel\RANKING MENSUAL.xlsx'
        open(nombre_archivo,"r")
        os.startfile(nombre_archivo,"print")

    def r6(self, evt):
        self.ven_invitados()

    def ExcelInvitados(self, event):
        wb.open_new(r'.\excel\LISTA DE INVITADOS.xlsx')

    def ImprimirInvitados(self, event):
        nombre_archivo = '.\excel\LISTA DE INVITADOS.xlsx'
        open(nombre_archivo, "r")
        os.startfile(nombre_archivo, "print")

    def CerrarVenReporte(self, evt):
        self.seleccionReporte.Destroy()

    def SeleccionClase(self, evt):
        self.claseSeleccionada = str(self.seleccionClase.lista.GetStringSelection())
        self.seleccionClase.Destroy()
        self.ven_seleccion_reporte()
    
if __name__ == "__main__":
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
