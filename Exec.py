from Pessoa import Pessoa
from AlgoritmoGenetico import AlgoritmoGenetico
import matplotlib.pyplot as plt

lista_pessoas = []

#nome, idade, 
#institucionalizada, pcd, trabalhaNaAreaDeSaude, possuiComorbidades, 
#trabalhaNaAreaDaEducacao, trabalhaNaAreaDeSeguranca, trabalhaNaAreaDeTransporte
lista_pessoas.append(Pessoa("Lorenzo", 50, False, False, False, False, False, False, True))
lista_pessoas.append(Pessoa("Mario", 50, True, True, False, False, False, False, False))
lista_pessoas.append(Pessoa("João", 30, False, False, True, False, False, False, False))
lista_pessoas.append(Pessoa("Davi", 65, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Pedro", 50, False, True, False, False, False, False, False))
lista_pessoas.append(Pessoa("Jael", 50, False, False, False, False, True, False, False))
lista_pessoas.append(Pessoa("Maria", 65, True, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Lívia", 40, False, True, False, False, False, False, False))
lista_pessoas.append(Pessoa("Bernardo", 75, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Alice", 70, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Edson", 50, False, False, False, False, False, True, False))
lista_pessoas.append(Pessoa("Helena", 60, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Isabela", 60, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Pedro", 50, False, False, False, True, False, False, False))
lista_pessoas.append(Pessoa("Jonas", 40, False, False, False, True, False, False, False))
lista_pessoas.append(Pessoa("Arthur", 80, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Heitor", 95, False, False, False, False, False, False, False))
lista_pessoas.append(Pessoa("Marcos", 50, False, False, False, False, False, False, True))
lista_pessoas.append(Pessoa("Arnaldo", 75, True, False, False, False, False, False, False))

for pessoa in lista_pessoas:
    print("Nome: ", pessoa.nome, " - Pontuação", pessoa.pontuacao)

#Listas contendo os dados da solução encontrada
espacos = 0
pontuacoes = []
nomes = []
for pessoa in lista_pessoas:
    espacos += 1
    pontuacoes.append(pessoa.pontuacao)
    nomes.append(pessoa.nome)

resposta = 's'#input("Deseja executar com as variáveis padrões?(S/N) ").lower()
if (resposta == 'n'):
    limite = int(input("Limite de pessoas: "))#10
    tamanho_populacao = int(input("Tamanho da população: "))#20
    taxa_mutacao = float(input("Taxa de mutação (Valores sugeridos: 0.01, 0.001): "))#0.01
    numero_geracoes = int(input("Número de gerações: "))#100
else:
    limite = 10
    tamanho_populacao = 20
    taxa_mutacao =0.01
    numero_geracoes = 200#100


ag = AlgoritmoGenetico(tamanho_populacao)
resultado = ag.resolver(taxa_mutacao, numero_geracoes, pontuacoes, espacos, limite)
for i in range(espacos):
    if resultado[i] == '1':
        print("Nome: %s - Pontuação: %s " % (lista_pessoas[i].nome,
                                       lista_pessoas[i].pontuacao))
            
    
plt.plot(ag.lista_solucoes)
plt.title("Acompanhamento dos valores")
plt.show()