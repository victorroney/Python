# palavra

nome=input("Digite um funcionário:  ")
empresa=input("Digite instituição: ")
qtde_funcionários=int(input("Digite a quantidade de funcionários: "))
mediaMensalidade=float(input("Digite amédia da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui:", qtde_funcionários, "funcionarios")
print("A média da mensalidade é de :" + str(mediaMensalidade))
print("========Verifique os tipos de dados abaixo:========")
print(" tipo de dado da variavel [nome] é:",type(nome))
print("O tipo de dado da variavel [empresa] é:", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: " ,type(qtde_funcionários))
print("O tipo de dado da viraivel [mediaMensalidade] é : ",type(mediaMensalidade))
