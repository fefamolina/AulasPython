minutos = int(input("Quantos minutos você utilizou?  "))
if minutos < 200:
    preco = 0.2 * minutos
elif 400 >= minutos >= 200:
    preco = 0.18 * minutos
else:
    preco = 0.15 * minutos
print(f"Você vai pagar este mês R$ {preco:.2f} ")

