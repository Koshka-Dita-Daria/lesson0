my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict:", my_dict)
print("Existing value:", my_dict['Masha'])
print("Not existing value:", my_dict.get('Sasha'))
a = my_dict.pop('Egor')
print("Deleted value:", a)
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print("Modified dictionary:", my_dict)
print()

my_set = {1, 'Яблоко', 42.314}
list1 = {13, (5, 6, 1.6)}
print("Set:", my_set)
my_set.update(set(list1))
my_set.discard(1)
print("Modified set:", my_set)