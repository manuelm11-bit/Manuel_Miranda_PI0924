prod = eval(input("Digite o dicionário: "))

match prod:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")