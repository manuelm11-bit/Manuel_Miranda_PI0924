soma = 0
contador = 0

print("Introduza 30 números pares entre 1 e 50:")

while contador < 30:
    num = int(input("Número " + str(contador + 1) + ": "))
    
    if num >= 1 and num <= 50 and num % 2 == 0:
        soma = soma + num
        contador = contador + 1
    else:
        print("Número inválido! Deve ser par e estar entre 1 e 50.")

media = soma / 30

print("\nMédia dos 30 números pares: " + str(round(media, 2)))