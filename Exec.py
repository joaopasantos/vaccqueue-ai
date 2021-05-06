from Pessoa import Pessoa
from AlgoritmoGenetico import AlgoritmoGenetico
import matplotlib.pyplot as plt

lista_pessoas = []
# nome, idade, institucionalizada, pcd, trabalhaNaAreaDeSaude, possuiComorbidades, trabalhaNaAreaDaEducacao, trabalhaNaAreaDeSeguranca, trabalhaNaAreaDeTransporte
lista_pessoas.append(Pessoa("Maria", 65, True, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Mario", 50, True, True, False, False, False, False, False))
lista_pessoas.append(Pessoa("João", 30, False, False, True, False, False, False, False))
lista_pessoas.append(Pessoa("Zé1", 80, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Zé2", 75, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Zé3", 70, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Zé4", 65, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Zé5", 60, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Zé5", 60, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Pedro", 50, False, False, False, True, False, False, False))
lista_pessoas.append(Pessoa("Jonas", 40, False, False, False, True, False, False, False))
lista_pessoas.append(Pessoa("Pedro", 50, False, True, False, False, False, False, False))
lista_pessoas.append(Pessoa("Jael", 50, False, False, False, False, True, False, False))
lista_pessoas.append(Pessoa("Edson", 50, False, False, False, False, False, True, False))
lista_pessoas.append(Pessoa("Marcos", 50, False, False, False, False, False, False, True))

for pessoa in lista_pessoas:
    print("Nome: ", pessoa.nome, " - Pontuação", pessoa.pontuacao)

#Listas contendo os dados da solução encontrada
pontuacoes = []
nomes = []
for pessoa in lista_pessoas:
    pontuacoes.append(pessoa.pontuacao)
    nomes.append(pessoa.nome)
limite = 14

tamanho_populacao = 20
taxa_mutacao = 0.01
numero_geracoes = 100
ag = AlgoritmoGenetico(tamanho_populacao)
resultado = ag.resolver(taxa_mutacao, numero_geracoes, pontuacoes, limite)
for i in range(limite):
    if resultado[i] == '1':
        print("Nome: %s - Pontuação: %s " % (lista_pessoas[i].nome,
                                       lista_pessoas[i].pontuacao))
            
    
plt.plot(ag.lista_solucoes)
plt.title("Acompanhamento dos valores")
plt.show()

  
