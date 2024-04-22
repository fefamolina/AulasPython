#1. Faça um programa para exibir os números de 1 a 100.

# x = 1
#
# while x <= 100:
#     print(x)
#     x = x + 1

#2. Faça um programa para exibir os números de 50 a 100.

# x = 50
# while x <= 100:
#     print(x)
#     x = x + 1
#
# #3. Faça um programa para escrever a contagem
# regressiva do lançamento de um foguete. O programa
# deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! Na tela

# x = 10
# while x >= 1:
#     print(x)
#     x = x - 1

# 4. Faça um programa para imprimir de 1 até o número
# digitado pelo usuário que mostre apenas os números
# ímpares

# num = int(input("Digite um número: "))
# x = 1
# while x <= num:
#     print(x)
#     x = x + 2
#
# 5. Faça um programa para escrever os 10 primeiros
# múltiplos de 3

# num = 30
# x = 3
# while x <= num:
#     print(x)
#     x = x + 3

# 6. Faça um programa para exibir os resultados de uma
# tabuada no formato: 2 x 1 = 2, 2 x 2 = 4, ...
# 7. Modifique o programa interior de forma que o usuário
# também digite o início e o fim da tabuada, em vez de
# começar com 1 e 10

# n = 2
# inicio = int(input("De: "))
# fim = int(input("Até: "))
# x = inicio
#
# while x <= fim:
#     print(f"{n} x {x} = {n*x}")
#     x = x + 1
#
# 8. Escreva um programa que pergunte o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total
# do ganho com juros no período

#
# 9. Altere o programa anterior de forma a perguntar
# também o valor depositado mensalmente. Esse valor
# será depositado no início de cada mês e você deve
# considerá-lo para o cálculo de juros do mês seguinte

# deposito = float(input("Deposito inicial: "))
# taxa = float(input("Taxa de juros: "))
# mensalmente = float(input("Valor depositado mensalmente: "))
# mes = 1
# saldo = deposito

# while mes <= 24:
#     saldo = saldo + (saldo * (taxa /100) + mensalmente)
#     print(f"O saldo do mês de {mes} é de R$ {saldo:.2f}")
#     mes = mes + 1

# print(f"O ganho com juros é de R$ {saldo-deposito:.2f}")

# 10. Escreva um programa que leia números inteiros do teclado. O
# programa deve ler os números até que o usuário digite 0 (zero). No
# final da execução, exiba a quantidade de números digitados, assim
# como a soma e a média aritmética.
    
# soma = 0
# quantidade = 0
# while True:
# num = int(input("Digite um número inteiro: "))
# if num == 0:
# break
# soma = soma + num
# quantidade += 1
# print("Quantidade de números digitados:",quantidade)
# print("Soma =",soma)
# print(f"Média = {(soma/quantidade):.2f}")

# 11. Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar
# ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a
# seguir para obter o preço de cada produto:
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
# código deve gerar a mensagem de erro “Código inválido”.
    
# apagar = 0
# while True:
# codigo = int(input("Código do produto (0 para sair): "))
# preco = 0
# if codigo == 0:
# break
# elif codigo == 1:
# preco = 0.5
# elif codigo == 2:
# preco = 1
# elif codigo == 3:
# preco = 4
# elif codigo == 5:
# preco = 7
# elif codigo == 9:
# preco = 8
# else:
# print("Código inválido!")
# if preco != 0:
# quantidade = int(input("Quantidade: "))
# apagar = apagar+ (preco * quantidade)
# print(f"Total a pagar R${apagar:.2f}")
