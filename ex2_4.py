saldo = float(input("Saldo inicial: "))
cheque = float(input("Valor do cheque: "))

if cheque <= saldo:
    saldo_atual = saldo - cheque
    print(f"Cheque descontado, saldo: {saldo_atual:.0f}")
else:
    print("Cheque não pode ser descontado")