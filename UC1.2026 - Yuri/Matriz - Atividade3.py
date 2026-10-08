print("\n------------------ ATIVIDADE 3 ------------------\n")

matriz3 = [
    [7, 8, 9],
    [5, 6, 7],
    [8, 9, 10]
]

print("\n------- ALTERNATIVA A -------")

soma = 0
for linha in matriz3:
    for numero in linha:
        soma += numero
print(f"A soma total dos números da matriz, é igual a: {soma}")

print("\n------- ALTERNATIVA B -------")

for linha in matriz3:
    for numero2 in linha:
        media = sum(numero2) / len(numero2)
print(float(media))
