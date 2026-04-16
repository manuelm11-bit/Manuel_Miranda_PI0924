num = int(input("Digite um número: "))
divisores = sum(1 for i in range(1, num+1) if num % i == 0)
print(f"O número {num} tem {divisores} divisores.")