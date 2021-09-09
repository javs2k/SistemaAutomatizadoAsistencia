import bd
import utils
import wx
import datetime
from views.Reportes.reporteEXCEL import reporteEXCEL

def asistencia(clase, semana, dia, bus):
    
    # SEMANA DE REFERENCIA REAL DE INICIO DE CLASES: 12 , CONSIDERADA AHORA: 23
    semanaQ = semana + 33

    # print(datetime.date(2019, 3, 17).isocalendar()[1])
    lis = bd.consultaClase(clase, semanaQ, dia, bus)
    asistentes = [i[0] for i in lis]
    a_m = bd.alumnos_matriculados(clase)
    asistentes = utils.intersectarListas(asistentes,a_m)

    namesA = bd.getNombres(asistentes)

    output_real = []
    for i, j in zip(asistentes, namesA):
        output_real.append([i, j])

    output_real = utils.ordenar_por(output_real, 1)

    return output_real

def inasistencia(clase, semana, dia, bus):
    # SEMANA DE REFERENCIA REAL DE INICIO DE CLASES: 12 , CONSIDERADA AHORA: 23
    semanaQ = semana + 33
    # lista de matriculados

    # print(datetime.date(2019, 3, 17).isocalendar()[1])
    lis = bd.consultaClase(clase, semanaQ, dia, bus)
    lis2 = bd.busquedaPorNombre(clase, bus)
    asistentes = [i[0] for i in lis]
    inasistentes = utils.diferenciaListas(lis2, asistentes)

    namesI = bd.getNombres(inasistentes)

    output_real = []

    for i, j in zip(inasistentes, namesI):
        output_real.append([i, j])

    output_real = utils.ordenar_por(output_real, 1)

    return output_real

semana = utils.semana_actual() - 33

def report_asist_horario(curso,registros_exc):
    porcentaje=[]
    titulo = "ASISTENCIA POR HORARIOS"
    cabecera = ("Codigo", "Nombre")
    nombreEXCEL = "ASISTENCIA POR HORARIOS"
    a=len(registros_exc)
    i=0
    for i in range(a):
        porcentaje=porcentaje + [(100)]
    reporte = reporteEXCEL(titulo,curso, cabecera, registros_exc, nombreEXCEL,porcentaje).Exportar()
    return reporte

