"""
Download e padronizacao do dataset 'Give Me Some Credit' do Kaggle.
Origem: Competicao Kaggle (kaggle.com/competitions/GiveMeSomeCredit)
150.000 registros reais de historico de credito norte-americano (Bureau of Credit).
Traduzido e padronizado em Portugues para uso no estudo da CredTech Brasil.
"""

import os
import urllib.request
import io
import pandas as pd

URL_FONTE = "https://raw.githubusercontent.com/mesfind/datasets/master/cs-training.csv"

def baixar_e_padronizar():
    pasta_destino = os.path.join(os.path.dirname(__file__), "dados")
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_csv = os.path.join(pasta_destino, "give_me_some_credit.csv")

    print("Baixando dataset Give Me Some Credit (Kaggle)...")
    req = urllib.request.Request(URL_FONTE, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        df = pd.read_csv(io.BytesIO(resp.read()), sep=";", index_col=0)

    print(f"-> Registros brutos: {len(df):,}")

    # Renomeando colunas para o portugues
    mapeamento_colunas = {
        "SeriousDlqin2yrs": "inadimplente_2anos",
        "RevolvingUtilizationOfUnsecuredLines": "utilizacao_credito_rotativo",
        "age": "idade",
        "NumberOfTime30-59DaysPastDueNotWorse": "atrasos_30_59_dias",
        "DebtRatio": "indice_endividamento",
        "MonthlyIncome": "renda_mensal",
        "NumberOfOpenCreditLinesAndLoans": "qtd_linhas_credito_abertas",
        "NumberOfTimes90DaysLate": "atrasos_acima_90_dias",
        "NumberRealEstateLoansOrLines": "qtd_financiamentos_imoveis",
        "NumberOfTime60-89DaysPastDueNotWorse": "atrasos_60_89_dias",
        "NumberOfDependents": "qtd_dependentes"
    }
    df = df.rename(columns=mapeamento_colunas).copy()

    # Informacoes pre-tratamento
    print(f"-> Valores nulos antes do tratamento:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"\n-> Dataset salvo em: {caminho_csv}")
    print(f"-> Linhas: {len(df):,} | Colunas: {list(df.columns)}")
    print(f"-> Taxa de inadimplencia (2 anos): {df['inadimplente_2anos'].mean()*100:.2f}% ({df['inadimplente_2anos'].sum():,} casos)")

if __name__ == "__main__":
    baixar_e_padronizar()
