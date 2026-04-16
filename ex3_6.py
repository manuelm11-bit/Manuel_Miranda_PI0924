primos = []
n = 2
while len(primos) < 10:
    if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
        primos.append(n)
    n += 1

print(primos)