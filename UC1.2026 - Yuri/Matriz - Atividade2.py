print("\n------------------ ATIVIDADE 2 ------------------\n")

matriz2 = [
    [5, 8, 3],
    [2, 7, 9],
    [4, 6, 1]
]
print("\n------- ALTERNATIVA A -------")

for linha in matriz2:
    print(linha)

print("\n------- ALTERNATIVA B -------")

for linha in matriz2:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)
            
print("\n------- ALTERNATIVA C -------")

for linha in matriz2:
    for numero in linha:
        if numero > 5:
            print(numero)
 