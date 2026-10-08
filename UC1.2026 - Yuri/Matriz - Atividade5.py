print("\n------------------ ATIVIDADE 5 ------------------\n")

matriz5 = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = float(input("Digite um número: "))
        linha.append(numero)
    matriz5.append(linha)
    print(f"As notas do aluno {i+1}, foram cadastradas com sucesso!\n")
    
soma = 0
somar = 0
for linha in matriz5:
    for media in linha:
        med = sum(linha) / len(linha)
        somar += 1
    print(f"A media do {int(somar/3)}° aluno, foi: {med}")
 