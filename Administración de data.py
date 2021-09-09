import bd
import cv2
import os
import wx
from PIL import Image
import numpy as np

c = bd.consulta("SELECT cod_alumno FROM alumno")
cods = [i[0] for i in c]
print (cods)

def post_clase():
    class post_class(wx.Frame):

        def __init__(self, parent):
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(534, 445), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

            self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

            bSizer8 = wx.BoxSizer(wx.VERTICAL)

            self.m_panel8 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer9 = wx.BoxSizer(wx.VERTICAL)

            self.m_bitmap1 = wx.StaticBitmap(self.m_panel8, wx.ID_ANY, wx.Bitmap(
                u"./imagenes/Postponement.jpg", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer9.Add(self.m_bitmap1, 0, wx.ALL | wx.EXPAND, 5)

            self.m_panel9 = wx.Panel(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

            m_listBox1Choices = []
            self.m_listBox1 = wx.ListBox(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         m_listBox1Choices, 0)
            bSizer10.Add(self.m_listBox1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.m_bitmap3 = wx.StaticBitmap(self.m_panel9, wx.ID_ANY, wx.Bitmap(
                u"./imagenes/1200px-Flecha_tesela.svg.png",
                wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer10.Add(self.m_bitmap3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.m_calendar1 = wx.calendar.CalendarCtrl(self.m_panel9, wx.ID_ANY, wx.DefaultDateTime,
                                                        wx.DefaultPosition, wx.DefaultSize,
                                                        wx.calendar.CAL_SHOW_HOLIDAYS)
            bSizer10.Add(self.m_calendar1, 0, wx.ALL, 5)


            self.m_panel9.SetSizer(bSizer10)
            self.m_panel9.Layout()
            bSizer10.Fit(self.m_panel9)
            bSizer9.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

            self.m_button6 = wx.Button(self.m_panel8, wx.ID_ANY, u"Posponer clase", wx.DefaultPosition, wx.DefaultSize,
                                       0)
            bSizer9.Add(self.m_button6, 0, wx.ALL | wx.EXPAND, 5)

            self.m_panel8.SetSizer(bSizer9)
            self.m_panel8.Layout()
            bSizer9.Fit(self.m_panel8)
            bSizer8.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

            self.SetSizer(bSizer8)
            self.Layout()

            self.Centre(wx.BOTH)

        def __del__(self):
            pass

    if __name__ == "__main__":
        app4 = wx.App()
        ventanaPost = post_class(None)
        app4.MainLoop()

def ven_cur():
    class ven_cur(wx.Frame):
        def __init__(self, parent):
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

            self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

            bSizer12 = wx.BoxSizer(wx.VERTICAL)

            self.m_panel10 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer15 = wx.BoxSizer(wx.VERTICAL)

            self.m_staticText9 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"Información del curso", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText9.Wrap(-1)
            bSizer15.Add(self.m_staticText9, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.m_panel11 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_staticText4 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"Código del curso:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText4.Wrap(-1)
            bSizer16.Add(self.m_staticText4, 0, wx.ALL, 5)

            self.m_textCtrl2 = wx.TextCtrl(self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            bSizer16.Add(self.m_textCtrl2, 0, wx.ALL, 5)

            self.m_panel11.SetSizer(bSizer16)
            self.m_panel11.Layout()
            bSizer16.Fit(self.m_panel11)
            bSizer15.Add(self.m_panel11, 0, wx.ALL | wx.EXPAND, 5)

            self.m_panel12 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_staticText5 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"Nombre del curso:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText5.Wrap(-1)
            bSizer17.Add(self.m_staticText5, 0, wx.ALL, 5)

            self.m_textCtrl3 = wx.TextCtrl(self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            bSizer17.Add(self.m_textCtrl3, 0, wx.ALL, 5)

            self.m_panel12.SetSizer(bSizer17)
            self.m_panel12.Layout()
            bSizer17.Fit(self.m_panel12)
            bSizer15.Add(self.m_panel12, 0, wx.EXPAND | wx.ALL, 5)

            self.m_panel121 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer171 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_staticText51 = wx.StaticText(self.m_panel121, wx.ID_ANY, u"Créditos:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_staticText51.Wrap(-1)
            bSizer171.Add(self.m_staticText51, 0, wx.ALL, 5)

            self.m_textCtrl31 = wx.TextCtrl(self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            bSizer171.Add(self.m_textCtrl31, 0, wx.ALL, 5)

            self.m_panel121.SetSizer(bSizer171)
            self.m_panel121.Layout()
            bSizer171.Fit(self.m_panel121)
            bSizer15.Add(self.m_panel121, 0, wx.EXPAND | wx.ALL, 5)

            self.m_panel16 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sbSizer16 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel16, wx.ID_ANY, u"Especialidades"), wx.HORIZONTAL)

            self.m_checkBox2 = wx.CheckBox(sbSizer16.GetStaticBox(), wx.ID_ANY, u"Ingeniería de Sistemas",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
            sbSizer16.Add(self.m_checkBox2, 0, wx.ALL, 5)

            self.m_checkBox3 = wx.CheckBox(sbSizer16.GetStaticBox(), wx.ID_ANY, u"Ingeniería Industrial",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
            sbSizer16.Add(self.m_checkBox3, 0, wx.ALL, 5)

            self.m_panel16.SetSizer(sbSizer16)
            self.m_panel16.Layout()
            sbSizer16.Fit(self.m_panel16)
            bSizer15.Add(self.m_panel16, 0, wx.EXPAND | wx.ALL, 5)

            self.m_panel17 = wx.Panel(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer22 = wx.BoxSizer(wx.VERTICAL)

            m_radioBox2Choices = [u"Obligatorio", u"Electivo"]
            self.m_radioBox2 = wx.RadioBox(self.m_panel17, wx.ID_ANY, u"Tipo", wx.DefaultPosition, wx.DefaultSize,
                                           m_radioBox2Choices, 2, wx.RA_SPECIFY_COLS)
            self.m_radioBox2.SetSelection(0)
            bSizer22.Add(self.m_radioBox2, 0, wx.ALL, 5)

            self.m_panel17.SetSizer(bSizer22)
            self.m_panel17.Layout()
            bSizer22.Fit(self.m_panel17)
            bSizer15.Add(self.m_panel17, 0, wx.EXPAND | wx.ALL, 5)

            self.m_button27 = wx.Button(self.m_panel10, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer15.Add(self.m_button27, 0, wx.ALIGN_CENTER | wx.ALL, 5)

            self.m_panel10.SetSizer(bSizer15)
            self.m_panel10.Layout()
            bSizer15.Fit(self.m_panel10)
            bSizer12.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

            self.Secciones = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            self.Secciones.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

            bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

            m_radioBox4Choices = [u"U", u"V", u"W"]
            self.m_radioBox4 = wx.RadioBox(self.Secciones, wx.ID_ANY, u"Secciones", wx.DefaultPosition, wx.DefaultSize,
                                           m_radioBox4Choices, 3, wx.RA_SPECIFY_COLS)
            self.m_radioBox4.SetSelection(0)
            bSizer23.Add(self.m_radioBox4, 0, wx.ALL, 5)

            self.m_button3 = wx.Button(self.Secciones, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer23.Add(self.m_button3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.m_button2 = wx.Button(self.Secciones, wx.ID_ANY, u"Nueva sección", wx.DefaultPosition, wx.DefaultSize,
                                       0)
            bSizer23.Add(self.m_button2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            self.Secciones.SetSizer(bSizer23)
            self.Secciones.Layout()
            bSizer23.Fit(self.Secciones)
            bSizer12.Add(self.Secciones, 0, wx.EXPAND | wx.ALL, 5)

            self.SetSizer(bSizer12)
            self.Layout()
            bSizer12.Fit(self)

            self.Centre(wx.BOTH)

            # Connect Events
            self.m_button3.Bind(wx.EVT_BUTTON, self.Secc)

            self.Show()

        def __del__(self):
            pass

        # Virtual event handlers, overide them in your derived class
        def Secc(self, event):
            post_clase()
            event.Skip()

    if __name__ == "__main__":
        app3 = wx.App()
        ventanaSecc = ven_cur(None)
        app3.MainLoop()

def edit():
    class Edit(wx.Frame):

        def __init__(self, parent):
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="MENÚ DE EDICIÓN", pos=wx.DefaultPosition,
                              size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

            self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

            mainsz = wx.BoxSizer(wx.VERTICAL)

            self.p1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sz1 = wx.BoxSizer(wx.VERTICAL)

            self.title = wx.StaticText(self.p1, wx.ID_ANY, u"Menú de operaciones", wx.DefaultPosition, wx.DefaultSize,
                                       0)
            self.title.Wrap(-1)
            self.title.SetFont(wx.Font(20, 70, 90, 92, False, "PMingLiU-ExtB"))

            sz1.Add(self.title, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

            alumno = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Alumno"), wx.HORIZONTAL)

            self.new_alum = wx.Button(alumno.GetStaticBox(), wx.ID_ANY, u"Nuevo alumno", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
            alumno.Add(self.new_alum, 0, wx.ALL, 5)

            self.sl1 = wx.StaticLine(alumno.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.LI_VERTICAL)
            alumno.Add(self.sl1, 0, wx.EXPAND | wx.ALL, 5)

            self.bus_alum = wx.SearchCtrl(alumno.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
            self.bus_alum.ShowSearchButton(True)
            self.bus_alum.ShowCancelButton(False)
            self.bus_alum.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

            alumno.Add(self.bus_alum, 0, wx.ALL, 5)

            self.edit_alum = wx.Button(alumno.GetStaticBox(), wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize,
                                       0)
            alumno.Add(self.edit_alum, 0, wx.ALL, 5)

            sz1.Add(alumno, 1, wx.EXPAND, 5)

            docente = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Docente"), wx.HORIZONTAL)

            self.new_doc = wx.Button(docente.GetStaticBox(), wx.ID_ANY, u"Nuevo docente", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
            docente.Add(self.new_doc, 0, wx.ALL, 5)

            self.sl2 = wx.StaticLine(docente.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.LI_VERTICAL)
            docente.Add(self.sl2, 0, wx.EXPAND | wx.ALL, 5)

            print(bd.allDocentes())
            bus_docChoices = bd.allDocentes()
            self.bus_doc = wx.Choice(docente.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     bus_docChoices, 0)
            self.bus_doc.SetSelection(-1)

            docente.Add(self.bus_doc, 0, wx.ALL, 5)

            self.edit_doc = wx.Button(docente.GetStaticBox(), wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize,
                                      0)
            docente.Add(self.edit_doc, 0, wx.ALL, 5)

            sz1.Add(docente, 1, wx.EXPAND, 5)

            curso = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Curso"), wx.HORIZONTAL)

            self.new_cur = wx.Button(curso.GetStaticBox(), wx.ID_ANY, u"Nuevo curso", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
            curso.Add(self.new_cur, 0, wx.ALL, 5)

            self.sl3 = wx.StaticLine(curso.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.LI_VERTICAL)
            curso.Add(self.sl3, 0, wx.EXPAND | wx.ALL, 5)


            bus_curChoices = bd.allCursos()
            self.bus_cur = wx.Choice(curso.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     bus_curChoices, 0)
            self.bus_cur.SetSelection(-1)
            curso.Add(self.bus_cur, 0, wx.ALL, 5)

            self.edit_cur = wx.Button(curso.GetStaticBox(), wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0)
            curso.Add(self.edit_cur, 0, wx.ALL, 5)

            sz1.Add(curso, 1, wx.EXPAND, 5)

            aula = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Aula"), wx.HORIZONTAL)

            self.AgregarAula = wx.Button(aula.GetStaticBox(), wx.ID_ANY, u"Nueva aula", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
            aula.Add(self.AgregarAula, 0, wx.ALL, 5)

            self.m_staticline411 = wx.StaticLine(aula.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.LI_VERTICAL)
            aula.Add(self.m_staticline411, 0, wx.EXPAND | wx.ALL, 5)

            self.m_searchCtrl32 = wx.SearchCtrl(aula.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_searchCtrl32.ShowSearchButton(True)
            self.m_searchCtrl32.ShowCancelButton(False)
            aula.Add(self.m_searchCtrl32, 0, wx.ALL, 5)

            self.m_button10 = wx.Button(aula.GetStaticBox(), wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize,
                                        0)
            aula.Add(self.m_button10, 0, wx.ALL, 5)

            sz1.Add(aula, 1, wx.EXPAND, 5)

            Asistencia = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Asistencia"), wx.HORIZONTAL)

            self.m_button22 = wx.Button(Asistencia.GetStaticBox(), wx.ID_ANY, u"Marcar", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
            Asistencia.Add(self.m_button22, 0, wx.ALL, 5)

            self.m_button23 = wx.Button(Asistencia.GetStaticBox(), wx.ID_ANY, u"Desmarcar", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
            Asistencia.Add(self.m_button23, 0, wx.ALL, 5)

            sz1.Add(Asistencia, 1, wx.EXPAND, 5)

            Matricula = wx.StaticBoxSizer(wx.StaticBox(self.p1, wx.ID_ANY, u"Matricula"), wx.HORIZONTAL)

            self.m_button11 = wx.Button(Matricula.GetStaticBox(), wx.ID_ANY, u"Retiro parcial", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
            Matricula.Add(self.m_button11, 0, wx.ALL, 5)

            self.m_button13 = wx.Button(Matricula.GetStaticBox(), wx.ID_ANY, u"Retiro total", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
            Matricula.Add(self.m_button13, 0, wx.ALL, 5)

            self.change = wx.Button(Matricula.GetStaticBox(), wx.ID_ANY, u"Cambio de sección", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
            Matricula.Add(self.change, 0, wx.ALL, 5)

            sz1.Add(Matricula, 1, wx.EXPAND, 5)

            self.p1.SetSizer(sz1)
            self.p1.Layout()
            sz1.Fit(self.p1)
            mainsz.Add(self.p1, 1, wx.EXPAND | wx.ALL, 5)

            self.SetSizer(mainsz)
            self.Layout()
            mainsz.Fit(self)

            self.Centre(wx.BOTH)

            # Connect Events
            self.edit_cur.Bind(wx.EVT_BUTTON, self.enter_secciones)

            self.Show()

        def __del__(self):
            pass        

        def enter_secciones(self, event):
            curso = self.bus_cur.GetStringSelection()
            ven_cur()
            event.Skip()

    if __name__ == "__main__":
        app2 = wx.App()
        ventanaE = Edit(None)
        app2.MainLoop()

def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'dataset'
    if not os.path.exists('./recognizer'):
        os.makedirs('./recognizer')

    def getImagesWithID(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces

    labels, faces = getImagesWithID(path)
    recognizer.train(faces, labels)
    recognizer.save('recognizer/trainingData.yml')
    cv2.destroyAllWindows()
    
class ven_newAlum ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Código de alumno:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self.m_panel21, wx.ID_ANY, u"Edad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer31.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self.m_panel21, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 14, 80, 14 )
		bSizer31.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer31 )
		self.m_panel21.Layout()
		bSizer31.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"Ciclo relativo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer32.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self.m_panel22, wx.ID_ANY, 50, 1, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer32.Add( self.m_slider1, 0, wx.ALL, 5 )


		self.m_panel22.SetSizer( bSizer32 )
		self.m_panel22.Layout()
		bSizer32.Fit( self.m_panel22 )
		bSizer1.Add( self.m_panel22, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox1Choices = [ u"Ingeniería de Sistemas", u"Ingeniería Industrial" ]
		self.m_radioBox1 = wx.RadioBox( self.m_panel23, wx.ID_ANY, u"Especialidad", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer33.Add( self.m_radioBox1, 0, wx.ALL, 5 )


		self.m_panel23.SetSizer( bSizer33 )
		self.m_panel23.Layout()
		bSizer33.Fit( self.m_panel23 )
		bSizer1.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self.m_panel12, wx.ID_ANY, u"Registrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer9 )
		self.m_panel12.Layout()
		bSizer9.Fit( self.m_panel12 )
		bSizer1.Add( self.m_panel12, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.register )

	def __del__( self ):
		pass
"""   
    def register(self, event):
        insert("INSERT INTO ALUMNOS VALUES (?),(?),(?),(?),(?))", (self.m_textCtrl1.getValue()))
"""        
def registro(coda):
    # REGISTRA AL ALUMNO EN LA TABLA ALUMNOS

    #menu.insert('INSERT INTO ALUMNO (cod_alumno, nombre) VALUES (?)', (coda, ))
    # hacer modulo de validación de código con sql

    # CAPTURAS DEL ALUMNO
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    sampleNum = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1
            cv2.imwrite("dataset/User." + str(coda[:8]) + "." + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.waitKey(100)
            cv2.imshow('img', img)
            cv2.waitKey(1)
        if sampleNum > 9:
            break
    cap.release()
    cv2.destroyAllWindows()

# vista para ingresar alumnos
class menu_admin(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        mainsz = wx.BoxSizer(wx.HORIZONTAL)

        self.p1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz1 = wx.BoxSizer(wx.VERTICAL)

        self.p11 = wx.Panel(self.p1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz11 = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self.p11, wx.ID_ANY, u"REGISTRO DE ALUMNO SAS", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.title.Wrap(-1)
        self.title.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        sz11.Add(self.title, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.p11.SetSizer(sz11)
        self.p11.Layout()
        sz11.Fit(self.p11)
        sz1.Add(self.p11, 1, wx.EXPAND | wx.ALL, 5)

        self.p12 = wx.Panel(self.p1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz12 = wx.BoxSizer(wx.HORIZONTAL)

        self.codigo_txt = wx.StaticText(self.p12, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.codigo_txt.Wrap(-1)
        sz12.Add(self.codigo_txt, 0, wx.ALL, 5)

        self.codigo = wx.TextCtrl(self.p12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sz12.Add(self.codigo, 0, wx.ALL, 5)

        self.p12.SetSizer(sz12)
        self.p12.Layout()
        sz12.Fit(self.p12)
        sz1.Add(self.p12, 1, wx.EXPAND | wx.ALL, 5)

        self.p13 = wx.Panel(self.p1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz13 = wx.BoxSizer(wx.HORIZONTAL)

        self.registro = wx.BitmapButton(self.p13, wx.ID_ANY,
                                        wx.Bitmap(u'./imagenes/m_a2.jpg', wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        sz13.Add(self.registro, 0, wx.ALL, 5)

        self.p13.SetSizer(sz13)
        self.p13.Layout()
        sz13.Fit(self.p13)
        sz1.Add(self.p13, 0, wx.EXPAND | wx.ALL, 5)

        self.p1.SetSizer(sz1)
        self.p1.Layout()
        sz1.Fit(self.p1)
        mainsz.Add(self.p1, 0, wx.EXPAND | wx.ALL, 5)

        self.p2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz2 = wx.BoxSizer(wx.VERTICAL)

        self.p21 = wx.Panel(self.p2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz21 = wx.BoxSizer(wx.VERTICAL)

        self.training = wx.BitmapButton(self.p21, wx.ID_ANY,
                                        wx.Bitmap(u'./imagenes/training.jpg', wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        sz21.Add(self.training, 0, wx.ALL, 5)

        self.p21.SetSizer(sz21)
        self.p21.Layout()
        sz21.Fit(self.p21)
        sz2.Add(self.p21, 0, wx.EXPAND | wx.ALL, 5)

        self.p22 = wx.Panel(self.p2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sz22 = wx.BoxSizer(wx.HORIZONTAL)

        self.edit = wx.BitmapButton(self.p22, wx.ID_ANY,
                                    wx.Bitmap(u'./imagenes/edit.png', wx.BITMAP_TYPE_ANY),
                                    wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        sz22.Add(self.edit, 0, wx.ALL, 5)

        self.p22.SetSizer(sz22)
        self.p22.Layout()
        sz22.Fit(self.p22)
        sz2.Add(self.p22, 0, wx.EXPAND | wx.ALL, 5)

        self.p2.SetSizer(sz2)
        self.p2.Layout()
        sz2.Fit(self.p2)
        mainsz.Add(self.p2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(mainsz)
        self.Layout()
        mainsz.Fit(self)

        self.Centre(wx.BOTH)
        # Connect Events
        self.registro.Bind(wx.EVT_BUTTON, self.registrar)
        self.training.Bind(wx.EVT_BUTTON, self.entrenar)
        self.edit.Bind(wx.EVT_BUTTON, self.editar)

        self.Show()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def registrar(self, event):
        cod = self.codigo.GetValue()
        if cod in cods:
            s = './dataset/User.'
            s += cod[:8]
            ss = s+ '.1.jpg'
            if not os.path.exists(ss):
                registro(cod)
            else:
                dlg = wx.MessageDialog(ventana, "Estudiante ya ha sido marcado antes. Desea continuar?!", "Error",
                                 wx.YES_NO | wx.ICON_WARNING)
                ret = dlg.ShowModal()
                dlg.Destroy()
                if ret == wx.ID_YES:
                    for i in range(1,11):
                        r = s+'.'+str(i)+'.jpg'
                        os.remove(r)
                    registro(cod)

        else:
            wx.MessageDialog(ventana, "Estudiante no se encuentra registrado!", "Error",
                             wx.OK | wx.ICON_WARNING).ShowModal()

        self.codigo.SetValue('')
        event.Skip()

    def entrenar(self, event):
        training()
        event.Skip()

    def editar(self, event):
        edit()
        event.Skip()

if __name__ == "__main__":
    app1 = wx.App()
    ventana = menu_admin(None, "SISTEMA DE ASISTENCIA!")
    app1.MainLoop()
