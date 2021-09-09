
import wx

#interfaz de las clases del profesor
class ven_clases_habilitadas(wx.Frame):
    def __init__(self, parent, title, choices):
        wx.Frame.__init__(self, parent=parent, title=title, size=(-1,-1))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Seleccione Clase:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        bSizer8.Add(self.m_staticText1, 0, wx.ALL, 5)

        m_listBox1Choices = choices
        self.lista = wx.ListBox(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                m_listBox1Choices,
                                wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SINGLE | wx.LB_SORT)
        self.lista.SetFont(wx.Font(20, 70, 90, 90, False, "@Microsoft JhengHei Light"))
        self.lista.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.lista.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer8.Add(self.lista, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer8)
        self.m_panel6.Layout()
        bSizer8.Fit(self.m_panel6)
        bSizer7.Add(self.m_panel6, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()
        bSizer7.Fit(self)
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))

        self.Centre(True)
        self.Show()

    def __del__(self):
        pass

    ''' def Seleccionar_clase(self, event):
        clase = str(self.lista.GetStringSelection())
        sel_reporte(clase) '''
