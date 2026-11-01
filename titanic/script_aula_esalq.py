# -*- coding: utf-8 -*-

# Minicurso: Introdução ao Machine Learning com Python (USP/ESALQ)
# Prof. Dr. Wilson Tarantin Junior

#%% Apresentação do Python e do Spyder

# Python é a linguagem de programação que vamos utilizar
# Spyder é um software (IDE) que torna o uso do Python mais simples

# Escolhendo a interface atual: Window -> Layouts da janela -> Layout Rstudio
# Escolhendo as cores da interface: Ferramentas -> Preferências

# Esta interface do Spyder divide-se em 4 grandes partes:

# 1ª Parte: script com o histórico de códigos daquele projeto ou análise
# 2ª Parte: console onde os códigos podem ser digitados e são implementados
# 3ª Parte: um ambiente onde ficam listados os objetos e os plots criados
# 4ª Parte: onde aparecem helps de pacotes e os arquivos do project atual

#%% Projects e scripts

# Para retomar um projeto: Projetos -> Abrir Projeto -> Seleciona a pasta

# Para iniciar um novo projeto, sugere-se criar uma pasta "project":
# Projetos -> Novo Projeto -> Novo diretório -> Nomear -> Localização -> Criar

# O project cria uma pasta, o que facilita a organização e o compartilhamento
# Ajuda na importação de dados para o Spyder
# Auxilia na centralização dos arquivos específicos do seu projeto

# Normalmente, utiliza-se um script para guardar o histórico das análises

# Arquivo -> Novo Arquivo

# Em seguida, é possível editar o cabeçalho e salvá-lo na pasta do project

#%% Organização e execução do script

# Importante: perceba que os textos, neste script, se iniciam com #
# Os códigos são digitados diretamente e são identificados como comandos
# Se digitarmos os textos diretamente, o Python identificará um erro
# Da mesma forma, se um comando estiver incorreto, um erro aparecerá

# O elemento #%% utilizado tem o objetivo de organizar o script
# Cria células dentro do script
# Assim, é possível executar o conteúdo daquela célula com "shift + enter"

# Para executar apenas uma linha ou uma seleção, utilize o F9

#%% Vamos conhecer algumas operações básicas no Python

# Adição
print(5 + 10)

# Note que foi utilizada a função "print"
# Tem o objetivo de mostrar no console o resultado da fórmula
# Também é possível digitar os comandos diretamente no console

# Subtração
print(20 - 6)

# Multiplicação
print(30 * 3)

# Divisão
print(200 / 10)

# Exponenciação
print(5 ** 3)

#%% Pacotes e instalação

# O Python possui uma linguagem básica com funções prontas para uso
# Entretanto, os desenvolvimentos ocorrem por meio de "pacotes"
# Tais pacotes precisam ser instalados antes do primeiro uso

# Para instalar pacotes, digite no console: pip install nome_do_pacote
# É feito para pacotes que serão utilizados, mas nunca foram instalados
# O pip é um instalador que deve ser executado diretamente na linha de comando

# Vamos instalar (executar um a um na linha de comando do console sem #):
# pip install pandas #focada em analise de dados
# pip install numpy funções matematicas
# pip install matplotlib visualização de dados em graficos
# pip install seaborn #pacote grafico

# Caso o pacote já tenha sido instalado antes, retornará a mensagem:
# "Requirement already satisfied:" e o nome do pacote

#%% Importando pacotes

# É comum definir um apelido para o pacote no momento de sua importação
# Isso é feito para facilitar a declaração de pacotes com nomes grandes
# É boa prática importar todas as bibliotecas que serão utilizadas no início

import numpy as np
import pandas as pd

#%% As funções

# Neste momento, é importante entendermos o objetivo das funções
# As funções indicam a ação que deve executada pelo script Python
# Portanto, as funções executam uma ação pré-estabelecida

# A função np.sqrt() retorna a raiz quadrada e print() printa o resultado
# A operação foi feita com uma função da biblioteca "numpy"

print(np.sqrt(144))

#%% Objetos

# O Python funciona com base em objetos
# Quando utilizamos o Spyder, os objetos ficam listados no ambiente ao lado

# Vamos iniciar armazenando as listas em novos objetos
# As listas são elementos fundamentais para a estruturação de dados

# Abaixo, vamos criar uma lista chamada "lista_numeros" que contém números
# Para criar os objetos utilizamos o indicador = para a atribuição

