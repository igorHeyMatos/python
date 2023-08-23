comissao_garcom = 0.10
conta_cliente = float(input("Digite o total que o cliente gastou: "))
gorjeta = conta_cliente * comissao_garcom
total = gorjeta + conta_cliente
print(f"A conta que o cliente terá que pagar é de R${total} com uma gorjeta de R${gorjeta} para o garçom.")
