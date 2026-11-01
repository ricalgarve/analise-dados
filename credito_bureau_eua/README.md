# Give Me Some Credit - Histórico de Crédito (Kaggle)

Base de dados proveniente da competição oficial do Kaggle **[Give Me Some Credit](https://www.kaggle.com/competitions/GiveMeSomeCredit)**, com **150.000 registros reais** de histórico de crédito de consumidores norte-americanos obtidos de um bureau de crédito.

O objetivo da competição era construir um modelo capaz de prever com dois anos de antecedência se um tomador de crédito entraria em situação de grave inadimplência — definida como **atraso superior a 90 dias** em pelo menos uma de suas obrigações financeiras.

---

## Estrutura da Pasta

- [analise_credito_bureau.ipynb](analise_credito_bureau.ipynb): Notebook Jupyter com o carregamento da base (local ou GitHub), inspeção de tipagem, diagnóstico de dados ausentes e distribuição da inadimplência.
- `dados/`:
  - `give_me_some_credit.csv`: Base com 150.000 registros já traduzida e padronizada em português.
- [download_dados.py](download_dados.py): Script Python para baixar e padronizar novamente a base a partir da fonte pública.

---

## Dicionário de Variáveis

| Atributo | Descrição Original (Kaggle) | Tipo |
| :--- | :--- | :--- |
| **`inadimplente_2anos`** | **Variável Alvo:** 1 = Entrou em inadimplência grave nos 2 anos seguintes, 0 = Não | Binário (Target) |
| `utilizacao_credito_rotativo` | Saldo total de linhas rotativas (cartão de crédito, cheque especial) dividido pelo limite total | Numérico contínuo |
| `idade` | Idade do tomador de crédito em anos | Numérico inteiro |
| `atrasos_30_59_dias` | Nº de vezes que o pagamento ficou 30 a 59 dias em atraso nos últimos 2 anos | Numérico inteiro |
| `indice_endividamento` | Pagamentos mensais de dívidas (amortização + juros + pensões) dividido pela renda mensal bruta | Numérico contínuo |
| `renda_mensal` | Renda mensal bruta declarada (em dólares) — **29.731 valores ausentes** | Numérico |
| `qtd_linhas_credito_abertas` | Número de empréstimos e linhas de crédito abertas (ex: cartões, financiamentos, cheque) | Numérico inteiro |
| `atrasos_acima_90_dias` | Nº de vezes que o pagamento ficou 90 ou mais dias em atraso | Numérico inteiro |
| `qtd_financiamentos_imoveis` | Nº de empréstimos ou linhas de crédito imobiliário (ex.: hipoteca, home equity) | Numérico inteiro |
| `atrasos_60_89_dias` | Nº de vezes que o pagamento ficou 60 a 89 dias em atraso nos últimos 2 anos | Numérico inteiro |
| `qtd_dependentes` | Nº de dependentes na família (excluindo o próprio solicitante) — **3.924 valores ausentes** | Numérico inteiro |

---

## Características da Base

- **Total de registros:** 150.000 consumidores
- **Taxa de inadimplência observada:** 6,68% (10.026 casos)
- **Valores ausentes documentados:**
  - `renda_mensal`: 29.731 registros sem informação (~19,8%)
  - `qtd_dependentes`: 3.924 registros sem informação (~2,6%)
- **Fonte:** Competição Kaggle — [Give Me Some Credit (2011)](https://www.kaggle.com/competitions/GiveMeSomeCredit)
- **Desafio analítico:** Volume elevado (150k), desbalanceamento de classes real, outliers expressivos em variáveis de utilização e endividamento, e a necessidade de estratégia de imputação de dados ausentes tornam esta base um benchmark clássico para modelos de *Credit Scoring* com **Regressão Logística**, **Gradient Boosting** e **XGBoost**.

