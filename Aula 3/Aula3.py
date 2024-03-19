# 1
import velocidade as velocidade

# velocidade = int(input("Velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado por excesso de velocidade, valor total a pagar R$ {multa:.2f}")
else:
    print("Velocidade permitida.")
# 2


# 3.
  
v_salario = float(input("Valor do salário: "))

if v_salario > 1250.00:
    porcentual = 10
else:
    porcentual = 15

v_porcentual = porcentual / 100
aumento = v_porcentual * v_salario
total = v_salario + aumento

print(f"A porcentagem de aumento é de {porcentual}% e o valor do novo salário é de R$ {total:.2f}")
