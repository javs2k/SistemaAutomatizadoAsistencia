import wx
import bd
from views.Reportes.reporteEXCEL import reporteEXCEL

def report_resum_semana(curso,cabecera,registros_exc):
    porcentaje=[]
    titulo = "RESUMEN SEMANAL DE ASISTENCIAS"
    nombreEXCEL = "RESUMEN SEMANAL DE ASISTENCIAS"
    a=len(registros_exc)
    i=0
    for i in range(a):
        porcentaje=porcentaje + [(100)]
    reporte = reporteEXCEL(titulo,curso, cabecera, registros_exc, nombreEXCEL,porcentaje).Exportar()
    return reporte


class ven_resumen(wx.Frame):
    def __init__(self, parent, title, clase):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                            size=wx.Size(735, 536), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

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
        bSizer4.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        #m_radioBox5Choices = [u"Asistencia", u"Inasistencia"]
        #self.m_radioBox5 = wx.RadioBox(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
        #                                wx.DefaultSize, m_radioBox5Choices, 1, wx.RA_SPECIFY_ROWS)
        # self.m_radioBox5.SetSelection(0)
        # bSizer6.Add(self.m_radioBox5, 0, wx.ALIGN_CENTER | wx.ALL | wx.BOTTOM, 1)

        self.m_panel7.SetSizer(bSizer6)
        self.m_panel7.Layout()
        bSizer6.Fit(self.m_panel7)
        bSizer4.Add(self.m_panel7, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Clase: " + clase,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer7.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_panel8.SetSizer(bSizer7)
        self.m_panel8.Layout()
        bSizer7.Fit(self.m_panel8)
        bSizer4.Add(self.m_panel8, 0, wx.ALL | wx.EXPAND, 5)            

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        lis = bd.consulta("SELECT fecha, hora_inicio, hora_final FROM HORARIO_CLASE WHERE cod_clase = (?)",(clase,))
        day = {'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miercoles', 'Thursday': 'Jueves', 'Friday': 'Viernes',
                'Saturday': 'Sábado', 'Sunday': 'Domingo'}
        
        col = []
        cabecera=[]
        registros_exc=[]
        for i in lis:
            col.append(day[i[0]])

        # Grid
        self.m_grid1.CreateGrid(16, 2*len(lis)+1)
        self.m_grid1.SetColLabelValue(0, "Semana")
        cabecera.append('semana')
        for i in range(1,len(col)+1):
            self.m_grid1.SetColLabelValue(2*i-1, col[i-1])
            self.m_grid1.SetColLabelValue(2*i, "%")
            #insertando dato a la calumna de excel
            cabecera.append(str(col[i-1]))
            cabecera.append('% asist')
            
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)
        #[[123,'maguiño', 2, 50%],[],[]]           
        
        for i in range(0, 16):
            aux=[]
            # añadimos la primera columna
            self.m_grid1.SetCellValue(i, 0, "Semana " + str(i+1))
            a='Semana ' + str(i+1)
            aux.append(a)
            # añadimos la segunda columna
            for j in range(0,len(col)):
                list = bd.consulta(
                    "SELECT cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h WHERE a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) "
                    "and DATEPART(week, a.fecha_m)=(?) and h.fecha = (?)",
                    (clase, i+23, lis[j][0],))

                self.m_grid1.SetCellValue(i, 2*j+1, str(len(list)))
                self.m_grid1.SetCellValue(i, 2*j+2, str(round(100*(len(list)/bd.num_alum_matriculados(clase)),2))+"%")
                aux.append(str(len(list)))
                b=str(round(100*(len(list)/bd.num_alum_matriculados(clase)),2))+'%'
                aux.append(b)
            registros_exc.append(aux)
        #GENERAMOS EL REPORTE EXCEL
        report_resum_semana(clase,cabecera,registros_exc)
        
        
        # Columns
        self.m_grid1.AutoSizeColumns()
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(60)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance.

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        
        
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
        bSizer4.Add(self.m_panel9, 0, wx.ALIGN_CENTER, wx.ALL, 5) 
        bSizer4.Add(self.m_grid1, 0, wx.ALL, 5)
        self.SetSizer(bSizer4)
        self.Layout()
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))

        self.Centre(wx.BOTH)

        # Connect Events
        #self.m_radioBox5.Bind(wx.EVT_RADIOBOX, self.onRadioBox)

        self.Show()
        # Virtual event handlers, overide them in your derived class