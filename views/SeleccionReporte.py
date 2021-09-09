import wx

# Interfaz para seleccionar el reporte
class ven_seleccion_reporte(wx.Frame):
    def __init__(self, parent, title, clase):
        wx.Frame.__init__(self, parent=parent, title=title, size=(-1,-1))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Menú de reportes",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(18, 72, 90, 90, False, wx.EmptyString))
        self.m_staticText1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2.Add(self.m_staticText1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Clase:" + clase, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton4 = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r1.jpg', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer4.Add(self.m_bpButton4, 0, wx.ALL, 5)

        self.m_bpButton5 = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r2.png', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer4.Add(self.m_bpButton5, 0, wx.ALL, 5)

        self.m_bpButton6 = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r3.png', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer4.Add(self.m_bpButton6, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer4)
        self.m_panel2.Layout()
        bSizer4.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton7 = wx.BitmapButton(self.m_panel3, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r4.png', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer5.Add(self.m_bpButton7, 0, wx.ALL, 5)

        self.m_bpButton8 = wx.BitmapButton(self.m_panel3, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r5.png', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer5.Add(self.m_bpButton8, 0, wx.ALL, 5)

        self.m_bpButton9 = wx.BitmapButton(self.m_panel3, wx.ID_ANY,
                                            wx.Bitmap('./imagenes/r6.png', wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        bSizer5.Add(self.m_bpButton9, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer5)
        self.m_panel3.Layout()
        bSizer5.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_button1 = wx.Button(self.m_panel4, wx.ID_ANY, u"Finalizar", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer3.Add(self.m_button1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer3)
        self.m_panel4.Layout()
        bSizer3.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))
        self.Centre(wx.BOTH)
        
        self.Show()

    def __del__(self):
        pass