numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    for j in range(2, int(numbers[i]//2) + 1):
        if numbers[i] % j == 0:
          is_prime = False
          break
        j += 1
    if is_prime == True and numbers[i] != 1:
        primes.append(numbers[i])
    if is_prime == False and numbers[i] != 1:
        not_primes.append(numbers[i])
    i += 1
print(primes)
print(not_primes)