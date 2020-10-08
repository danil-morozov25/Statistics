import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import math

class Histogram:
	"""Графическое отображение:
	- Интервального вариационного ряда
	- Гистограммы
	"""
	
	def DrawHistogram(self, table):
		"""Вычисление количества интервалов"""
		intervalCount = round(1 + 3.22 * math.log(len(table)))

		"""Параметры отображения гистограмы"""
		n, bins, patches = plt.hist(table, intervalCount, facecolor='red', alpha=0.5, align='left')

		"""Наименование графика и осей"""
		plt.title('Гистограмма')
		plt.xlabel('Интервалы значений')
		plt.ylabel('Частота')

		"""Отображение гистограммы"""
		plt.show()
		pass