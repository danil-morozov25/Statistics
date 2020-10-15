from openpyxl import load_workbook, Workbook
import statistics

class StatisticsB():
	def statisticV(name):													#где name - переменная, в которую записана выборка
		try:
			return [len(name), statistics.mean(name), statistics.variance(name), statistics.mode(name), statistics.median(name)]
		except:
			return [len(name), statistics.mean(name), statistics.variance(name), '-', statistics.median(name)]
	
	def sortedV(name):														#где name - переменная, в которую записана выборка
		return sorted(name)

wb = load_workbook(str(input('Введите название файла ')))   #Открытие выборки
sheet = wb.get_sheet_by_name('Лист1')
temp = []
temp2 = []
for row in sheet.rows:
	if type(row[0].value)!=str:
		temp.append(float(row[0].value))
		temp2.append(float(row[1].value))

re = 1
while re<=4:
	re = int(input("""Действие:
	1. Вывести числовые характеристики 1 выборки
	2. Вывести числовые характеристики 2 выборки
	3. Отсортировать 1 выборку
	4. Отсортировать 2 выборку
	5. Выход
	Выбор: """))
	if re==1:
		A = StatisticsB.statisticV(temp)
		print(A)
	if re==2:
		A = StatisticsB.statisticV(temp)
		print(A)
	if re==3:
		B = StatisticsB.sortedV(temp)										#где B[0] - размер; B[1] - среднее; B[2] - дисперсия; B[3] - мода; B[4] - медиана
		print(B)
	if re==4:
		B = StatisticsB.sortedV(temp2)
		print(B)
	
