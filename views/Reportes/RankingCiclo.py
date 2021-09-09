import bd
import utils
import wx
import datetime
from views.Reportes.reporteEXCEL import reporteEXCEL

def report_ranking1(curso,registros_exc):
        porcentaje=[]
        titulo = "RANKING DEL CICLO"
        cabecera = ("Codigo", "Nombre", "Nro. de Asistencias")
        nombreEXCEL = "RANKING DEL CICLO"
        a=len(registros_exc)
        i=0
        for i in range(a):
            porcentaje=porcentaje + [(100)]
        reporte = reporteEXCEL(titulo,curso, cabecera, registros_exc, nombreEXCEL,porcentaje).Exportar()
        return reporte

def asistencia(clase, dia):

    #SEMANA DE REFERENCIA REAL DE INICIO DE CLASES: 12 , CONSIDERADA AHORA: 23
    a_m = bd.alumnos_matriculados(clase)
    #print(datetime.date(2019, 3, 17).isocalendar()[1])
    lis = bd.consultaCiclo(clase, dia)
    registros = [i[0] for i in lis]
    con_asistencia = [registros.count(i) for i in a_m]
    names = bd.getNombres(a_m)

    output_real = []
    for i, j, k in zip(a_m, names, con_asistencia):
        output_real.append([i, j, k])
    # ordenandolo:
    output_real= utils.ordenar_por_inv(output_real, 2)

    return output_real

semana = int(datetime.date.today().isocalendar()[1])-33


class ven_ranking_ciclo(wx.Frame):
    def __init__(self, parent, title, clase):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title,
                            pos=wx.DefaultPosition,
                            size=wx.Size(735, 536),
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
        bSizer5.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer5)
        self.m_panel6.Layout()
        bSizer5.Fit(self.m_panel6)
        self.bSizer4.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel7.SetSizer(bSizer6)
        self.m_panel7.Layout()
        bSizer6.Fit(self.m_panel7)
        self.bSizer4.Add(self.m_panel7, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)




        self.m_staticText6 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Seleccionar horario: ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer7.Add(self.m_staticText6, 0, wx.ALL, 5)


        lis = bd.consulta(
            "SELECT fecha, hora_inicio, hora_final FROM HORARIO_CLASE WHERE cod_clase = (?)",
            (clase,))

        m_choice2Choices = []
        m_choice2Choices.append("Todos")
        for i in lis:
            m_choice2Choices.append(i[0]+" "+str(i[1])+":00-"+str(i[2])+":00")


        self.m_choice2 = wx.Choice(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        bSizer7.Add(self.m_choice2, 0, wx.ALL, 5)



        self.m_panel8.SetSizer(bSizer7)
        self.m_panel8.Layout()
        bSizer7.Fit(self.m_panel8)
        self.bSizer4.Add(self.m_panel8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        day = {'Monday':1,'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday': 7}
        dayh = int(datetime.date.today().isocalendar()[2])
        dia = lis[0][0]
        for i in lis:
            if day[i[0]]<=dayh: dia = i[0]

        print (dia)

        salida = asistencia(clase, "")
        # Grid

        self.m_grid1.CreateGrid(len(salida), 3)
        self.m_grid1.SetColLabelValue(0, 'Codigo')
        self.m_grid1.SetColLabelValue(1, 'Nombre')
        self.m_grid1.SetColLabelValue(2, 'Nro. de Asistencias')
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
            # añadimos la tercera columna
            self.m_grid1.SetCellValue(i, 2, "%s" % salida[i][2])
            
            #ESCRIBIMOS LOS DATOS EN EL EXCEL
            registros_exc = registros_exc + [(salida[i][0],salida[i][1],salida[i][2])]
            
        #GENERAMOS EL REPORTE EXCEL
        report_ranking1(clase,registros_exc)

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
        self.Centre(wx.BOTH)
        
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))
        self.Show()
        # Virtual event handlers, overide them in your derived class