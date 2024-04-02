# 1
# velocidade = int(input("Velocidade do carro: "))
#
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print(f"Você foi multado por excesso de velocidade, valor total a pagar R$ {multa:.2f}")
# else:
#     print("Velocidade permitida.")
# 2

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
# maior = n1
# menor = n1
#
# if n2 > n1 and n2 > n3:
#     maior = n2
#
# if n3 > n1 and n3 > n1:
#     maior = n3
#
# if n2 < n1 and n2 < n1:
#     menor = n2
#
# if n3 < n1 and n3 < n1:
#     menor = n3

# print(f"O número maior é {maior} e o menor é {menor}")

# 3.
  
# v_salario = float(input("Valor do salário: "))
#
# if v_salario > 1250.00:
#     porcentual = 10
# else:
#     porcentual = 15
#
# v_porcentual = porcentual / 100
# aumento = v_porcentual * v_salario
# total = v_salario + aumento
#
# print(f"A porcentagem de aumento é de {porcentual}% e o valor do novo salário é de R$ {total:.2f}")

#4.
#
# distancia = int(input("Calcule a distancia a percorrer em km/h: "))
#
# if distancia <= 200:
#     preco = 0.50 * distancia
# else:
#     preco = 0.45 * distancia
#
# print(f"O preço da passagem é de R$ {preco:.2f} ")

#5.

n1 = float(input())
n2 = float(input())

if calculo == 1:
    total = n1 + n2
elif calculo == 2:
    total = n1 - n2
elif categoria == 3:
    total = n1 * n2
elif categoria == 4:
    total = n1 / n2
else:
    print("Categoria inválida, digite um valor entre 1 e 4!")
    total = 0

