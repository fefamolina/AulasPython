cadastro = {"48769878998": ["Fernanda", 2003, "São Paulo", "SP"],
            "56987415632": ["Geovana", 2005, "São Paulo", "SP"],
            "56235469874": ["Ana Clara", 2004, "São Paulo", "SP"]}
while True:
    pessoa = input("Digite o CPF ou fim pra terminar: ")
    if pessoa == "fim" or "Fim":
        break
    if pessoa in cadastro:
        print(cadastro[pessoa])
    else:
        print("CPF não encontrado.")