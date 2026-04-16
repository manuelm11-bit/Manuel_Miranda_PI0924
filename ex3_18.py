limite = int(input("Até que número quer verificar números perfeitos? "))

print("\nNúmeros perfeitos encontrados até " + str(limite) + ":")

quantidade = 0

for num in range(1, limite + 1):
    soma_divisores = 0
    
    for divisor in range(1, num):
        if num % divisor == 0:
            soma_divisores = soma_divisores + divisor
    
    if soma_divisores == num:
        print(str(num) + " é um número perfeito!")
        quantidade = quantidade + 1

print("\nTotal de números perfeitos encontrados: " + str(quantidade))