for i in range (1,6):
    nota = -1
    
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota do {i}° aluno: "))

    if nota >= 7:
        print(f"Aluno {i} foi aprovado!")

    elif nota >= 5:
        print(f"Aluno {i} está em recuperação!")
    
    else:
        print(f"Aluno {i} foi reprovado!")
        
#PARA CADA ALUNO, VAI SOLICITAR A NOTA VAI DIZER SE FOI APROVADO E SOLICITA A PROXIMA NOTA
