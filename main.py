# Импорты библиотек
import wx
# Импорты классов
from histogram import Histogram



class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800,640))

		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "Открыть файл", "Открыть файл с выборкой")
		menuBuffer = filemenu.Append(wx.ID_COPY, "Скопировать буффер", "Скопировать выборку из буффера")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "О программе", "Общая информация о программе")
		menuExit = filemenu.Append(wx.ID_EXIT, "Выйти", "Закрыть программу")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "Файл")
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnCopy, menuBuffer)

		self.Show(True)

	def OnCopy(self, e):
		pass #Копирование из буффера

	def OnOpen(self, e):
		pass #Открытие файла

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "Программа по работе со статистикой\nСовместный проект выполненный группой ПИ-Б19-1", "О программе", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnExit(self, e):
		self.Close(True)


if __name__ == "__main__":
	app = wx.App(False)
	frame = MainWindow(None, "Статистика")
	app.MainLoop()