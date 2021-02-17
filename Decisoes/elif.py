nome=input("Digite o nome: ")
idade=int("Digite a idade: ")
doenca_infec=input("Suspeito de doenças infectocontagiosa?").upper()
if idade>=65:
    print("O paciente "+ nome +" POSSUI atendimento prioritário!")
elif doenca_infec=="SIM":
    print("O paciente" + nome + " deve ser direcionado para sala de espera reservada.")
else
    print("O paciente" + nome + "NÃO possui atendimento prioritário e pode aguardar na sala comum")
