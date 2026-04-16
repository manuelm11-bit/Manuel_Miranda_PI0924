numero = int(input("Introduza um número inteiro positivo: "))

if numero <= 1:
    print("Por favor, introduza um número maior que 1.")
else:
    soma = 0
    subtracao = 0
    multiplicacao = 1
    contador_operacoes = 0

    for i in range(1, numero):
        soma = soma + i
        subtracao = subtracao - i
        multiplicacao = multiplicacao * i
        contador_operacoes = contador_operacoes + 1

    print("\n=== Resultados para o número " + str(numero) + " ===")
    print("Soma: " + str(soma))
    print("Subtração: " + str(subtracao))
    print("Multiplicação: " + str(multiplicacao))
    print("Número de operações realizadas: " + str(contador_operacoes))