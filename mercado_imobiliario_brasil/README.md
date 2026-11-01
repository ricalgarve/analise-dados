# Precificação de Imóveis no Brasil: Dados Reais e Machine Learning

Projeto prático de análise exploratória de dados e aprendizado de máquina supervisionado utilizando uma **base de dados real de 10.692 anúncios de aluguel** de imóveis residenciais no Brasil.

Os dados contemplam anúncios reais distribuídos entre cinco grandes centros urbanos: **São Paulo**, **Rio de Janeiro**, **Belo Horizonte**, **Porto Alegre** e **Campinas**.

---

## Estrutura da Pasta

- [analise_e_modelagem_imoveis.ipynb](analise_e_modelagem_imoveis.ipynb): Notebook Jupyter completo com:
  - Inspeção dos dados brutos e tratamento estatístico de outliers extremos comuns em anúncios reais.
  - Análise exploratória: preço médio de locação por metro quadrado por capital e correlações lineares.
  - Preparação para Machine Learning com prevenção de *Data Leakage* (exclusão de variáveis derivadas do aluguel, como seguro incêndio e total).
  - Treinamento e comparativo entre **Regressão Ridge (Linear)** e **Random Forest Regressor**.
  - Avaliação de desempenho com métricas reais: **MAE** (Erro Médio Absoluto), **RMSE** e **$R^2$**.
  - Diagnóstico de resíduos, importância de variáveis (*Feature Importance*) e simulação prática de preço de mercado para novos imóveis.
- [download_dados.py](download_dados.py): Script Python para baixar e padronizar automaticamente a base original caso queira refazer o download.
- `dados/`:
  - `imoveis_brasil.csv`: Base de dados real padronizada e traduzida para o português com 10.692 registros.

---

## Dicionário de Variáveis

| Coluna | Descrição | Tipo |
| :--- | :--- | :--- |
| `cidade` | Cidade onde o imóvel está localizado | Categórico (5 cidades) |
| `area_m2` | Área útil em metros quadrados | Numérico (`int`) |
| `quartos` | Número de quartos | Numérico (`int`) |
| `banheiros` | Número de banheiros | Numérico (`int`) |
| `vagas_garagem` | Vagas de garagem disponíveis | Numérico (`int`) |
| `andar` | Andar do imóvel (0 para casas ou térreo) | Numérico (`int`) |
| `aceita_animais` | Se aceita animais de estimação (`Sim` / `Não`) | Categórico binário |
| `mobiliado` | Se o imóvel é alugado mobiliado (`Sim` / `Não`) | Categórico binário |
| `valor_condominio` | Valor mensal da taxa de condomínio (R$) | Numérico (`int`) |
| **`valor_aluguel`** | **Variável Alvo:** Valor mensal de aluguel negociado (R$) | Numérico (`int`) |
| `valor_iptu` | Valor mensal de IPTU (R$) | Numérico (`int`) |
| `valor_seguro_incendio` | Valor do seguro incêndio anual diluído/mês (R$) | Numérico (`int`) |
| `valor_total` | Custo total mensal (aluguel + condomínio + IPTU + seguro) | Numérico (`int`) |

---

## Como Executar

Com o ambiente virtual ativo e as dependências instaladas:

```bash
jupyter lab mercado_imobiliario_brasil/analise_e_modelagem_imoveis.ipynb
```
