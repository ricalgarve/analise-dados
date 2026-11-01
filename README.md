# Análise de Dados em Python

Repositório com estudos práticos e projetos de análise de dados, estatística descritiva, visualização e modelagem preditiva (Machine Learning) em Python. 

Os projetos utilizam bases de dados reais e aplicadas ao contexto brasileiro — cobrindo áreas como mercado imobiliário, saúde pública, vigilância epidemiológica, dados eleitorais e introdução a machine learning.

---

## Projetos

- **[inadimplencia_credito/](inadimplencia_credito/)**: Estudo de risco de crédito e predição de inadimplência da **CredTech Brasil** (fintech fictícia). Base de dados com 16.650 solicitações de cartão de crédito e crédito pessoal, abordando variáveis socioeconômicas, estabilidade de emprego e desbalanceamento realista de classes (2,34% de taxa de inadimplência).
- **[credito_bureau_eua/](credito_bureau_eua/)**: Dataset da competição Kaggle *Give Me Some Credit* com 150.000 registros reais de histórico de crédito de consumidores norte-americanos. Inclui variáveis de comportamento de pagamento, utilização de crédito rotativo e endividamento para modelagem preditiva de inadimplência grave (atraso > 90 dias).
- **[mercado_imobiliario_brasil/](mercado_imobiliario_brasil/)**: Análise e precificação imobiliária preditiva baseada em 10.692 anúncios reais de locação em São Paulo, Rio de Janeiro, Belo Horizonte, Porto Alegre e Campinas. Inclui pipeline completo de Machine Learning com tratamento de outliers, engenharia de variáveis (sem vazamento de dados), comparação entre Regressão Ridge e Random Forest, métricas de regressão (MAE, RMSE, $R^2$) e simulação de precificação de mercado.
- **[infogripe_fiocruz/](infogripe_fiocruz/)**: Vigilância epidemiológica de Síndrome Respiratória Aguda Grave (SRAG) e circulação de vírus respiratórios (SARS-CoV-2, Influenza A/B, VSR, Rinovírus) com dados oficiais do InfoGripe (Fiocruz / Ministério da Saúde). Inclui script para download automatizado das séries temporais e visualizações de evolução temporal e comparações por UF.
- **[expectativa_vida_sus/](expectativa_vida_sus/)**: Estudo demográfico de mortalidade e expectativa de vida no Brasil utilizando microdados do Sistema de Informações sobre Mortalidade (SIM/DATASUS) integrados via biblioteca `PySUS` e projeções populacionais do IBGE.
- **[titanic/](titanic/)**: Análise exploratória e visualização de dados baseada no clássico dataset de passageiros do Titanic, seguindo a estrutura do minicurso da USP/ESALQ ministrado pelo Prof. Dr. Wilson Tarantin Junior. Aborda estatística descritiva completa, tabelas de contingência e gráficos com Seaborn e Matplotlib.
- **[votacao_presidente_2026_secao/](votacao_presidente_2026_secao/)**: Análise de microdados eleitorais disponibilizados pelo TSE, avaliando votos na ponta (por seção e colégio eleitoral) com foco no município de Pederneiras/SP.

---

## Tecnologias e Bibliotecas

- **Linguagem:** Python (3.11+)
- **Manipulação e Análise:** Pandas, NumPy, OpenPyXL
- **Machine Learning:** Scikit-Learn
- **Visualização Gráfica:** Matplotlib, Seaborn
- **Dados de Saúde Pública:** PySUS, PyArrow, Fastparquet
- **Ambiente de Trabalho:** Jupyter Notebook / VS Code

---

## Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/ricalgarve/analise-dados.git
cd analise-dados
```

### 2. Configurar o ambiente virtual

Se estiver no Windows, você pode usar os scripts que já cuidam de criar a `.venv`, ativá-la e instalar os pacotes:

- **PowerShell:**
  ```powershell
  .\activate_env.ps1
  ```
- **CMD:**
  ```cmd
  activate_env.bat
  ```

Ou fazer o processo manual:

```bash
python -m venv .venv

# No Windows:
.venv\Scripts\activate

# No Linux/Mac:
source .venv/bin/activate

# Instalar dependências:
pip install -r requirements.txt
```

### 3. Rodar os notebooks

Abra o diretório no VS Code ou execute o Jupyter:

```bash
jupyter lab
```

Ao abrir qualquer `.ipynb`, selecione o kernel correspondente ao ambiente virtual (`.venv`).
