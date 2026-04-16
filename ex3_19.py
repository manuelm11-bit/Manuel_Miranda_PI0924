a, b = 1, 1
print(a, end=" ")
for _ in range(59):
    a, b = b, a + b
    print(b, end=" ")