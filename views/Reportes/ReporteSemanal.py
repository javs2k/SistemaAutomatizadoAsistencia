import wx
import wx.grid
import wx.xrc
from views.Reportes.reporteEXCEL import reporteEXCEL
import bd
import datetime

def ordenar_por(mat, para):
    for i in range(0, len(mat) - 1):
        for j in range(i + 1, len(mat)):
            if (mat[i][para] > mat[j][para]):
                aux = mat[i]
                mat[i] = mat[j]
                mat[j] = aux
    return mat

def report_asist_semana(curso,registros_exc,porcentaje):
    titulo = "ASISTENCIA POR SEMANA"
    cabecera = ("Codigo", "Nombre", "Asistencia", "% de asistencia")
    nombreEXCEL = "ASISTENCIA POR SEMANA"
    reporte = reporteEXCEL(titulo,curso, cabecera, registros_exc, nombreEXCEL,porcentaje).Exportar()
    return(reporte)

def asistencia(clase, semana, bus):  # asistencia semanal de todos los alumnos, por cada clase,

    # SEMANA DE REFERENCIA REAL DE INICIO DE CLASES: 12 , CONSIDERADA AHORA: 23
    cxs = bd.num_clases_semanal(clase)  # numero de clases por semana
    semanaQ = semana + 33
    a_m = bd.alumnos_matriculados(clase)  # lista de matriculados

    lis = bd.consultaSemanal(clase, semanaQ, bus)
    registros = [i[0] for i in lis]
    cod_alumnos = bd.busquedaPorNombre(clase, bus)
    con_asistencia = [registros.count(i) for i in cod_alumnos]
    porc_asistencia = [round((100 * i / ((cxs) * (semana))),2) for i in con_asistencia]

    names = bd.getNombres(cod_alumnos)

    output_real = []
    for i, j, k, l in zip(cod_alumnos, names, con_asistencia, porc_asistencia):
        output_real.append([i, j, k, l])
    print(output_real)
    output_real = ordenar_por(output_real, 1)
    print(output_real)
    return output_real

def inasistencia(clase, semana, bus):

    cxs = bd.num_clases_semanal(clase)

    output_real = asistencia(clase, semana, bus)
    output_realI=[]
    for i in output_real:
        output_realI.append([i[0], i[1], ((cxs) * (semana ))-i[2], 100-i[3]])

    return output_realI

semana = int(datetime.date.today().isocalendar()[1])-33

