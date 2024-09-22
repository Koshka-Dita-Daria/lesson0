# -*- coding: utf-8 -*-
import requests
import numpy
import matplotlib.patches
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


r = requests.get('https://urban-university.ru/members/courses/course999421818026/20231222-0000domasnee-zadanie-po-teme-obzor-storonnih-bibliotek-python-400269495184')
print(r.text)
a = numpy.array([[1, 2, 3], [4, 5, 6]])
print(a*2)
print()
print(a-1)
print()
print(a+3)
print()
print(a/2)
print()
plt.xlim(0, 12)
plt.ylim(0, 12)
ax = plt.gca()
circle = Circle((0, 1), 5)
ax.add_patch(circle)
plt.show()