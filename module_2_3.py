my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] > 0:
    print(my_list[i], end=' ')
    if my_list[i] < 0 or i == len(my_list) - 1:
        break
    i += 1
    if my_list[i] == 0:
        i += 1
        continue
