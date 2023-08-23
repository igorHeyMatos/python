valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 500.0:
    valor_total = valor_compra * (1.0 - (15 / 100.0))
    print(f"Valor antes do desconto: R${valor_compra}\nValor do desconto: 15%\nValor total a ser pago: R${valor_total}")
elif valor_compra >= 200.0 and valor_compra <= 499.0:
    valor_total = valor_compra * (1.0 - (10 / 100.0))
    print(f"Valor antes do desconto: R${valor_compra}\nValor do desconto: 10%\nValor total a ser pago: R${valor_total}")
elif valor_compra < 200.0 and valor_compra > 0:
    valor_total = valor_compra * (1.0 - (5 / 100.0))
    print(f"Valor antes do desconto: R${valor_compra}\nValor do desconto: 5%\nValor total a ser pago: R${valor_total}")
else:
    print("Valor inválido!")