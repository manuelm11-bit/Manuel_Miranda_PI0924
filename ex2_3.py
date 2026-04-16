num1 = int(input("num1 = "))
num2 = int(input("num2 = "))

if num1 < num2:
    crescente = f"{num1}, {num2}"
    decrescente = f"{num2}, {num1}"
else:
    crescente = f"{num2}, {num1}"
    decrescente = f"{num1}, {num2}"

print(f"Crescente: {crescente}")
print(f"Decrescente: {decrescente}")