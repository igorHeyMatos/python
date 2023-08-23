nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salario: "))
total_venda = float(input("Digite o total de vendas no mês em dinheiro: "))
total_comissao = 15
total_receber = salario_fixo + (total_venda * 0.15)
print(f"O funcionario {nome_vendedor} irá receber no final do mês : R${total_receber} com uma comissão de {total_comissao}%.")
