"""
Download e padronizacao do dataset real de imoveis para aluguel no Brasil.
Fonte original: Anuncios reais de locacao no Brasil (QuintoAndar / Kaggle Brazilian Houses to Rent).
Cidades cobertas: Sao Paulo, Rio de Janeiro, Belo Horizonte, Porto Alegre e Campinas.
"""

import os
import urllib.request
import io
import pandas as pd

URL_DATASET_REAL = "https://raw.githubusercontent.com/marcos-s1/Aluguel/master/houses_to_rent_v2.csv"

def baixar_e_padronizar_dados():
    pasta_destino = os.path.join(os.path.dirname(__file__), "dados")
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_csv = os.path.join(pasta_destino, "imoveis_brasil.csv")

    print(f"Baixando base real de aluguel de imoveis...")
    req = urllib.request.Request(URL_DATASET_REAL, headers={"User-Agent": "Mozilla/5.0"})
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        df_raw = pd.read_csv(io.BytesIO(resp.read()))

    print(f"-> Registros brutos baixados: {len(df_raw):,}")

    # Renomeando colunas para o portugues padrao
    mapeamento_colunas = {
        "city": "cidade",
        "area": "area_m2",
        "rooms": "quartos",
        "bathroom": "banheiros",
        "parking spaces": "vagas_garagem",
        "floor": "andar",
        "animal": "aceita_animais",
        "furniture": "mobiliado",
        "hoa (R$)": "valor_condominio",
        "rent amount (R$)": "valor_aluguel",
        "property tax (R$)": "valor_iptu",
        "fire insurance (R$)": "valor_seguro_incendio",
        "total (R$)": "valor_total"
    }
    df = df_raw.rename(columns=mapeamento_colunas).copy()

    # Tratamento de valores para consistencia
    # Andar: converter '-' (casas ou terreo) para 0
    df["andar"] = pd.to_numeric(df["andar"].replace("-", "0"), errors="coerce").fillna(0).astype(int)

    # Aceita animais: 'acept' -> 'Sim', 'not acept' -> 'Não'
    df["aceita_animais"] = df["aceita_animais"].map({"acept": "Sim", "not acept": "Não"}).fillna("Não")

    # Mobiliado: 'furnished' -> 'Sim', 'not furnished' -> 'Não'
    df["mobiliado"] = df["mobiliado"].map({"furnished": "Sim", "not furnished": "Não"}).fillna("Não")

    # Padronizacao do nome das cidades
    df["cidade"] = df["cidade"].replace({
        "São Paulo": "São Paulo",
        "So Paulo": "São Paulo"
    })

    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"-> Base real salva e padronizada em: {caminho_csv}")
    print(f"-> Colunas: {list(df.columns)}")
    print(f"-> Cidades: {df['cidade'].value_counts().to_dict()}")

if __name__ == "__main__":
    baixar_e_padronizar_dados()
