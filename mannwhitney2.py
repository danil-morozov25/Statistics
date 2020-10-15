from scipy.stats import mannwhitneyu
from openpyxl import Workbook, load_workbook

class mannwhitneyu():
    def mann(name1, name2):
        stat, p = mannwhitneyu(name1, name2)
        alpha = 0.05
        if p > alpha:
            return[stat, p, 'Распредления выборки равны (не отвергает H0)']
        else:
            return[stat, p, 'Распределения выборки не равны (отвергает H0)']
    
wb = load_workbook(str(input('Введите название файла ')))
sheet = wb.get_sheet_by_name('Лист1')
name1 = []
name2 = []
for row in sheet.rows:
    if type(row[0].value)!=str:
        name1.append(float(row[0].value))
        name2.append(float(row[1].value))