lista_numeros = [1, 2, 3, 4, 5]

# Podemos especificar e realizar atividades com tais elementos
# Vamos somar o elemento zero com o elemento três da lista

print(lista_numeros[0] + lista_numeros[3])

# ATENÇÃO: note que a contagem dos elementos inicia-se no zero!

# A seguir, vamos criar uma lista contendo textos
# Note que os textos são indicados entre aspas

lista_cores = ['Vermelho', 'Amarelo', 'Azul', 'Verde', 'Roxo']

print(lista_cores[3] + ' e ' + lista_cores[2])

#%% No Python, um pacote muito importante é o "pandas"

# O pandas contém ferramentas muito úteis para trabalhar com bancos de dados

# Lembrando: o primeiro passo é importar o pacote pandas (import acima)

# Vamos conhecer elementos do pandas iniciando pelas "Series"
# "Series" são objetos muito utilizados em análise de dados

#%% Numérico

# Na função a seguir, note que é comum atribuir apelidos aos pacotes "pd"
# A partir de agora, sempre que usarmos o pandas será com o nome "pd"
# Na sequência, indicamos a função "Series" que está no pacote "pd"

numeros = pd.Series([10, 20, 30, 40, 50])

print(numeros)

# dtype: int - indica que são números inteiros
# dtype: float - indica que são números com decimais

#%% Caracteres

# Vamos criar uma série com textos, isto é, com caracteres:

cores = pd.Series(['Vermelho', 'Amarelo', 'Azul', 'Verde', 'Roxo'])

print(cores)

# dtype: object - indica que são textos

#%% Lógicos

# Também poderíamos criar uma série com argumentos lógicos, True ou False

logico = pd.Series([True, False, True, False, False])

print(logico)

# dtype: bool - indica que são argumentos lógicos

#%% Importando a base de dados

# Comumente, os bancos de dados ficam armazenados em objetos do tipo DataFrame
# É um objeto fundamental do pacote "pandas"

#%% Excel

# Inicialmente, vamos importar um arquivo em Excel
# O banco de dados contém uma amostra de passageiros do Titanic

# Note que o pacote relevante para esta função é o pandas "pd"

titanic = pd.read_excel('titanic.xlsx')

#%% CSV

# Outro formato bastante comum é o (.csv)
# Vamos importar o banco de dados do Titanic que está em csv

titanic_exemplo = pd.read_csv('titanic.csv', sep=',', decimal='.')

# Os argumentos adicionados nesta função foram:
# O separador das colunas (,) e a indicação de decimais (.)

#%% Conceitos básicos de manipulação de dados

# A manipulação dos dados consiste em organizar variáveis e observações
# Na grande maioria dos casos, as bases de dados precisam ser preparadas

#%% Detalhes das variáveis do dataset

# Informações mais detalhadas das variáveis do banco de dados

titanic.info()

# Vale identificar os tipos de variáveis (Dtype)

#%% Selecionando variáveis

# Podemos armazenar a variável especificada em um novo objeto

classe = titanic['classe']

# Também poderíamos armazenar mais de uma variável em um novo objeto

selecao_var = titanic[['sobreviveu', 'classe', 'sexo']]

#%% Removendo variáveis sem uso

# Vamos excluir uma das variáveis, supondo que não vamos utilizá-la

selecao_var_sem_classe = selecao_var.drop(columns=['classe'])

selecao_var_reduzida = selecao_var.drop(columns=['classe', 'sobreviveu'])

#%% Selecionando observações

# É possível filtrar (selecionar) observações por meio de condições
# Alguns operadores úteis para realizar os filtros:

# "== igual"
# "> maior"
# ">= maior ou igual"
# "< menor"
# "<= menor ou igual"
# "!= diferente"
# "& indica e"
# "| indica ou"

# Exemplos de filtros:

# Sobreviveram (duas opções de filtros)

sobreviveu = titanic[titanic['sobreviveu'] == 'sim']
sobreviveu = titanic[titanic['sobreviveu'] != 'nao']

sobreviveu.info()

# Adultos do sexo masculino 

masc_adultos = (titanic[(titanic['sexo'] == 'masculino') & 
                        (titanic['idade'] >= 18)])

# Mulheres ou crianças

