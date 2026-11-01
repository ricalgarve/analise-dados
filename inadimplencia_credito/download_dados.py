"""
Download e padronizacao da base real de risco de credito e inadimplencia para a CredTech Brasil.
Origem: Microdados de proponentes de cartao de credito (Credit Scoring / Default).
Contem 16.650 solicitacoes com dados cadastrais, perfil socioeconomico e status de inadimplencia.
Todas as categorias descritivas sao traduzidas e padronizadas em Portugues.
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

    # Tradução de valores em inglês para português
    mapa_renda = {
        "Working": "Assalariado",
        "Commercial associate": "Empresário / Comercial",
        "State servant": "Servidor público",
        "Pensioner": "Pensionista / Aposentado",
        "Student": "Estudante"
    }

    mapa_instrucao = {
        "Secondary / secondary special": "Ensino médio",
        "Higher education": "Ensino superior",
        "Incomplete higher": "Superior incompleto",
        "Lower secondary": "Ensino fundamental",
        "Academic degree": "Pós-graduação"
    }

    mapa_estado_civil = {
        "Married": "Casado",
        "Single / not married": "Solteiro",
        "Civil marriage": "União estável",
        "Widow": "Viúvo",
        "Separated": "Separado / Divorciado"
    }

    mapa_moradia = {
        "House / apartment": "Casa / Apartamento próprio",
        "Rented apartment": "Aluguel",
        "Municipal apartment": "Habitação pública",
        "With parents": "Com os pais",
        "Co-op apartment": "Cooperativa habitacional",
        "Office apartment": "Apartamento funcional"
    }

    df["tipo_renda"] = df["tipo_renda"].map(mapa_renda).fillna(df["tipo_renda"])
    df["grau_instrucao"] = df["grau_instrucao"].map(mapa_instrucao).fillna(df["grau_instrucao"])
    df["estado_civil"] = df["estado_civil"].map(mapa_estado_civil).fillna(df["estado_civil"])
    df["tipo_moradia"] = df["tipo_moradia"].map(mapa_moradia).fillna(df["tipo_moradia"])

    # Padronização de binários e numéricos
    df["posse_veiculo"] = df["posse_veiculo"].map({"Y": "Sim", "N": "Não"}).fillna("Não")
    df["posse_imovel"] = df["posse_imovel"].map({"Y": "Sim", "N": "Não"}).fillna("Não")
    df["inadimplente"] = df["inadimplente"].astype(int)  # 1 = Inadimplente, 0 = Adimplente
    df["idade"] = df["idade"].round().astype(int)
    df["tempo_emprego_anos"] = df["tempo_emprego_anos"].round(1)
    df["qtd_pessoas_residencia"] = df["qtd_pessoas_residencia"].astype(int)

    # Salvando com codificação utf-8 explícita
    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"-> Base traduzida e salva com sucesso em: {caminho_csv}")
    print(f"-> Linhas: {len(df):,} | Colunas: {list(df.columns)}")
    print(f"-> Categorias de tipo_renda: {df['tipo_renda'].unique().tolist()}")
    print(f"-> Categorias de grau_instrucao: {df['grau_instrucao'].unique().tolist()}")
    print(f"-> Categorias de estado_civil: {df['estado_civil'].unique().tolist()}")
    print(f"-> Categorias de tipo_moradia: {df['tipo_moradia'].unique().tolist()}")

if __name__ == "__main__":
    baixar_e_padronizar()
