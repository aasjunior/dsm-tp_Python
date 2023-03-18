salario_base = 1500
comissao_imovel = 200
vl_venda = 0.05
nome_corretor = input("Digite o nome do corretor: ")
qt_imoveis_vendidos = float(input("Digite a quantidade de imóveis vendidos: "))
vl_total_vendas = float(input("Digite o valor total das vendas: "))
salario_final = salario_base + ((qt_imoveis_vendidos * comissao_imovel) + (((vl_total_vendas / qt_imoveis_vendidos) * vl_venda) * qt_imoveis_vendidos))
print(f"O salário final do corretor {nome_corretor} é R$ {salario_final:.2f}")