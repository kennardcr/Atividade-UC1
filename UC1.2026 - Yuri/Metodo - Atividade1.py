class produto:
    #def init__ é um método construtor, que é chamado quando um objeto da classe é criado. Ele inicializa os atributos do objeto com os valores fornecidos como argumentos.
    def __init__(self, nome, preco, peso, perecivel):
        self.nome = nome
        self.preco = preco
        self.peso = peso
        self.perecivel = perecivel
        #self é uma referência ao objeto atual da classe, permitindo acessar seus atributos e métodos.

#pod1 e prod2 são instâncias da classe produto, que representam produtos específicos com atributos nome, preço, peso e perecível.
prod1 = produto("Maçã Verde", 2, 0.1, True)
prod2 = produto("Pano", 10, 0.2, False)

print(f"Nome: {prod1.nome} - {type(prod1.nome)}") #Acessando o atributo nome do objeto prod1
print(f"Preço: {prod1.preco} - {type(prod1.preco)}") #Acessando o atributo preço do objeto prod1
print(f"Peso: {prod1.peso} - {type(prod1.peso)}") #Acessando o atributo peso do objeto prod1
print(f"Perecível: {prod1.perecivel} - {type(prod1.perecivel)}") #Acessando o atributo perecível do objeto prod1
print("\n")
print(f"Nome: {prod2.nome} - {type(prod2.nome)}") #Acessando o atributo nome do objeto prod2
print(f"Preço: {prod2.preco} - {type(prod2.preco)}") #Acessando o atributo preço do objeto prod2
print(f"Peso: {prod2.peso} - {type(prod2.peso)}") #Acessando o atributo peso do objeto prod2
print(f"Perecível: {prod2.perecivel} - {type(prod2.perecivel)}") #Acessando o atributo perecível do objeto prod2
