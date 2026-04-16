nums = [int(input(f"num{i+1} = ")) for i in range(3)]
nums_ordenados = sorted(nums)

print(f"Crescente: {nums_ordenados[0]}, {nums_ordenados[1]}, {nums_ordenados[2]}")
print(f"Decrescente: {nums_ordenados[2]}, {nums_ordenados[1]}, {nums_ordenados[0]}")