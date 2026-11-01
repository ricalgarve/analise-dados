import os
import urllib.request
import pandas as pd

# URLs oficiais dos dados consolidados do InfoGripe (Fiocruz / MS)
URLS = {
    "virus_brasil_estados": "https://raw.githubusercontent.com/infogripe/Boletim_InfoGripe/main/Dados/InfoGripe/estados_e_pais_serie_estimativas_virus_sem_filtro_febre.csv",
    "faixa_etaria_brasil_estados": "https://raw.githubusercontent.com/infogripe/Boletim_InfoGripe/main/Dados/InfoGripe/estados_e_pais_serie_estimativas_fx_etaria_sem_filtro_febre.csv",
    "alerta_semanal": "https://raw.githubusercontent.com/infogripe/Boletim_InfoGripe/main/Dados/InfoGripe/tabela_de_alerta_sem_filtro_febre.csv"
}

def baixar_dados():
    diretorio_destino = os.path.join(os.path.dirname(__file__), "dados")
    os.makedirs(diretorio_destino, exist_ok=True)
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for nome, url in URLS.items():
        caminho_arquivo = os.path.join(diretorio_destino, f"{nome}.csv")
        print(f"Baixando {nome} de: {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response, open(caminho_arquivo, "wb") as out_file:
                out_file.write(response.read())
            print(f"-> Salvo com sucesso: {caminho_arquivo}")
        except Exception as e:
            print(f"-> Erro ao baixar {nome}: {e}")

if __name__ == "__main__":
    baixar_dados()
