notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média = {(soma/x):.2f}")

# 1. Escreva um programa para ler 7 notas e calcular a média aritmética.
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x+1} = "))
    soma += notas[x]
    x += 1
print(f"Média = {(soma/x):.2f}")


# 2. Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
L = []
V = []
while True:
    lista1 = input("Digite um valor para 1ª lista (fim para terminar): ")
    if lista1 == "fim":
        break
    L.append(lista1)
while True:
    lista2 = input("Digite um valor para 2ª lista (fim para terminar): ")
    if lista2 == "fim":
        break
    V.append(lista2)
Z = []
Z.extend(L + V)
print(Z)

# 3. Modifique o exemplo anterior de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.
L = [15, 7, 27, 39]
pesquisa = int(input("Digite o valor a pesquisar: "))
x = 0
while x < len(L):
    if L[x] == pesquisa:
        break
    x += 1
if x < len(L):
    print(f"{pesquisa} achado na posição {x}.")
else:
    print(f"{pesquisa} não encontrado.")



