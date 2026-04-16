notas = []
for i in range(10):
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / 10
acima_media = sum(1 for nota in notas if nota >= media)

print(f"Média: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_media}")