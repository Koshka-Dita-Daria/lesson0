# -*- coding: utf-8 -*-
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
a = zip(first, second)
b = list(a)
first_result = (abs(len(x[0])-len(x[1])) for x in b if len(x[0]) != len(x[1]))
second_result = (len(x) == len(y) for x in first for y in second if first.index(x) == second.index(y))
print(list(first_result))
print(list(second_result))