mulheres_criancas = (titanic[(titanic['sexo'] == 'feminino') |
                             (titanic['idade'] < 18)])

# Pessoas sozinhas (sem parentes)

sozinhos = (titanic[(titanic['irmaos_conjuges'] == 0) &
                    (titanic['pais_filhos'] == 0)])

# Pessoas que pagaram mais de $100 pela tarifa e embarcaram em Cherbourg

tarifas_embarque = (titanic[(titanic['valor_tarifa'] > 100) &
                            (titanic['embarque'] == 'Cherbourg')])

#%% Limpeza de dados

# Para analisar as observações com informações completas em todas as variáveis

# titanic_limpo = titanic.dropna()

# Porém, desta forma, seria uma opção muito ruim para esse banco de dados!
# Uma das variáveis (nivel_cabine) tem muitos valores faltantes
# Vamos excluir a variável e, em seguida, remover os NAs

titanic_limpo = titanic.drop(columns=['nivel_cabine']).dropna()

#%% Estatísticas descritivas: tabela de frequências

print(titanic['sobreviveu'].value_counts())
print(titanic['sobreviveu'].value_counts(normalize=True))

# Podemos utilizar os DataFrames filtrados

print(sozinhos['sobreviveu'].value_counts(normalize=True))
print(masc_adultos['sobreviveu'].value_counts(normalize=True))

#%% Estatísticas descritivas: variável quantitativa

# Contagem de observações
print("Contagem:", titanic['idade'].count())

# Média aritmética
print("Média:", titanic['idade'].mean())

# Mediana
print("Mediana:", titanic['idade'].median())

# Máximo
print("Máximo:", titanic['idade'].max())

# Mínimo
print("Mínimo:", titanic['idade'].min())

# Quartis e Percentis
print("Q1 (25%):", titanic['idade'].quantile(q = 0.25)) # Primeiro Quartil #percentil 25
print("Q3 (75%):", titanic['idade'].quantile(q = 0.75)) # Terceiro Quartil #percentil 75
# metade das observações da amostra possuem de 20 a 38 anos baseado nas medidas de posição acima.

# Variância
print("Variância:", titanic['idade'].var())

# Desvio padrão
print("Desvio padrão:", titanic['idade'].std())

# Tabela de descritivas
print(titanic['idade'].describe())
print(titanic[['idade', 'valor_tarifa']].describe())
print(titanic.describe())

#%% Estatísticas descritivas: agrupadas por meio de critério qualitativo

# Qual é o valor médio da tarifa por classe?
print(titanic[['classe', 'valor_tarifa']].groupby(by=['classe']).mean())

# Percentual de sobreviventes por sexo
print(titanic[['sobreviveu', 'sexo']].groupby('sexo')['sobreviveu'].value_counts(normalize=True))

# Percentual de sobreviventes por classe
print(titanic[['sobreviveu', 'classe']].groupby('classe')['sobreviveu'].value_counts(normalize=True))

#%% Data Visualization

# O intuito é a análise exploratória dos dados por meio dos gráficos

# Se estiver utilizando pela primeira vez, instalar as bibliotecas:
# pip install matplotlib
# pip install seaborn

# Importações dos pacotes

import matplotlib.pyplot as plt
import seaborn as sns

# Se estiver iniciando o Spyder, carregar o pandas e o numpy

import pandas as pd
import numpy as np

# Vamos importar novamente o banco de dados

titanic = pd.read_excel('titanic.xlsx')

#%% Gráfico de barras para contagem

# Vamos iniciar por uma variável qualitativa 
# Como é variável categórica, vamos criar um gráfico de contagem (countplot)
# Neste caso, o gráfico apresentará a contagem em cada categoria da variável

plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x='sobreviveu')
plt.show()

# Vamos adicionar algumas formatações ao gráfico básico

