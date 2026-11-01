# Votação por Seção Eleitoral - Dados Abertos TSE

Análise exploratória dos microdados de votação por seção eleitoral das eleições gerais brasileiras, disponibilizados pelo Tribunal Superior Eleitoral (TSE).

O estudo analisa os votos na ponta (por local de votação e seção), com um recorte detalhado para os colégios eleitorais do município de **Pederneiras/SP**.

---

## Conteúdo

- [votos_secao_analise.ipynb](votos_secao_analise.ipynb): Notebook com a leitura do arquivo de seções, filtros para Pederneiras, consolidação de votos por colégio eleitoral (ex: E.E. Comendador João Chammas e demais escolas) e tabelas comparativas de percentual de votos por candidato. O notebook está salvo com todas as tabelas e saídas calculadas para visualização direta no GitHub.
- `leiame.pdf`: Manual e dicionário de dados oficial fornecido pelo TSE, detalhando cada coluna e código presente no dataset de resultados por seção.

---

## Base de Dados

O arquivo completo de votação por seção do Brasil (`votacao_secao_2026_BR.csv`) possui mais de **1 GB** descompactado, excedendo o limite de tamanho de arquivos do GitHub (100 MB), por isso não é versionado diretamente aqui.

Para reproduzir a leitura a partir da base bruta:
1. Acesse o portal de [Dados Abertos do TSE](https://dadosabertos.tse.jus.br/).
2. Baixe o arquivo de votação por seção eleitoral desejado.
3. Extraia o arquivo CSV nesta pasta mantendo o nome `votacao_secao_2026_BR.csv` (ou altere o caminho correspondente na primeira célula do notebook).

