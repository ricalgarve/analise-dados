# Análise de Dados em Python

Repositório com estudos práticos e projetos de análise de dados, estatística descritiva e visualização em Python. 

Os projetos utilizam bases de dados reais — tanto públicas quanto acadêmicas — cobrindo áreas como saúde pública, vigilância epidemiológica, dados eleitorais e introdução a machine learning.

---

## Projetos

- **[infogripe_fiocruz/](infogripe_fiocruz/)**: Vigilância epidemiológica de Síndrome Respiratória Aguda Grave (SRAG) e circulação de vírus respiratórios (SARS-CoV-2, Influenza A/B, VSR, Rinovírus) com dados oficiais do InfoGripe (Fiocruz / Ministério da Saúde). Inclui script para download automatizado das séries temporais e visualizações de evolução temporal e comparações por UF.
- **[expectativa_vida_sus/](expectativa_vida_sus/)**: Estudo demográfico de mortalidade e expectativa de vida no Brasil utilizando microdados do Sistema de Informações sobre Mortalidade (SIM/DATASUS) integrados via biblioteca `PySUS` e projeções populacionais do IBGE.
- **[titanic/](titanic/)**: Análise exploratória e visualização de dados baseada no clássico dataset de passageiros do Titanic, seguindo a estrutura do minicurso da USP/ESALQ ministrado pelo Prof. Dr. Wilson Tarantin Junior. Aborda estatística descritiva completa, tabelas de contingência e gráficos com Seaborn e Matplotlib.
- **[votacao_presidente_2026_secao/](votacao_presidente_2026_secao/)**: Análise de microdados eleitorais disponibilizados pelo TSE, avaliando votos na ponta (por seção e colégio eleitoral) com foco no município de Pederneiras/SP.

---

## Tecnologias e Bibliotecas

- **Linguagem:** Python (3.11+)
- **Manipulação e Análise:** Pandas, NumPy, OpenPyXL
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
