   
print("\n------------------ ATIVIDADE 6 ------------------\n")

matriz6 = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

print("\n_____ ALTERNATIVA A _____")

#0 = livre
#1 = ocupado
assento = 1

for linha in matriz6:
    for numero in linha:
        if numero == 0:
            print(f"Assento {assento} está livre!")
        else:
            print(f"Assento {assento} está ocupado!")

        assento += 1