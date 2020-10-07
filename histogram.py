import matplotlib
import scipy
import statistics
import pandas
import math

class Histogram:
	"""Графическое отображение:
	- Интервального вариационного ряда
	- Гистограммы
	"""

	def evalIVS(self, table):
		"""Вычисление необходимых величин для интервального ряда"""
		randomNumbers = [18, 38, 28, 29, 26, 38, 34, 22, 28, 30, 22, 23, 35, 33, 27, 24, 30, 32, 28, 25, 29, 26, 31, 24, 29, 27, 32, 25, 29, 29]
		"""Нахождение максимального и минимального значения"""
		minNumber = min(randomNumbers)
		maxNumber = max(randomNumbers)
		"""Вычисление размаха"""
		scope = maxNumber - minNumber
		"""Вычисление количества интервалов"""
		intervalCount = 1 + 3.22 * math.log(len(randomNumbers))
		"""Вычисление оптимальная ширины интервала"""
		intervalWidth = scope / intervalCount
		"""Вычисление границ интервала"""
		bottomLine = minNumber
		topLine = bottomLine + scope
		pass

	def DrawIVSTable(self):
		"""Отображение таблицы интервального вариационного ряда"""
		pass

	def DrawHistogram(self):
		"""Отображение гистограммы"""
		pass

	def DrawDistDensityGraph(self):
		"""Отображение графика плотности распределения"""
		pass