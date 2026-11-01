# Expectativa de Vida e Mortalidade no Brasil (DATASUS / PySUS)

Estudo de demografia e saúde pública com foco no cálculo de tábuas de vida e taxas de mortalidade no Brasil, utilizando os microdados oficiais do Sistema de Informações sobre Mortalidade (SIM/DATASUS) e projeções populacionais do IBGE.

---

## Estrutura

- [analise_expectativa_vida.ipynb](analise_expectativa_vida.ipynb): Notebook com o roteiro de extração dos microdados via FTP do DataSUS, padronização da variável de idade (que possui codificação própria no DATASUS para horas, dias, meses e anos) e estruturação dos dados para cálculo de tábuas de vida.

---

## Fontes de Dados

- **SIM (DATASUS)**: Microdados de declarações de óbito por município, causa (CID-10), faixa etária e sexo.
- **IBGE**: Censos e estimativas anuais de população residente por faixa etária e município.
- **PySUS**: Biblioteca utilizada para download direto dos arquivos oficiais sem necessidade de intervenção manual no portal do governo.
