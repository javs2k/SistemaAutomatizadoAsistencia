import wx
import wx.grid

# VENTANA DE MENÚ PRINCIPAL
class ven_menu_principal(wx.Frame):
    def __init__(self, parent, title, secc):
        wx.Frame.__init__(self, parent=parent, title=title, size=(621, 492), 
                            style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # Icono de la ventana
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))
        # Paneles
        panel1 = wx.Panel(self, wx.ID_ANY, wx.Point(-1, -1), wx.DefaultSize, wx.TAB_TRAVERSAL)
        panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL) 
        # Sizers
        mainsz = wx.BoxSizer(wx.VERTICAL)
        sz1 = wx.BoxSizer(wx.VERTICAL)
        sz2 = wx.BoxSizer(wx.VERTICAL)
        sz3 = wx.BoxSizer(wx.HORIZONTAL)
        sz4 = wx.BoxSizer(wx.VERTICAL)       
        # Controles
        self.st_menu = wx.StaticText(panel1, wx.ID_ANY, u"Menu principal", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_CENTRE)
        self.st_seccion = wx.StaticText(panel2, wx.ID_ANY, "Sección: " + secc, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.b_marcar_asistencia = wx.BitmapButton(panel3, wx.ID_ANY, wx.Bitmap('./imagenes/marcar_asistencia.PNG', wx.BITMAP_TYPE_ANY), 
                                                    wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.b_marcar_asistencia.SetBitmapDisabled(wx.Bitmap('./imagenes/bloqueado.png', wx.BITMAP_TYPE_ANY))
        self.b_reportes = wx.BitmapButton(panel3, wx.ID_ANY, wx.Bitmap('./imagenes/reporte.png', wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        self.b_cerrar_sesion = wx.Button(panel3, wx.ID_ANY, u"Cerrar sesión", wx.DefaultPosition, wx.DefaultSize, 0)
        # Agregando elementos a sizers
        sz1.Add(self.st_menu, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sz2.Add(self.st_seccion, 0, wx.ALL, 5)
        sz3.Add(self.b_marcar_asistencia, 0, wx.ALL, 5)
        sz4.Add(self.b_reportes, 0, wx.ALL, 5)
        sz4.Add(self.b_cerrar_sesion, 1, wx.ALIGN_RIGHT | wx.ALL, 5)
        sz3.Add(sz4, 1, wx.EXPAND, 5)
        # Diseñando el sizer principal:
        mainsz.Add(panel1, 0, wx.ALL | wx.EXPAND, 5)
        mainsz.Add(panel2, 0, wx.EXPAND | wx.ALL, 5)
        mainsz.Add(panel3, 1, wx.EXPAND | wx.ALL, 5)
        # Agregando panel a sizer
        panel1.SetSizer(sz1)
        panel2.SetSizer(sz2)
        panel3.SetSizer(sz3)
        self.SetSizer(mainsz)
        # Deshabilitar el botón de asistencia en caso no haya clase
        if(secc == 'AULA LIBRE'):
            self.b_marcar_asistencia.Disable()
        # Fondos y fuentes
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, True, wx.EmptyString))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        panel1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.st_menu.Wrap(-1)
        self.st_menu.SetFont(wx.Font(18, 70, 90, 92, False, "@Microsoft JhengHei UI Light"))
        self.st_menu.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.st_menu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.st_seccion.Wrap(-1)
        self.b_cerrar_sesion.SetFont(wx.Font(15, 70, 90, 90, False, "Yu Gothic Medium"))
        self.b_cerrar_sesion.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
        self.b_cerrar_sesion.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        # Alineamiento
        self.Centre(True)