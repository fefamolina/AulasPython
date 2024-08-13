cadastro = {"48769878998": ["Fernanda", 2003, "São Paulo", "SP"],
            "56987415632": ["Geovana", 2005, "São Paulo", "SP"],
            "56235469874": ["Ana Clara", 2004, "São Paulo", "SP"]}

for chave, valores in cadastro.items():
    print("Nome: ", valores[0])
    print("CPF: ", chave)
    print("Ano de nascimento: ", valores[1])
    print(f"Cidade e Estado de nascimento: , {valores[2]}/{valores[3]}\n")

while True:
    pessoa = input("Digite o CPF ou fim pra terminar: ").lower()
    if pessoa == "fim":
        break
    elif pessoa in cadastro:
        print(cadastro[pessoa])
        print(cadastro[pessoa][1])
    else:
        print("CPF não encontrado.")