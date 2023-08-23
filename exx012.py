salario_atual = float(input("Digite seu salário atual: "))

if salario_atual <= 1400.0:
    salario_corrigido = salario_atual * (1.0 + (15 / 100.0))
    print(f"Aumento de 15%, salário corrigido: R${salario_corrigido}")
elif salario_atual >= 1401.0 and salario_atual <= 2000.0:
    salario_corrigido = salario_atual * (1.0 + (12 / 100.0))
    print(f"Aumento de 12%, salário corrigido: R${salario_corrigido}")
elif salario_atual >= 2001.0 and salario_atual <= 3000.0:
    salario_corrigido = salario_atual * (1.0 + (10 / 100.0))
    print(f"Aumento de 10%, salário corrigido: R${salario_corrigido}")
elif salario_atual >= 3001.0 and salario_atual <= 3800.0:
    salario_corrigido = salario_atual * (1.0 + (7 / 100.0))
    print(f"Aumento de 7%, salário corrigido: R${salario_corrigido}")
elif salario_atual >= 3801.0 and salario_atual <= 5000.0:
    salario_corrigido = salario_atual * (1.0 + (4 / 100.0))
    print(f"Aumento de 4%, salário corrigido: R${salario_corrigido}")
elif salario_atual > 5000.0:
    print("Sem aumento.")