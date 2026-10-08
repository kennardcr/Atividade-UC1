print("\n------------------ ATIVIDADE 4 ------------------\n")

matriz4 = []

for i in range(2):
    linha = []
    for j in range(3):
        numero = int(input("Digite um número: "))
        linha.append(numero)
    matriz4.append(linha)
    print("\nMatriz costruida com sucesso!")

for linha in matriz4:
    print(linha)
