# #4.Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2 

print(f"A soma dos dois números é de: {soma}")

# #5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = int(input("Digite o valor do comprimento: "))

resultado = metros * 1000

print(f"O valor do comprimento em milimetros é de: {resultado} mm")


# #6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = 1
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"O total em segundos é: {total}")

# 7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário. 

salario = float(input("Digite o valor do salário: "))
aumento = float(input("Digite a porcentagem de aumento: "))

calculo = salario * aumento / 100

novo_salario = salario + calculo

print(f"O valor do aumento é de R$ {calculo:.2f}, o valor do novo salario é de R$ {novo_salario:.2f}")

# 8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

v_mercadoria = float(input("Digite o valor da mercadoria: "))
v_desconto = float(input("Digite a porcentagem de desconto: "))

desconto = v_mercadoria * v_desconto / 100 

v_pagar = v_mercadoria - desconto

print(f"O valor do desconto é de R$ {desconto:.2f}, o valor a pagar é de R$ {v_pagar:.2f}")

# 9. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distância a percorrer em km: "))
v_media = float(input("Digite a velocidade média esperada para a viagem (em km/h): "))

tempo = distancia / v_media

print(f"O tempo estimado de viagem é de {tempo} horas")

# 10. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é F = ((9 x C) / 5) + 32

C = int(input("Digite a temperatura: "))

F = ((9 * C) / 5) + 32

print(f"A temperatura em fahrenheit é de {F}º")

# 11. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

qtd = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Quantidade de dias alugados: "))

total = (qtd * 0.15) + (dias * 60)

print(f"O total a pagar é de R$ {total:.2f}")

# 12. Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:z = (x2 + y2) / (x – y)2

x = float(input())
y = float(input())

z = (x**2 + y**2) / (x–y)**2

print(f"{z}")

# 13. Escreva um programa que receba o salário de um funcionário (float) e retorne o resultado do novo salário com reajuste de 35%.

salario = float(input("Digite o valor do salário: "))
v_reajuste = 35

reajuste = salario * v_reajuste / 100 

n_salario = salario + reajuste

print(f"O valor do novo salário com reajuste de 35% é de R$ {n_salario:.2f}")
