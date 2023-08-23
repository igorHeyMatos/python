nome_funcionario = input("Digite o nome do funcionario: ")
num_hrs = float(input("Digite o número de horas trabalhadas: "))
qnt_hora = float(
    input(f"Digite o quanto {nome_funcionario} recebe por hora: "))
salario_funcionario = num_hrs * qnt_hora
print(f"{nome_funcionario} recebe {salario_funcionario}.")
