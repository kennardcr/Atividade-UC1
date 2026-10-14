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
        
# print("\n------------------ Primeio método ------------------")

# class aluno:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
        
#     def apresentar(self):#O método apresentar é definido dentro da classe Aluno. Ele imprime o nome e a idade do aluno.
#         print("Olá, meu nome é", self.nome)
        
# aluno1 = aluno("Ana", 19)  
# aluno1.apresentar() #Chamando o método apresentar do objeto aluno1, que imprime o nome do aluno.
# #deve ser lembrado da identação do código, pois o método apresentar está dentro da classe Aluno, e deve ser chamado na identação da class Aluno.

# print("\n------------------ Metodos que recebem parâmetros ------------------")

# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
        
#     def depositar(self, valor):#O método depositar é definido dentro da classe Conta. Ele recebe um parâmetro valor e adiciona esse valor ao saldo da conta.
#         self.saldo += valor
        
# conta1 = Conta("Maria", 100)#Maria é o titular da conta1, e o saldo inicial é 100.
# conta1.depositar(50) #Chamando o método depositar do objeto conta1, que adiciona 50 ao saldo da conta.
# print(conta1.saldo) #Imprimindo o saldo da conta1, que agora é 150.

class conta:
    def __init__(self,saldo):
        self.saldo = saldo

    def sacar(self,valor):
        #Verificando se o valor do saque é maior que 0 e menor ou igual ao saldo da conta. Se for, o valor é subtraído do saldo e uma mensagem de sucesso é exibida. Caso contrário, uma mensagem de erro é exibida.
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado!")
        else:
            print("Saque inválido!")

#criando a conta com 100 de saldo
conta_do_cliente = conta(100)

#testanto um saque válido
conta_do_cliente.sacar(30)
#vai imprimir: Saque realizado!

#Testando saque inválido
conta_do_cliente.sacar(200)
#Vai imprimir saque inválido!

#Mostrando o saldo final
print("O saldo final é:", conta_do_cliente.saldo)

# ------------------- CONSTRUINDO UMA CLASSE PRODUTO
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}")

    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.estoque:
            self.estoque -= quantidade
            print("Venda realizada!")
        else:
            print("Venda inválida!")

produto1 = Produto("Mouse", 50, 10)
produto2 = Produto("Teclado", 120,5)

produto1.mostrar_dados()
produto1.vender(3)
produto1.mostrar_dados()