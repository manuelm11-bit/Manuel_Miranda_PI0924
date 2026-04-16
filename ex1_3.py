pedido = eval(input("Digite o dicionário: "))  # Ex: {"tipo": "venda", "valor": 250}

match pedido:
    case {"tipo": "compra", "valor": valor}:
        print(f"Compra de {valor}€")
    case {"tipo": "venda", "valor": valor}:
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")