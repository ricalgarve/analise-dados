# Vigilância de Vírus Respiratórios e SRAG (InfoGripe / Fiocruz)

Projeto de análise epidemiológica de casos de Síndrome Respiratória Aguda Grave (SRAG) e monitoramento laboratorial de vírus respiratórios no Brasil, baseado nos dados públicos do sistema InfoGripe (Fiocruz, FGV EMap e Ministério da Saúde).

---

## O que é o InfoGripe?

O InfoGripe monitora notificações do SIVEP-Gripe e aplica correções estatísticas (*nowcasting*) para estimar a incidência real recente de infecções respiratórias graves, compensando o atraso habitual entre a ocorrência dos primeiros sintomas e a inserção do laudo no sistema de saúde.

### Patógenos Acompanhados

- **SARS-CoV-2**: COVID-19
- **Influenza A e B**: Gripe comum e variantes (H1N1, H3N2, etc.)
- **VSR**: Vírus Sincicial Respiratório (principal responsável por quadros graves em crianças menores de 2 anos)
- **Rinovírus** e **Metapneumovírus**

---

## Arquivos e Estrutura

- [analise_infogripe.ipynb](analise_infogripe.ipynb): Notebook com análise das séries temporais nacionais e estaduais, gráficos de evolução por vírus e sazonalidade.
- [download_dados.py](download_dados.py): Script para baixar ou atualizar as bases de dados diretamente do repositório oficial da Fiocruz no GitHub.
- `dados/`: Pasta com os dados offline para consulta imediata:
  - `virus_brasil_estados.csv`: Séries estimadas de casos por vírus no Brasil e por UF.
  - `faixa_etaria_brasil_estados.csv`: Séries discriminadas por idade.
  - `alerta_semanal.csv`: Situação e nível de atividade de transmissão recente por estado.

---

## Como Atualizar os Dados

Para sincronizar com as séries mais recentes disponibilizadas semanalmente pela Fiocruz:

```bash
python download_dados.py
```
