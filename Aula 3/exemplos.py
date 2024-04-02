#Exemplo1
#
# minutos = int(input("Quantos minutos você utilizou?  "))
#
# if minutos < 200:
#     preco = 0.2 * minutos
# elif 400 >= minutos >= 200:
#     preco = 0.18 * minutos
# else:
#     preco = 0.15 * minutos
# print(f"Você vai pagar este mês R$ {preco:.2f} ")

#Exemplo2

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preco = 0

print(f"O preço do produto é de R$ {preco:.2f}")
