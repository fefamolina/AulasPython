cadastro = {"48769878998": ["Fernanda", 2003, "São Paulo", "SP"],
            "56987415632": ["Geovana", 2005, "São Paulo", "SP"],
            "56235469874": ["Ana Clara", 2004, "São Paulo", "SP"]}
print(cadastro)
print(cadastro["48769878998"])

cadastro["48769878998"][1] = 2004
print(cadastro["48769878998"])

del cadastro["48769878998"]
print(cadastro)

print("48769878998" in cadastro)
print("56987415632" in cadastro)

print(cadastro.keys())
print(cadastro.values())