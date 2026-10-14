# class Aluno: #class Aluno é uma classe que representa um aluno, mas atualmente não possui atributos ou métodos definidos.
#     pass #pass é uma classe vazia, que não possui atributos ou métodos definidos.

# aluno1 = Aluno() #aluno1 é uma instância da classe Aluno, que representa um aluno específico.

# aluno1.nome = "Carlos"
# aluno1.idade = 20
# aluno1.altura = 1.75
# aluno1.aprovado = True

# #Type() é uma função que retorna o tipo de dado de uma variável. 
# print(aluno1.nome) #nome é uma string;
# print(type(aluno1.idade)) #idade é um inteiro;

# print("\n------------------ Função def ------------------")
# def saudacao():
#     print("Olá, seja bem-vindo(a)!")

# saudacao() #Chamando a função saudacao, que imprime uma mensagem de boas-vindas.

# def apresentar(nome, idade):#def é uma palavra-chave usada para definir uma função. Neste caso, a função apresentar recebe dois parâmetros: nome e idade.
#     print("Nome:", nome)
#     print("Idade:", idade)

# apresentar("Maria", 20) #Chamando a função apresentar, que imprime o nome e a idade fornecidos como argumentos.
# apresentar("Carlos", 25) #Chamando a função apresentar, que imprime o nome e a idade fornecidos como argumentos.

# print("\n------------------ Função _init_ ------------------")
# class Aluno:
#     def __init__(self, nome, idade):#init__ é um método construtor. Ele inicializa os atributos do objeto com os valores fornecidos como argumentos.
#         self.nome = nome
#         self.idade = idade
        
print("\n------------------ Primeio método ------------------")

class aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):#O método apresentar é definido dentro da classe Aluno. Ele imprime o nome e a idade do aluno.
        print("Olá, meu nome é", self.nome)
        
aluno1 = aluno("Ana", 19)  
aluno1.apresentar() #Chamando o método apresentar do objeto aluno1, que imprime o nome do aluno.
#deve ser lembrado da identação do código, pois o método apresentar está dentro da classe Aluno, e deve ser chamado na identação da class Aluno.

print("\n------------------ Metodos que recebem parâmetros ------------------")

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):#O método depositar é definido dentro da classe Conta. Ele recebe um parâmetro valor e adiciona esse valor ao saldo da conta.
        self.saldo += valor
        
conta1 = Conta("Maria", 100)#Maria é o titular da conta1, e o saldo inicial é 100.
conta1.depositar(50) #Chamando o método depositar do objeto conta1, que adiciona 50 ao saldo da conta.
print(conta1.saldo) #Imprimindo o saldo da conta1, que agora é 150.