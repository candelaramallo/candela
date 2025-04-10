import random
lista = []
for _ in range(20):
    numero = random.randint(1,  100)
    if numero not in lista:
        lista.append(numero)
longitud=len(lista)
print(lista)



persona= ("nombre": "candela","edad":49,)