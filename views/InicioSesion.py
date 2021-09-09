import wx

# VENTANA DE INICIO SESIÓN
class ven_inicio_sesion(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title, size=(390, 405),
                            style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # Icono de la ventana
        self.SetIcon(wx.Icon("./imagenes/UNI.ico"))
        # Paneles:
        panel1 = wx.Panel(self)
        panel2 = wx.Panel(self)
        panel3 = wx.Panel(self)
        panel4 = wx.Panel(self)
        # Imagen UNI
        imagen = wx.StaticBitmap(self, -1, wx.Bitmap('./imagenes/logo_uni.png', wx.BITMAP_TYPE_ANY), pos=wx.Point(0, 0))
        # Sizers:
        mainsz = wx.BoxSizer(wx.VERTICAL)
        sz1 = wx.BoxSizer(wx.HORIZONTAL) # Ingreso de código docente 
        sz2 = wx.BoxSizer(wx.HORIZONTAL) # Ingreso de clave
        sz3 = wx.BoxSizer(wx.HORIZONTAL) # Botones de entrar y salir
        sz4 = wx.BoxSizer(wx.HORIZONTAL) # Botón QR
        # Controles:
        st1 = wx.StaticText(panel1, -1, "Código: ")
        self.tc_codigo = wx.TextCtrl(panel1, -1)
        st2 = wx.StaticText(panel2, -1, u"Clave: ")
        self.tc_clave = wx.TextCtrl(panel2, -1, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.b_entrar = wx.Button(panel3, -1, u"Aceptar")
        self.b_salir = wx.Button(panel3, -1, u"Salir")
        self.b_qr = wx.Button(panel4, -1, u"Código QR")
        # Agregando elementos a sizers:
        sz1.Add(st1, 1, wx.EXPAND | wx.ALL, 15)
        sz1.Add(self.tc_codigo, 1, wx.EXPAND | wx.ALL, 15)
        sz2.Add(st2, 1, wx.EXPAND | wx.ALL, 15)
        sz2.Add(self.tc_clave, 1, wx.EXPAND | wx.ALL, 15)
        sz3.Add(self.b_entrar, 1, wx.EXPAND | wx.ALL, 10)
        sz3.Add(self.b_salir, 1, wx.EXPAND | wx.ALL, 10)
        sz4.Add(self.b_qr, 1, wx.EXPAND | wx.ALL, 10)
        # Diseñando el sizer principal:
        mainsz.Add(imagen, 0, wx.ALIGN_CENTRE)
        mainsz.Add(panel1, 0, wx.ALIGN_CENTRE)
        mainsz.Add(panel2, 0, wx.ALIGN_CENTRE)
        mainsz.Add(panel3, 0, wx.EXPAND | wx.ALL)
        mainsz.Add(panel4, 0, wx.ALIGN_CENTRE)
        # Asignando sizers en paneles:
        panel1.SetSizer(sz1)
        panel2.SetSizer(sz2)
        panel3.SetSizer(sz3)
        panel4.SetSizer(sz4)
        self.SetSizer(mainsz)
        # Fondos y fuentes
        self.SetBackgroundColour(panel1.GetBackgroundColour())
        font1 = self.tc_codigo.GetFont()
        font1.SetPointSize(13)
        st1.SetFont(font1)
        self.tc_codigo.SetFont(font1)
        st2.SetFont(font1)
        self.tc_clave.SetFont(font1)
        self.b_salir.SetFont(font1)
        self.b_entrar.SetFont(font1)
        # Alineamiento
        self.Centre(True)