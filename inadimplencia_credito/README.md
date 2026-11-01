# Análise de Risco de Crédito e Inadimplência - CredTech Brasil

Estudo de caso de concessão de crédito e predição de inadimplência (*default*) para a **CredTech Brasil**, uma fintech fictícia de serviços financeiros e emissão de cartões de crédito.

O objetivo do projeto é estruturar os dados cadastrais e socioeconômicos de solicitantes de cartão para alimentar a futura esteira de decisão automatizada (*Credit Scoring*), equilibrando crescimento da base de clientes com o controle de perdas financeiras.

---

## O Desafio de Negócio

A CredTech Brasil enfrenta o dilema clássico das instituições financeiras e fintechs:
1. **Aprovar poucos clientes:** Reduz o risco de calote, mas gera perda de receita e atrito comercial.
2. **Aprovar em excesso:** Acelera o crescimento, mas aumenta o índice de perdas por não pagamento.

A base deste diretório reúne o histórico tratado de **16.650 propostas de crédito**, permitindo diagnosticar quais características do proponente aumentam o risco de inadimplência.

---

## Estrutura da Pasta

- `dados/`:
  - `inadimplencia_credito.csv`: Base tratada com 16.650 solicitações de crédito e 16 variáveis padronizadas em português.
- [download_dados.py](download_dados.py): Script Python para baixar e refazer a padronização e tradução dos dados brutos.

---

## Dicionário de Variáveis

| Atributo | Descrição | Tipo |
| :--- | :--- | :--- |
| `sexo` | Sexo biológico do solicitante (`M` ou `F`) | Categórico |
| `posse_veiculo` | Se possui veículo próprio (`Sim` ou `Não`) | Categórico |
| `posse_imovel` | Se possui imóvel próprio (`Sim` ou `Não`) | Categórico |
| `qtd_filhos` | Quantidade de filhos | Numérico inteiro |
| `tipo_renda` | Categoria profissional (Assalariado, Empresário, Servidor, etc.) | Categórico |
| `grau_instrucao` | Escolaridade (Médio, Superior, Pós-graduação, etc.) | Categórico |
| `estado_civil` | Estado civil do solicitante | Categórico |
| `tipo_moradia` | Tipo de residência (Casa própria, Aluguel, Com os pais) | Categórico |
| `idade` | Idade em anos | Numérico inteiro |
| `tempo_emprego_anos` | Tempo no emprego atual em anos | Numérico contínuo |
| `tem_celular` | Telefone celular cadastrado (1 = Sim, 0 = Não) | Binário |
| `tem_fone_comercial` | Telefone comercial informado (1 = Sim, 0 = Não) | Binário |
| `tem_telefone_fixo` | Telefone fixo informado (1 = Sim, 0 = Não) | Binário |
| `tem_email` | E-mail cadastrado (1 = Sim, 0 = Não) | Binário |
| `qtd_pessoas_residencia` | Total de residentes no domicílio | Numérico inteiro |
| **`inadimplente`** | **Variável Alvo:** 1 = Inadimplente (atraso > 60 dias), 0 = Adimplente | Binário (Target) |

---

## Características da Base

- **Total de proponentes:** 16.650 registros
- **Taxa de inadimplência observada:** 2,34% (390 casos de calote)
- **Desafio estatístico:** O forte desbalanceamento de classes reflete o cenário real do mercado de crédito brasileiro, abrindo espaço para técnicas como ajuste de limiar (*decision threshold*), amostragem estratificada, e validação por métricas de negócio (**ROC-AUC**, **Recall**, **Precision** e **KS**).
