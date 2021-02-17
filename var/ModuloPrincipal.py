from var.IdentificacaoDeFuncoes import *

minhaLista=[]
print("Preenchimento")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)
print("Alteração")
depreciarPorNome(minhaLista, 20)

print("Excluído")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)

