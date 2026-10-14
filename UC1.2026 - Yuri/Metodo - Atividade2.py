class Celular:
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

celular1 = Celular("Iphone", "XS Max", 3.299)
celular2 = Celular("Samsung", "S25 Ultra", 4.499)

print(f"Marca: {celular1.marca} - {type(celular1.marca)}")
print(f"Modelo: {celular1.modelo} - {type(celular1.modelo)}")
print(f"Preço: {celular1.preco} - {type(celular1.preco)}")
print("\n")
print(f"Marca: {celular2.marca} - {type(celular2.marca)}")
print(f"Modelo: {celular2.modelo} - {type(celular2.modelo)}")
print(f"Preço: {celular2.preco} - {type(celular2.preco)}")
