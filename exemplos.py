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

# categoria = int(input("Digite a categoria do produto: "))
#
# if categoria == 1:
#     preco = 10
# elif categoria == 2:
#     preco = 18
# elif categoria == 3:
#     preco = 23
# elif categoria == 4:
#     preco = 26
# elif categoria == 5:
#     preco = 31
# else:
#     print("Categoria inválida, digite um valor entre 1 e 5!")
#     preco = 0
#
# print(f"O preço do produto é de R$ {preco:.2f}")

#Exemplo3

print("O seu pacote é o Tchau Pré-Pago Prezão 15GB "
      "Por R$29,99/mês\n")

plano = input("Você utilizou todo o seu pacote (sim/não): ")

if plano == "sim":
    pacote_adiconal = input("Você deseja compra um novo pacote? (sim/não): ")
    if pacote_adiconal == "sim":
        qtd_pacote_adicional = int(input("Digite a quantidade de pacote de franquia adicional de 300MB: "))
        valor_mensal = 29.99 + qtd_pacote_adicional * 7.99
        print(f"O Valor mensal do plano é de R$ {valor_mensal:.2f}.\n")

fechar = input("Aperte o botão ENTER para sair do programa.")
