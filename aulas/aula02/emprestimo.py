print("Programa de Emprestimos ## Responda: (0 - Não e 1 - Sim)")
negativado = int(input("Possui nome negativado? "))
if negativado == 1:
    print("Não pode realizar empréstimo.")
else:
    carteiraAssinada = int(input("Possui carteira assinada? "))
    if carteiraAssinada == 0:
        print("Não pode realizar empréstimo.")
    else:
        possuiCasaPropria = int(input("Possui casa própria? "))
        if possuiCasaPropria == 0:
            print("Não pode realizar empréstimo.")
        else:
            print("Conceder empréstimo")