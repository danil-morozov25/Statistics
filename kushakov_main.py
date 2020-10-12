import wx
import wx.grid

#Стартовая панель

class Start(wx.Panel):

    #Функция создания панели

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        #Установка размеров

        self.SetSize((800, 600))

        #Контейнер для виджетов

        self.boxsizer = wx.BoxSizer(wx.VERTICAL)

        #Наименование панели

        self.name_statictext = wx.StaticText(self, wx.ID_ANY, 'Statistics')

        #Отделяющая линия

        self.line_staticline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(0,2))

        #Кнопки для перехода

        #Ввод/выбор выборки

        self.input_output_button = wx.Button(self, wx.ID_ANY, 'Input/Choose', wx.DefaultPosition, wx.Size(150,25))

        #Расчёт данных

        self.math_button = wx.Button(self, wx.ID_ANY, 'Math', wx.DefaultPosition, wx.Size(150,25))

        #Просмотр результатов

        self.show_button = wx.Button(self, wx.ID_ANY, 'Show', wx.DefaultPosition, wx.Size(150,25))

        #Добавление виджетов в контейнер
        
        self.boxsizer.Add(self.name_statictext,0,wx.CENTER+wx.ALL,20)
        self.boxsizer.Add(self.line_staticline,0,wx.EXPAND)
        self.boxsizer.AddSpacer(20)
        self.boxsizer.Add(self.input_output_button,1,wx.EXPAND)
        self.boxsizer.Add(self.math_button,1,wx.EXPAND)
        self.boxsizer.Add(self.show_button,1,wx.EXPAND)

        self.SetSizer(self. boxsizer)


#Панель ввода/выбора выборки

class Input_Choose(wx.Panel):

    #Функция создания панели

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        #Установка размеров

        self.SetSize((800, 600))

        #Контейнер для виджетов

        self.boxsizer = wx.BoxSizer(wx.VERTICAL)

        #Наименование панели

        self.name_statictext = wx.StaticText(self, wx.ID_ANY, 'Input/Choose')

        #Отделяющая линия

        self.line_staticline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(0,2))

        #Кнопки

        #Загрузка выборки

        self.load_button = wx.Button(self, wx.ID_ANY, "Load", wx.DefaultPosition, wx.Size(150,25))

        #Сохранить выборку

        self.save_button = wx.Button(self, wx.ID_ANY, "Save", wx.DefaultPosition, wx.Size(150,25))

        #Вернуться назад

        self.back_button = wx.Button(self, wx.ID_ANY, "Go back", wx.DefaultPosition, wx.Size(150,25))


        #Кнопки для работы с таблицей

        #Контейнер

        self.grid_buttons_boxsizer = wx.BoxSizer(wx.HORIZONTAL)

        #Добавить варианту

        self.add_variant_button = wx.Button(self, wx.ID_ANY, "Add Variant", wx.DefaultPosition, wx.Size(150,25))

        #Удалить варианту

        self.delete_variant_button = wx.Button(self, wx.ID_ANY, "Delete Variant", wx.DefaultPosition, wx.Size(150,25))

        #Добавление виджетов в контейнер для работы с таблицей

        self.grid_buttons_boxsizer.Add(self.add_variant_button)
        self.grid_buttons_boxsizer.AddSpacer(20)
        self.grid_buttons_boxsizer.Add(self.delete_variant_button)

        #Таблица

        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(0,2)

        #Аттрибуты таблицы

        self.grid.SetColLabelValue(0,"X")
        self.grid.SetColLabelValue(1,"Y")

        #Добавление виджетов в контейнер
        
        self.boxsizer.Add(self.name_statictext,0,wx.CENTER+wx.ALL,20)
        self.boxsizer.Add(self.line_staticline,0,wx.EXPAND)
        self.boxsizer.AddSpacer(20)
        self.boxsizer.Add(self.load_button,0,wx.ALIGN_RIGHT+wx.ALL,20)
        self.boxsizer.Add(self.grid_buttons_boxsizer,0,wx.ALIGN_RIGHT+wx.ALL,20)
        self.boxsizer.Add(self.grid,1,wx.EXPAND)
        self.boxsizer.Add(self.save_button,0,wx.ALIGN_RIGHT+wx.ALL,20)
        self.boxsizer.Add(self.back_button,0,wx.ALIGN_LEFT+wx.ALL,20)

        self.SetSizer(self. boxsizer)


#Панель расчёта данных
       
class Math_Panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text = 'Math_Panel'
        wx.StaticText(self, -1, text, (300, 10))

        self.btn = wx.Button(self, -1, "Change panel", (345, 100))

#Панель просмотра результатов

class Show_Panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        text = 'Show_Panel'
        wx.StaticText(self, -1, text, (300, 10))

        self.btn = wx.Button(self, -1, "Change panel", (345, 100))

#Окно

class Create_Frame(wx.Frame):

    #Создание окна

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Statistics')

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        #Создание панелей

        #Создание стартовой панели

        self.start_panel = Start(self)

        #Создание панели ввода/выбора выборки

        self.input_choose_panel = Input_Choose(self)



        #Добавление всех планей на экран

        #Стартовая панель

        sizer.Add(self.start_panel, 1, wx.EXPAND)
        self.start_panel.Show(True)

        #Панель ввода/выбора выборки

        sizer.Add(self.input_choose_panel, 1, wx.EXPAND)
        self.input_choose_panel.Show(False)





        
        #Связи виджетов с функциями


        #Стартовая панель

        #Связь нажатия кнопки "Ввод/выбор выборки"

        self.start_panel.input_output_button.Bind(wx.EVT_BUTTON, self.go_to_input_choose_panel) 

        
        #Панель ввода/выбора выборки

        #Связь нажатия кнопки "Загрузить"

        self.input_choose_panel.load_button.Bind(wx.EVT_BUTTON, self.load_doc)

        #Связь нажатия кнопки "Добавить варианту"

        self.input_choose_panel.add_variant_button.Bind(wx.EVT_BUTTON, self.add_variant)

        #Связь нажатия кнопки "Удалить варианту"

        self.input_choose_panel.delete_variant_button.Bind(wx.EVT_BUTTON, self.delete_variant)

        #Связь нажатия кнопки "Назад"

        self.input_choose_panel.back_button.Bind(wx.EVT_BUTTON, self.go_to_start_panel)

        #Связь нажатия кнопки "Сохранить"

        self.input_choose_panel.save_button.Bind(wx.EVT_BUTTON, self.save_doc)



        self.SetSize(1280, 720)

    #Функции

    #

    #Проверка связи выводом 1

    def check(self, event):
        wx.MessageBox('1','Check',wx.OK+wx.ICON_INFORMATION)


    #

    #Переход на панель ввода/выбора выборки

    def go_to_input_choose_panel(self, event):
        self.start_panel.Hide()
        self.input_choose_panel.Show()
        self.Layout()

    #Загрузить выборку

    def load_doc(self, event):
        print(1)

    #Добавить варианту

    def add_variant(self, event):
        print(2)


    #Удалить варианту

    def delete_variant(self, event):
        print(3)

    #Сохранить выборку

    def save_doc(self, event):
        print(4)

    #Переход на стартовую панель

    def go_to_start_panel(self, event):
        self.start_panel.Show()
        self.input_choose_panel.Hide()
        self.Layout()




if __name__ == "__main__":
    app = wx.App(False)
    frame = Create_Frame()
    frame.Show()
    app.MainLoop()