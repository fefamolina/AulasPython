# #Exemplo1
# #
#
# pontos = 0
# questao = 1
#
# while questao <= 3:
#     resposta = input(f"Resposta da questão {questao}: ")
#
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     elif questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     elif questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
#
# print(f"O aluno fez {pontos} ponto(s)")

n = 1
soma = 0

while n <= 10:
    x = float(input(f"Digite o número {n}: "))
    soma = soma + x
    n = n + 1

print(f"Soma = {soma:.2f}")
