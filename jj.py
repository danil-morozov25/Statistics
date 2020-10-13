#Манна-Уитни
from scipy.stats import mannwhitneyu
from openpyxl import Workbook, load_workbook
wb = load_workbook(str(input('Введите название файла ')))
sheet = wb.get_sheet_by_name('Лист1')
temp = []
temp2 = []
for row in sheet.rows:
    if type(row[0].value)!=str:
        temp.append(float(row[0].value))
        temp2.append(float(row[1].value))
stat, p = mannwhitneyu(temp, temp2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
    print('Распредления выборки равны (не отвергает H0)')
else:
    print('Распределения выборки не равны (отвергает H0)')
