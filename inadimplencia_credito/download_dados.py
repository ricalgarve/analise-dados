"""
Download e padronizacao da base real de risco de credito e inadimplencia.
Origem: Microdados de proponentes de cartao de credito (Credit Scoring / Default).
Contem 16.650 solicitacoes com dados cadastrais, perfil socioeconomico e status de inadimplencia.
"""

import os
import urllib.request
import io
import pandas as pd

URL_FONTE = "https://raw.githubusercontent.com/rhatiro/Credit-score/main/demo01.csv"

def baixar_e_padronizar():
    pasta_destino = os.path.join(os.path.dirname(__file__), "dados")
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_csv = os.path.join(pasta_destino, "inadimplencia_credito.csv")

    print("Baixando base real de inadimplência de crédito...")
    req = urllib.request.Request(URL_FONTE, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        df = pd.read_csv(io.BytesIO(resp.read()))

    print(f"-> Registros recebidos: {len(df):,}")

    # Renomeando e padronizando variáveis
    mapeamento_colunas = {
        "sexo": "sexo",
        "posse_de_veiculo": "posse_veiculo",
        "posse_de_imovel": "posse_imovel",
        "qtd_filhos": "qtd_filhos",
        "tipo_renda": "tipo_renda",
        "educacao": "grau_instrucao",
        "estado_civil": "estado_civil",
        "tipo_residencia": "tipo_moradia",
        "idade": "idade",
        "tempo_emprego": "tempo_emprego_anos",
        "possui_celular": "tem_celular",
        "possui_fone_comercial": "tem_fone_comercial",
        "possui_fone": "tem_telefone_fixo",
        "possui_email": "tem_email",
        "qt_pessoas_residencia": "qtd_pessoas_residencia",
        "mau": "inadimplente"
    }
    df = df.rename(columns=mapeamento_colunas).copy()

    # Mapeamentos para clareza
    df["posse_veiculo"] = df["posse_veiculo"].map({"Y": "Sim", "N": "Não"}).fillna("Não")
    df["posse_imovel"] = df["posse_imovel"].map({"Y": "Sim", "N": "Não"}).fillna("Não")
    df["inadimplente"] = df["inadimplente"].astype(int)  # 1 = Inadimplente, 0 = Adimplente
    df["idade"] = df["idade"].round().astype(int)
    df["tempo_emprego_anos"] = df["tempo_emprego_anos"].round(1)
    df["qtd_pessoas_residencia"] = df["qtd_pessoas_residencia"].astype(int)

    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"-> Base salva com sucesso em: {caminho_csv}")
    print(f"-> Linhas: {len(df):,} | Colunas: {list(df.columns)}")
    print(f"-> Taxa de inadimplentes: {df['inadimplente'].mean()*100:.2f}% ({df['inadimplente'].sum()} casos)")

if __name__ == "__main__":
    baixar_e_padronizar()