class ven_reporte_semanal(wx.Frame):
    def __init__(self, parent, title, clase):
        self.clase = clase
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                            size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsz = wx.BoxSizer(wx.VERTICAL)

        self.p1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz1 = wx.BoxSizer(wx.VERTICAL)

        self.st1 = wx.StaticText(self.p1, wx.ID_ANY, u"ASISTENCIA DE ALUMNOS",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.st1.Wrap(-1)
        self.st1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False,
                                    "@Malgun Gothic Semilight"))

        sz1.Add(self.st1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.p1.SetSizer(sz1)
        self.p1.Layout()
        sz1.Fit(self.p1)
        mainsz.Add(self.p1, 0, wx.EXPAND | wx.ALL, 5)

        self.p2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz2 = wx.BoxSizer(wx.VERTICAL)

        choicesAChoices = [u"Asistencia", u"Inasistencia"]
        self.choicesA = wx.RadioBox(self.p2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, choicesAChoices, 1, wx.RA_SPECIFY_ROWS)
        self.choicesA.SetSelection(0)
        sz2.Add(self.choicesA, 0, wx.ALIGN_CENTER | wx.ALL | wx.BOTTOM, 1)

        self.p2.SetSizer(sz2)
        self.p2.Layout()
        sz2.Fit(self.p2)
        mainsz.Add(self.p2, 0, wx.EXPAND | wx.ALL, 5)

        self.p3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz3 = wx.BoxSizer(wx.HORIZONTAL)

        self.st31 = wx.StaticText(self.p3, wx.ID_ANY, u"Buscar por semana:", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.st31.Wrap(-1)
        sz3.Add(self.st31, 0, wx.ALL, 5)

        choicesSChoices = [u"Semana 1", u"Semana 2", u"Semana 3", u"Semana 4", u"Semana 5",
                            u"Semana 6", u"Semana 7", u"Semana 8", u"Semana 9", u"Semana 10",
                            u"Semana 11", u"Semana 12", u"Semana 13", u"Semana 14", u"Semana 15",
                            u"Semana 16"]
        self.choicesS = wx.Choice(self.p3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    choicesSChoices, 0)
        self.choicesS.SetSelection(semana-1)
        sz3.Add(self.choicesS, 0, wx.ALL, 5)

        self.st32 = wx.StaticText(self.p3, wx.ID_ANY, u"Buscar por alumno:", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.st32.Wrap(-1)
        sz3.Add(self.st32, 0, wx.ALL, 5)

        self.tc3 = wx.TextCtrl(self.p3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                wx.DefaultSize, wx.TE_PROCESS_ENTER)
        sz3.Add(self.tc3, 0, wx.ALL, 5)

        self.p3.SetSizer(sz3)
        self.p3.Layout()
        sz3.Fit(self.p3)
        mainsz.Add(self.p3, 0, wx.ALL | wx.EXPAND, 5)

        self.p4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz4 = wx.BoxSizer(wx.VERTICAL)

        self.st4 = wx.StaticText(self.p4, wx.ID_ANY, u"Semana actual:" + str(semana) , wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.st4.Wrap(-1)
        sz4.Add(self.st4, 0, wx.ALL, 5)

        self.p4.SetSizer(sz4)
        self.p4.Layout()
        sz4.Fit(self.p4)
        mainsz.Add(self.p4, 0, wx.EXPAND | wx.ALL, 5)

        self.p5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz5 = wx.BoxSizer(wx.VERTICAL)

        self.table = wx.grid.Grid(self.p5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        salida = asistencia(clase, semana, "")
        # Grid
        self.table.CreateGrid(len(salida), 4)
        self.table.SetColLabelValue(0, 'Codigo')
        self.table.SetColLabelValue(1, 'Nombre')
        self.table.SetColLabelValue(2, 'Asistencia')
        self.table.SetColLabelValue(3, '% de asistencia')
        self.table.EnableEditing(False)
        self.table.EnableGridLines(True)
        self.table.EnableDragGridSize(False)
        self.table.SetMargins(0, 0)
        # [[123,'maguiño', 2, 50%],[],[]]

        registros_exc=[]
        porcentaje=[]
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.table.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.table.SetCellValue(i, 1, "%s" % salida[i][1])
            # añadimos la tercera columna
            self.table.SetCellValue(i, 2, "%s" % salida[i][2])
            # añadimos la cuarta columna
            self.table.SetCellValue(i, 3, "%s" % salida[i][3])
            registros_exc = registros_exc + [(salida[i][0],salida[i][1],salida[i][2],salida[i][3])]
            porcentaje=porcentaje + [(salida[i][3])]
        
        #GENERAMOS EL REPORTE EXCEL
        report_asist_semana(clase,registros_exc,porcentaje)  

        # Columns
        self.table.AutoSizeColumns()
        self.table.EnableDragColMove(False)
        self.table.EnableDragColSize(True)
        self.table.SetColLabelSize(60)
        self.table.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.table.EnableDragRowSize(True)
        self.table.SetRowLabelSize(80)
        self.table.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        self.table.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sz5.Add(self.table, 0, wx.ALL, 5)

        self.p5.SetSizer(sz5)
        self.p5.Layout()
        sz5.Fit(self.p5)
        mainsz.Add(self.p5, 1, wx.EXPAND | wx.ALL, 5)
        
        #AGREGANDO EL BOTON DE EXCEL
        self.p6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.TAB_TRAVERSAL,)
        sz6 = wx.BoxSizer(wx.HORIZONTAL)
        self.bimprimir=wx.Button(self.p6,1, u"IMPRIMIR",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.bexcel=wx.Button(self.p6,0, u"ABRIR REPORTE EN EXCEL",
                                wx.DefaultPosition, wx.DefaultSize, 0)
        sz6.Add(self.bexcel, 1, wx.ALL, 10)
        sz6.Add(self.bimprimir, 1, wx.ALL, 10)
        
        self.p6.SetSizer(sz6)
        self.p6.Layout()
        sz6.Fit(self.p6)
        
        mainsz.Add(self.p6, 0, wx.ALIGN_CENTER, wx.ALL, 5) 
        ##mainsz.Add(self.p6, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(mainsz)
        self.Layout()
        mainsz.Fit(self)

        self.Centre(wx.BOTH)

        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))

        self.Show()
        # Virtual event handlers, overide them in your derived class