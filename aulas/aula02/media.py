nota1 = int(input("Informe a nota do 1º Bimestre: "))
nota2 = int(input("Informe a nota do 2º Bimestre: "))
media = (nota1 + nota2)/2
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")