class ven_asistencia(wx.Frame):
    def __init__(self, parent, title, clase):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title,
                            pos=wx.DefaultPosition,
                            size=wx.Size(780, 500),
                            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"ASISTENCIA DE ALUMNOS",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer5.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer5)
        self.m_panel6.Layout()
        bSizer5.Fit(self.m_panel6)
        self.bSizer4.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        m_radioBox5Choices = [u"Asistencia", u"Inasistencia"]
        self.m_radioBox5 = wx.RadioBox(self.m_panel7, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition,
                                        wx.DefaultSize, m_radioBox5Choices, 1,
                                        wx.RA_SPECIFY_ROWS)
        self.m_radioBox5.SetSelection(0)
        bSizer6.Add(self.m_radioBox5, 0, wx.ALIGN_CENTER | wx.ALL | wx.BOTTOM, 1)

        self.m_panel7.SetSizer(bSizer6)
        self.m_panel7.Layout()
        bSizer6.Fit(self.m_panel7)
        self.bSizer4.Add(self.m_panel7, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Seleccionar semana: ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer7.Add(self.m_staticText7, 0, wx.ALL, 5)

        m_choice1Choices = [u"Semana 1", u"Semana 2", u"Semana 3", u"Semana 4", u"Semana 5",
                            u"Semana 6", u"Semana 7", u"Semana 8", u"Semana 9", u"Semana 10",
                            u"Semana 11", u"Semana 12", u"Semana 13", u"Semana 14",
                            u"Semana 15",
                            u"Semana 16"]
        self.m_choice1 = wx.Choice(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    m_choice1Choices, 0)
        self.m_choice1.SetSelection(semana-1)
        bSizer7.Add(self.m_choice1, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Seleccionar horario: ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer7.Add(self.m_staticText6, 0, wx.ALL, 5)


        lis = bd.consulta(
            "SELECT fecha, hora_inicio, hora_final FROM HORARIO_CLASE WHERE cod_clase = (?)",
            (clase,))

        m_choice2Choices = []
        for i in lis:
            m_choice2Choices.append(i[0]+" "+str(i[1])+":00-"+str(i[2])+":00")


        self.m_choice2 = wx.Choice(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        bSizer7.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Buscar por alumno:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer7.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer7.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_panel8.SetSizer(bSizer7)
        self.m_panel8.Layout()
        bSizer7.Fit(self.m_panel8)
        self.bSizer4.Add(self.m_panel8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Semana actual: " + str(semana),
                                            wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.bSizer4.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        day = {'Monday':1,'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday': 7}
        dayh = int(datetime.date.today().isocalendar()[2])
        dia = lis[0][0]
        for i in lis:
            if day[i[0]]<=dayh: dia = i[0]

        print (dia)

        salida = asistencia(clase, semana, dia, "")
        # Grid

        self.m_grid1.CreateGrid(len(salida), 2)
        self.m_grid1.SetColLabelValue(0, 'Codigo')
        self.m_grid1.SetColLabelValue(1, 'Nombre')
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        registros_exc=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            registros_exc = registros_exc + [(salida[i][0],salida[i][1])]
        
        #GENERAMOS EL REPORTE EXCEL
        report_asist_horario(clase,registros_exc) 

        # Columns
        self.m_grid1.AutoSizeColumns()
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.bSizer4.Add(self.m_grid1, 0, wx.ALL, 5)
        #AGREGANDO EL BOTON DE EXCEL
        self.m_panel9 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_panel9.SetSizer(bSizer8)
        
        self.m_panel9.Layout()
        bSizer8.Fit(self.m_panel9)
        self.bexcel=wx.Button(self.m_panel9,0, u"ABRIR REPORTE EN EXCEL")                                
        self.bimprimir=wx.Button(self.m_panel9,1, u"IMPRIMIR")
        bSizer8.Add(self.bexcel, 1, wx.ALL, 10)
        bSizer8.Add(self.bimprimir, 1, wx.ALL, 10)
        self.bSizer4.Add(self.m_panel9, 0, wx.ALIGN_CENTER, wx.ALL, 5)
        
        

        self.SetSizer(self.bSizer4)
        self.Layout()
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))

        self.Centre(wx.BOTH)

        self.Show()
        # Virtual event handlers, overide them in your derived class
    

    """ def m_choice1OnChoice(self, event):
        bus = str(self.m_textCtrl2.GetValue())
        semana_string = self.m_choice1.GetStringSelection()
        dia_string = self.m_choice2.GetStringSelection()
        x = dia_string.split()
        dia = x[0]
        semana = int(semana_string[7:])
        selection = self.m_radioBox5.GetStringSelection()
        if (selection == u"Asistencia"):
            salida = asistencia(clase, semana, dia, bus)
        else:
            salida = inasistencia(clase, semana, dia, bus)
        self.m_grid1.Destroy()

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_grid1.CreateGrid(len(salida), 2)
        self.m_grid1.SetColLabelValue(0, 'Codigo')
        self.m_grid1.SetColLabelValue(1, 'Nombre')
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)


        registros_exc=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            #Escribimos los datos en el excel
            registros_exc = registros_exc + [(salida[i][0],salida[i][1])]
        
        #GENERAMOS EL REPORTE EXCEL
        report_asist_horario(clase,registros_exc)
            

        # Columns
        self.m_grid1.AutoSizeColumns()
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(40)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        
        #connected events
        self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.reporte )

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.bSizer4.Add(self.m_grid1, 0, wx.ALL, 5)
        
        self.SetSizer(self.bSizer4)
        self.Layout()


        event.Skip()
    def reporte(self, event):
        row = event.GetRow()
        column = 0
        print(column)
        cod_alum = self.m_grid1.GetCellValue(row,column)
        reporte_alumno(cod_alum,clase,cod_h_c)   
        return (cod)
     """