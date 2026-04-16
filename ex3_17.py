print("Múltiplos de 5 que não são múltiplos de 3:\n")

cont = 0
for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(str(i), end="  ")
        cont = cont + 1
        
        if cont % 10 == 0:
            print()

print("\n\nTotal de números encontrados: " + str(cont))