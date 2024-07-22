calls = 0
def count_class():
    global calls
    calls += 1
def string_info(string):
    count_class()
    return "(" + str(len(string)) + " " + string.upper() + " " + string.lower() + ")"
def is_contains(string, list_to_search):
    c = False
    for i in range(len(list_to_search)):
        if list_to_search[i].upper() == string.upper():
            c = True
    count_class()
    return c


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
