salario_minimo = float(input("Digite o valor do salário mínimo atual (R$): "))
salario_mensal = float(input("Digite o valor do salário mensal (R$): "))
qt_minimos = salario_mensal / salario_minimo
print(f"A quantidade de salários mínimos é {qt_minimos:.2f}")