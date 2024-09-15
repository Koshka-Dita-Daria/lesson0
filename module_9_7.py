# -*- coding: utf-8 -*-
def is_prime(func):
    def wrapper(d, e, f):
        res = func(d, e, f)
        k = 0
        if abs(res) == 2 or abs(res) == 1:
            print("Простое")
        else:
            for i in range(2, int(res/2)):
                if res % i == 0:
                    k += 1
            if k == 0:
                print("Простое")
            else:
                print("Составное")
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c
result = sum_three(2, 3, 6)
print(result)
