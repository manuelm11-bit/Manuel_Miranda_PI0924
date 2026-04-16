numeros = list(map(int, input("Digite 10 números separados por vírgula: ").split(',')))

pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")