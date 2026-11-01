# Risco de Crédito e Inadimplência Bancária (Credit Scoring)

Base de dados real voltada para modelagem de **risco de crédito e predição de inadimplência (default)** em propostas de cartão de crédito e concessão de crédito pessoal.

Este diretório concentra a base de dados tratada e estruturada, pronta para futuras etapas de análise exploratória (EDA) e treinamento de modelos preditivos de classificação supervisionada.

---

## Estrutura da Pasta

- `dados/`:
  - `inadimplencia_credito.csv`: Base com 16.650 solicitações de crédito e 16 variáveis cadastrais e comportamentais.
- [download_dados.py](download_dados.py): Script Python para baixar novamente os dados brutos e refazer a padronização das colunas quando necessário.

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
| `tipo_moradia` | Tipo de residência (Casa, Apartamento, Com os pais, Aluguel) | Categórico |
| `idade` | Idade em anos | Numérico inteiro |
| `tempo_emprego_anos` | Tempo no emprego atual em anos | Numérico contínuo |
| `tem_celular` | Telefone celular cadastrado (1 = Sim, 0 = Não) | Binário |
| `tem_fone_comercial` | Telefone comercial informado (1 = Sim, 0 = Não) | Binário |
| `tem_telefone_fixo` | Telefone fixo informado (1 = Sim, 0 = Não) | Binário |
| `tem_email` | E-mail cadastrado (1 = Sim, 0 = Não) | Binário |
| `qtd_pessoas_residencia` | Total de residentes no domicílio | Numérico inteiro |
| **`inadimplente`** | **Variável Alvo:** 1 = Mau pagador (inadimplente), 0 = Bom pagador | Binário (Target) |

---

## Características da Base

- **Total de registros:** 16.650 proponentes
- **Taxa de inadimplência:** 2,34% (390 inadimplentes)
- **Desafio analítico:** Por se tratar de um problema real de concessão de crédito, a base apresenta o desbalanceamento clássico do setor financeiro, sendo ideal para aplicar técnicas de balanceamento (SMOTE, subamostragem), otimização de ponto de corte (*threshold*) e avaliação por métricas de negócio como **ROC-AUC**, **Recall**, **Precision** e estatística **KS** (*Kolmogorov-Smirnov*).

