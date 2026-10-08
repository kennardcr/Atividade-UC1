#---------------------------------------------- QUESTÃO 2 ----------------------------------------------#

nomes = []
for i in range(5):
    nome = (input(f"Digite o {i+1}° nome: "))
    nomes.append(nome)
    for nome in nomes:
        print(nome)
    
#VAI ADICIONAR UM NOME POR VEZ E INCLUI-LOS NO VETOR, EM SEQUÊNCIA, VAI LISTA-LOS (CADA UM POR LINHA)