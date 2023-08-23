qnt_percorrido = float(input("Digite a quantidade de Km rodados: "))
qnt_dia = float(input("Digite a quantidade de dias: "))
valor_pagar = (qnt_percorrido * 0.15) + (qnt_dia * 70)
print(f"Você terá que pagar um total de R$ {valor_pagar}")
