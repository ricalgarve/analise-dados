# Mercado Imobiliário Brasileiro: Análise e Modelagem Preditiva

Projeto de análise exploratória de dados e aprendizado de máquina focado na precificação de imóveis e previsão de valor de locação (`valor_aluguel`) nas principais capitais e polos metropolitanos do Brasil.

As métricas e proporções do dataset utilizam como referência as faixas de preço por metro quadrado do índice FipeZAP para capitais como São Paulo, Rio de Janeiro, Belo Horizonte, Curitiba, Porto Alegre, Campinas, Florianópolis e Brasília.

---

## Estrutura da Pasta

- [analise_e_modelagem_imoveis.ipynb](analise_e_modelagem_imoveis.ipynb): Notebook contendo o pipeline completo:
  - Análise exploratória (distribuição de preços por m² entre capitais, correlações e impacto de comodidades).
  - Pré-processamento e codificação de variáveis categóricas (*One-Hot Encoding*).
  - Treinamento e comparação de modelos preditivos: **Regressão Linear** (baseline) e **Random Forest Regressor**.
  - Avaliação de métricas de regressão (**MAE**, **RMSE** e **$R^2$**).
  - Análise de importância de atributos (*Feature Importance*) e simulação de previsão para um novo imóvel no mercado.
- [gerar_dataset.py](gerar_dataset.py): Script Python com semente determinística para reproduzir ou parametrizar o volume de dados da base.
- `dados/`:
  - `imoveis_brasil.csv`: Base com 12.000 observações prontas para treino e validação de modelos.

---

## Dicionário de Variáveis

| Atributo | Descrição | Tipo |
| :--- | :--- | :--- |
| `cidade` | Cidade do imóvel | Texto |
| `estado` | UF correspondente | Texto |
| `bairro` | Bairro / Região | Texto |
| `tipo_imovel` | Categoria (`Apartamento`, `Casa`, `Cobertura`, `Kitnet/Studio`) | Categórico |
| `area_m2` | Área útil em metros quadrados | Numérico (`int`) |
| `quartos` | Quantidade de dormitórios | Numérico (`int`) |
| `banheiros` | Quantidade de banheiros | Numérico (`int`) |
| `vagas_garagem` | Vagas de estacionamento disponíveis | Numérico (`int`) |
| `andar` | Andar da unidade (0 para térreo ou casas) | Numérico (`int`) |
| `aceita_animais` | Se o condomínio / imóvel aceita pets (1 = Sim, 0 = Não) | Binário |
| `mobiliado` | Se o imóvel é alugado mobiliado (1 = Sim, 0 = Não) | Binário |
| `tem_piscina` | Presença de piscina no condomínio/imóvel | Binário |
| `tem_academia` | Presença de academia | Binário |
| `valor_condominio` | Custo mensal de condomínio (R$) | Numérico (`int`) |
| `valor_iptu` | IPTU mensal estimado (R$) | Numérico (`int`) |
| `valor_seguro_incendio` | Seguro incêndio obrigatório (R$) | Numérico (`int`) |
| **`valor_aluguel`** | **Variável Alvo Principal:** valor mensal de locação (R$) | Numérico (`int`) |
| `valor_venda` | Preço de mercado estimado para venda (R$) | Numérico (`int`) |
| `valor_total_mensal` | Custo total mensal (aluguel + condomínio + IPTU + seguro) | Numérico (`int`) |

---

## Como Executar

Com o ambiente virtual do repositório ativo e as dependências instaladas:

```bash
# Para rodar ou inspecionar o notebook
jupyter lab mercado_imobiliario_brasil/analise_e_modelagem_imoveis.ipynb
```
