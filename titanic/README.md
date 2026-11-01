# Análise do Dataset Titanic (USP/ESALQ)

Material e análises práticas baseados no minicurso de Introdução ao Machine Learning com Python da USP/ESALQ, ministrado pelo Prof. Dr. Wilson Tarantin Junior.

O foco aqui é a análise exploratória de dados (EDA), estatística descritiva e visualização gráfica com Pandas, Matplotlib e Seaborn a partir do clássico dataset de passageiros do Titanic.

---

## Arquivos

- [titanic_analise.ipynb](titanic_analise.ipynb): Notebook com todo o passo a passo da análise, incluindo limpeza, tabelas de contingência e gráficos comentados.
- [script_aula_esalq.py](script_aula_esalq.py): Script Python com blocos de código (`#%%`) para execução no Spyder ou no modo interativo do VS Code.
- [titanic.xlsx](titanic.xlsx): Base de dados em Excel (com colunas e categorias traduzidas para o português).
- [titanic.csv](titanic.csv): Base de dados em formato CSV (separador `,` e decimais `.`).

---

## Variáveis do Dataset

| Coluna | Descrição | Valores / Tipo |
| :--- | :--- | :--- |
| `sobreviveu` | Se o passageiro sobreviveu | `'sim'`, `'nao'` |
| `classe` | Classe do bilhete | `'primeira'`, `'segunda'`, `'terceira'` |
| `sexo` | Sexo do passageiro | `'masculino'`, `'feminino'` |
| `idade` | Idade em anos | Numérico contínuo (`float`) |
| `irmaos_conjuges` | Quantidade de irmãos/cônjuges a bordo | Inteiro (`int`) |
| `pais_filhos` | Quantidade de pais/filhos a bordo | Inteiro (`int`) |
| `valor_tarifa` | Valor pago pela passagem em dólares | Numérico contínuo (`float`) |
| `embarque` | Porto de embarque | `'Cherbourg'`, `'Southampton'`, `'Queenstown'` |
| `nivel_cabine` | Nível da cabine ocupada | Categórico |

---

## O que foi explorado

1. **Manipulação de dados com Pandas**: seleção, filtros condicionais, tratamento de nulos (`dropna`) e exclusão de colunas irrelevantes.
2. **Estatística descritiva**: tabelas de frequência (absoluta e relativa), medidas de posição (média, mediana, quartis) e dispersão (desvio padrão, variância), além de análises estratificadas com `groupby`.
3. **Visualizações**:
   - Gráficos de barras e contagem (`countplot`, `barplot`) destacando sobrevivência por classe e sexo.
   - Histograma e curva de densidade (`histplot` + KDE) para distribuição de idades.
   - Gráficos de dispersão (`scatterplot`, `regplot`) e boxplots detalhados com marcações de quartis e outliers.
