idade_crianca = int(input("Digite a idade do aluno: "))

if idade_crianca >= 4 and idade_crianca <= 5:
    print("Turma A.")
elif idade_crianca >= 6 and idade_crianca <= 8:
    print("Turma B.")
elif idade_crianca >= 9 and idade_crianca <= 10:
    print("Turma C.")
else:
    print("Sem turma.")