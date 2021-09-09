import wx
from views.Reportes.reporteEXCEL import reporteEXCEL
import bd

def report_invitados(curso,registros_exc):
    titulo = "LISTA DE INVITADOS"
    cabecera = ("Codigo", "Nombre", "Seccion", "dia", "fecha", "hora")
    nombreEXCEL = "LISTA DE INVITADOS"
    porcentaje=[]
    a=len(registros_exc)
    i=0
    for i in range(a):
        porcentaje=porcentaje + [(100)]
    reporte = reporteEXCEL(titulo,curso, cabecera, registros_exc, nombreEXCEL,porcentaje).Exportar()
    return reporte

def invDeOtrasSecciones(clase):
    result = bd.consulta("SELECT m.cod_alumno, m.cod_curso_seccion, hc.fecha, a.fecha_m, a.hora_m FROM matriculado m, horario_clase hc, asistencia "
                        "a where a.cod_alumno = m.cod_alumno AND hc.cod_horario_clase = a.cod_horario_clase AND "
                        "hc.cod_clase = (?) and m.cod_curso_seccion LIKE (?) and m.cod_curso_seccion<>(?)", (clase, "%"+clase[:(len(clase)-1)]
                                                                                                                +"%", clase))

    cods = [i[0] for i in result]
    names = bd.getNombres(cods)
    secciones = [i[1] for i in result]
    dias = [i[2] for i in result]
    fechas_m = [i[3].strftime('%d/%m/%Y') for i in result]
    horas_m = [i[4] for i in result]

    output_real = []
    for i,j,k,l,m,n in zip(cods, names, secciones, dias, fechas_m, horas_m):
        output_real.append([i,j,k,l,m,n])

    return output_real

class ven_invitados(wx.Frame):
    def __init__(self, parent, title, clase):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title,
                            pos=wx.DefaultPosition,
                            size=wx.Size(735, 606),
                            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.mainsz = wx.BoxSizer(wx.VERTICAL)

        self.p1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                            wx.TAB_TRAVERSAL)
        sz1 = wx.BoxSizer(wx.VERTICAL)

        self.st1 = wx.StaticText(self.p1, wx.ID_ANY, u"LISTA DE INVITADOS",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.st1.Wrap(-1)
        sz1.Add(self.st1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.p1.SetSizer(sz1)
        self.p1.Layout()
        sz1.Fit(self.p1)
        self.mainsz.Add(self.p1, 0, wx.EXPAND | wx.ALL, 5)


        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        salida = invDeOtrasSecciones(clase)
        # Grid
        #cods, names, secciones, fechas, fechas_m, horas_m
        self.m_grid1.CreateGrid(len(salida), 6)
        self.m_grid1.SetColLabelValue(0, 'Codigo')
        self.m_grid1.SetColLabelValue(1, 'Nombre')
        self.m_grid1.SetColLabelValue(2, 'Seccion')
        self.m_grid1.SetColLabelValue(3, 'Dia')
        self.m_grid1.SetColLabelValue(4, 'Fecha')
        self.m_grid1.SetColLabelValue(5, 'Hora')
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        registros_exc = []
        for i in range(0, len(salida)):
            # añadimos la primera columna
            self.m_grid1.SetCellValue(i, 0, "%s" % salida[i][0])
            # añadimos la segunda columna
            self.m_grid1.SetCellValue(i, 1, "%s" % salida[i][1])
            # añadimos la tercera columna
            self.m_grid1.SetCellValue(i, 2, "%s" % salida[i][2])
            # añadimos la cuarta columna
            self.m_grid1.SetCellValue(i, 3, "%s" % salida[i][3])
            # añadimos la quinta columna
            self.m_grid1.SetCellValue(i, 4, "%s" % salida[i][4])
            # añadimos la sexta columna
            self.m_grid1.SetCellValue(i, 5, "%s" % salida[i][5])

            # ESCRIBIMOS LOS DATOS EN EL EXCEL
            registros_exc = registros_exc + [(salida[i][0], salida[i][1], salida[i][2], salida[i][3], salida[i][4], salida[i][5])]

        # GENERAMOS EL REPORTE EXCEL
        report_invitados(clase, registros_exc)

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
        self.mainsz.Add(self.m_grid1, 0, wx.ALL, 5)

        # AGREGANDO EL BOTON DE EXCEL
        self.m_panel9 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_panel9.SetSizer(bSizer8)
        self.m_panel9.Layout()
        bSizer8.Fit(self.m_panel9)
        self.bexcel = wx.Button(self.m_panel9, 0, u"ABRIR REPORTE EN EXCEL")
        self.bimprimir = wx.Button(self.m_panel9, 1, u"IMPRIMIR")
        bSizer8.Add(self.bexcel, 1, wx.ALL, 10)
        bSizer8.Add(self.bimprimir, 1, wx.ALL, 10)
        self.mainsz.Add(self.m_panel9, 0, wx.ALIGN_CENTER, wx.ALL, 5)

        self.SetSizer(self.mainsz)
        self.Layout()

        self.Centre(wx.BOTH)
        
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))

        self.Show()