plt.figure(figsize=(10, 6))
sns.countplot(data=titanic, x='sobreviveu', color='purple')
plt.title('Titanic', fontsize=20)
plt.xlabel('Sobreviveu?', fontsize=15)
plt.ylabel('Contagem', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Adicionando as contagens para melhorar a visualização

plt.figure(figsize=(10, 6))
ax = sns.countplot(data=titanic, x='sobreviveu', color='purple')
for container in ax.containers:
    ax.bar_label(container, fontsize=12)
plt.title('Titanic', fontsize=20)
plt.xlabel('Sobreviveu?', fontsize=15)
plt.ylabel('Contagem', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Detalhando as informações entre grupos

plt.figure(figsize=(10, 6))
ax = sns.countplot(data=titanic, x='sobreviveu', hue='sexo', palette='viridis', legend=True)
for container in ax.containers:
    ax.bar_label(container, fontsize=12)
plt.title('Titanic', fontsize=20)
plt.xlabel('Sobreviveu?', fontsize=15)
plt.ylabel('Contagem', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de barras geral

# Valor médio da tarifa em cada local de embarque 

dados = titanic[['embarque', 'valor_tarifa']].groupby(by=['embarque']).mean()

# Gerando o gráfico de barras

plt.figure(figsize=(10, 6))
ax1 = sns.barplot(data=dados, x=dados.index, y='valor_tarifa', hue=dados.index, palette='bright')
for container in ax1.containers:
    ax1.bar_label(container, fmt='%.2f', padding=3, fontsize=12)
plt.title("Tarifa Média", fontsize=20)
plt.xlabel('Cidade de Embarque', fontsize=15)
plt.ylabel('Valor', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Histograma

# Vamos elaborar o histograma da idade, ou seja, variável métrica

plt.figure(figsize=(10, 6))
sns.histplot(data=titanic, x='idade', color='lightgreen')
plt.show()

# Aprimorando a apresentação do gráfico

plt.figure(figsize=(10, 6))
sns.histplot(data=titanic, x='idade', bins=range(0, 85, 5), kde=True, color='lightgreen')
plt.xlabel('Idade', fontsize=15)
plt.ylabel('Frequência', fontsize=15)
plt.xticks(ticks=np.arange(0, 85, 5), fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de pontos (scatterplot)

# Vamos elaborar um gráfico de dispersão dos pontos
# Neste caso, devemos especificar as variáveis métricas dos eixos x e y

# Suponha que o objetivo seja analisar passageiros que pagaram menos de $100

plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic[titanic['valor_tarifa'] < 100], x='idade', y='valor_tarifa')
plt.show()

# Existe alguma relação entre as variáveis? 

plt.figure(figsize=(10, 6))
sns.regplot(data=titanic[titanic['valor_tarifa'] < 100], x='idade', y='valor_tarifa')
plt.show()

# Como há variáveis nos dois eixos, podemos adicionar outras variáveis:

# Na forma de cores dos pontos ("hue")

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=titanic[titanic['valor_tarifa'] < 100],
    x='idade',
    y='valor_tarifa', 
    hue='classe',
    hue_order=['primeira', 'segunda', 'terceira']
)
plt.title('Titanic', fontsize=20)
plt.xlabel('Idade', fontsize=15)
plt.ylabel('Valor da Tarifa', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de linhas

# Vamos separar cada empresa por meio da cor da linha

dados_linha = titanic[['classe', 'valor_tarifa']].groupby(by=['classe']).mean()

plt.figure(figsize=(10, 6))
sns.lineplot(data=dados_linha, x=dados_linha.index, y='valor_tarifa', marker='o', linewidth=3, color='purple')
plt.title('Titanic', fontsize=20)
plt.xlabel('Classes', fontsize=15)
plt.ylabel('Tarifa Média', fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Boxplot

# Gráfico para representar as medidas de posição de variáveis métricas

plt.figure(figsize=(10, 6))
sns.boxplot(y=titanic['idade'], color='orange')

# Calcula as estatísticas
minimo = titanic['idade'].min()
q1 = titanic['idade'].quantile(q = 0.25)
q2 = titanic['idade'].median()
q3 = titanic['idade'].quantile(q = 0.75)
maximo = titanic['idade'].max()

# Adiciona os textos no gráfico
plt.text(0, minimo, f'Mín = {minimo:.1f}', ha='center', va='top', fontweight='bold')
plt.text(0, q1, f'Q1 = {q1:.1f}', ha='center', va='top', fontweight='bold')
plt.text(0, q2, f'Q2 = {q2:.1f}', ha='center', va='center', fontweight='bold')
plt.text(0, q3, f'Q3 = {q3:.1f}', ha='center', va='bottom', fontweight='bold')
plt.text(0, maximo, f'Máx = {maximo:.1f}', ha='center', va='bottom', fontweight='bold')

plt.title('Boxplot da Idade', fontsize=20)
plt.show()

#%% FIM!
