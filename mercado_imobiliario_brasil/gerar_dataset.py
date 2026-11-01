"""
Script para geracao de dataset realista do mercado imobiliario brasileiro.
Utiliza metricas de preco por m2 baseadas no historico FipeZAP para capitais brasileiras,
com correlacoes realistas entre metragem, comodos, taxas e localizacao.
"""

import os
import numpy as np
import pandas as pd

def gerar_dados(n_amostras=12000, seed=42):
    np.random.seed(seed)

    # Dados de cidades, UFs, bairros e seus multiplicadores medios de preco/m2
    cidades_config = {
        "São Paulo": {
            "uf": "SP",
            "base_m2": 10500,
            "aluguel_tx": 0.0048, # ~4.8% ao ano / 12 meses
            "bairros": {
                "Pinheiros": 1.45,
                "Moema": 1.40,
                "Itaim Bibi": 1.60,
                "Vila Mariana": 1.25,
                "Bela Vista": 1.05,
                "Santana": 0.85,
                "Tatuapé": 0.95,
                "Butantã": 0.90,
                "Lapa": 1.00
            }
        },
        "Rio de Janeiro": {
            "uf": "RJ",
            "base_m2": 9800,
            "aluguel_tx": 0.0045,
            "bairros": {
                "Leblon": 1.85,
                "Ipanema": 1.70,
                "Copacabana": 1.25,
                "Botafogo": 1.20,
                "Flamengo": 1.10,
                "Tijuca": 0.80,
                "Barra da Tijuca": 1.15,
                "Recreio": 0.85
            }
        },
        "Belo Horizonte": {
            "uf": "MG",
            "base_m2": 7600,
            "aluguel_tx": 0.0046,
            "bairros": {
                "Savassi": 1.40,
                "Lourdes": 1.45,
                "Buritis": 0.90,
                "Sion": 1.20,
                "Funcionários": 1.30,
                "Castelo": 0.85,
                "Pampulha": 0.95
            }
        },
        "Curitiba": {
            "uf": "PR",
            "base_m2": 8200,
            "aluguel_tx": 0.0044,
            "bairros": {
                "Batel": 1.50,
                "Bigorrilho": 1.30,
                "Água Verde": 1.15,
                "Centro": 0.90,
                "Portão": 0.85,
                "Cabral": 1.20
            }
        },
        "Porto Alegre": {
            "uf": "RS",
            "base_m2": 7100,
            "aluguel_tx": 0.0045,
            "bairros": {
                "Moinhos de Vento": 1.45,
                "Bela Vista": 1.35,
                "Petrópolis": 1.15,
                "Menino Deus": 1.05,
                "Centro Histórico": 0.80,
                "Mont'Serrat": 1.25
            }
        },
        "Campinas": {
            "uf": "SP",
            "base_m2": 6800,
            "aluguel_tx": 0.0047,
            "bairros": {
                "Cambuí": 1.45,
                "Taquaral": 1.20,
                "Barão Geraldo": 1.10,
                "Nova Campinas": 1.30,
                "Centro": 0.85
            }
        },
        "Florianópolis": {
            "uf": "SC",
            "base_m2": 9500,
            "aluguel_tx": 0.0045,
            "bairros": {
                "Agronômica": 1.30,
                "Itacorubi": 1.15,
                "Centro": 1.05,
                "Campeche": 1.20,
                "Jurerê": 1.60,
                "Trindade": 1.00
            }
        },
        "Brasília": {
            "uf": "DF",
            "base_m2": 8900,
            "aluguel_tx": 0.0046,
            "bairros": {
                "Asa Sul": 1.35,
                "Asa Norte": 1.30,
                "Sudoeste": 1.45,
                "Noroeste": 1.55,
                "Águas Claras": 0.95
            }
        }
    }

    cidades_lista = list(cidades_config.keys())
    # Pesos proporcionais ao tamanho de mercado
    pesos_cidades = [0.30, 0.20, 0.12, 0.10, 0.08, 0.07, 0.07, 0.06]

    registros = []

    for _ in range(n_amostras):
        cid = np.random.choice(cidades_lista, p=pesos_cidades)
        cfg = cidades_config[cid]
        uf = cfg["uf"]

        bairros = list(cfg["bairros"].keys())
        bairro = np.random.choice(bairros)
        fator_bairro = cfg["bairros"][bairro]

        # Tipo de imovel
        tipo = np.random.choice(
            ["Apartamento", "Casa", "Cobertura", "Kitnet/Studio"],
            p=[0.70, 0.18, 0.04, 0.08]
        )

        if tipo == "Kitnet/Studio":
            area = int(np.clip(np.random.normal(32, 7), 20, 48))
            quartos = 1
            banheiros = 1
            vagas = np.random.choice([0, 1], p=[0.7, 0.3])
            andar = int(np.clip(np.random.normal(7, 4), 1, 25))
        elif tipo == "Cobertura":
            area = int(np.clip(np.random.normal(240, 60), 120, 480))
            quartos = int(np.clip(np.random.normal(3.8, 0.8), 2, 5))
            banheiros = int(np.clip(quartos + np.random.choice([0, 1, 2]), 2, 6))
            vagas = int(np.clip(np.random.normal(3.2, 0.8), 2, 5))
            andar = int(np.clip(np.random.normal(18, 5), 10, 32))
        elif tipo == "Casa":
            area = int(np.clip(np.random.normal(160, 55), 60, 450))
            quartos = int(np.clip(np.random.normal(3.0, 0.8), 1, 5))
            banheiros = int(np.clip(np.random.normal(2.5, 0.9), 1, 5))
            vagas = int(np.clip(np.random.normal(2.2, 0.9), 0, 4))
            andar = 0
        else: # Apartamento
            area = int(np.clip(np.random.exponential(45) + 35, 30, 260))
            if area < 50:
                quartos = 1
            elif area < 85:
                quartos = np.random.choice([2, 3], p=[0.75, 0.25])
            elif area < 140:
                quartos = np.random.choice([2, 3, 4], p=[0.15, 0.70, 0.15])
            else:
                quartos = np.random.choice([3, 4, 5], p=[0.35, 0.50, 0.15])

            banheiros = max(1, int(np.clip(np.round(quartos * 0.85 + np.random.normal(0, 0.5)), 1, 5)))
            vagas = max(0, int(np.clip(np.round(area / 65 + np.random.normal(0, 0.5)), 0, 4)))
            andar = int(np.clip(np.random.normal(6, 4), 1, 28))

        aceita_animais = int(np.random.choice([1, 0], p=[0.78, 0.22]))
        mobiliado = int(np.random.choice([1, 0], p=[0.24, 0.76]))
        tem_piscina = int(np.random.choice([1, 0], p=[0.42 if tipo != "Casa" else 0.25, 0.58 if tipo != "Casa" else 0.75]))
        tem_academia = int(np.random.choice([1, 0], p=[0.55 if tipo in ["Apartamento", "Kitnet/Studio", "Cobertura"] else 0.05, 0.45 if tipo in ["Apartamento", "Kitnet/Studio", "Cobertura"] else 0.95]))

        # Calculo de valor de venda base por m2
        preco_m2_base = cfg["base_m2"] * fator_bairro
        fator_tipo = 1.35 if tipo == "Cobertura" else (1.10 if tipo == "Kitnet/Studio" else (0.95 if tipo == "Casa" else 1.0))
        fator_comodidades = 1.0 + (0.05 if tem_piscina else 0) + (0.04 if tem_academia else 0) + (0.08 if mobiliado else 0)
        ruido = np.random.normal(1.0, 0.08)

        preco_m2_final = preco_m2_base * fator_tipo * fator_comodidades * (1 + (vagas * 0.03)) * ruido
        valor_venda = int(np.round((area * preco_m2_final) / 1000) * 1000)

        # Calculo do aluguel baseado no valor de venda + elasticidade
        taxa_aluguel = cfg["aluguel_tx"] * (1.12 if mobiliado else 1.0) * np.random.normal(1.0, 0.07)
        valor_aluguel = int(np.round((valor_venda * taxa_aluguel) / 50) * 50)
        valor_aluguel = max(650, valor_aluguel)

        # Condominio
        if tipo == "Casa":
            valor_condominio = int(np.random.choice([0, 450, 850, 1200], p=[0.65, 0.15, 0.12, 0.08]))
        else:
            base_condo = area * np.random.uniform(7.5, 12.0)
            if tem_piscina:
                base_condo *= 1.15
            if tem_academia:
                base_condo *= 1.10
            valor_condominio = int(np.round(base_condo / 20) * 20)

        # IPTU
        valor_iptu = int(np.round((valor_venda * 0.0006) / 10) * 10)
        valor_iptu = max(30, valor_iptu)

        # Seguro incendio
        valor_seguro_incendio = int(np.round((valor_aluguel * 0.013 + area * 0.05) / 5) * 5)
        valor_seguro_incendio = max(15, valor_seguro_incendio)

        valor_total_mensal = valor_aluguel + valor_condominio + valor_iptu + valor_seguro_incendio

        registros.append({
            "cidade": cid,
            "estado": uf,
            "bairro": bairro,
            "tipo_imovel": tipo,
            "area_m2": area,
            "quartos": quartos,
            "banheiros": banheiros,
            "vagas_garagem": vagas,
            "andar": andar,
            "aceita_animais": aceita_animais,
            "mobiliado": mobiliado,
            "tem_piscina": tem_piscina,
            "tem_academia": tem_academia,
            "valor_condominio": valor_condominio,
            "valor_iptu": valor_iptu,
            "valor_seguro_incendio": valor_seguro_incendio,
            "valor_aluguel": valor_aluguel,
            "valor_venda": valor_venda,
            "valor_total_mensal": valor_total_mensal
        })

    df = pd.DataFrame(registros)
    return df

def salvar_dataset():
    pasta_destino = os.path.join(os.path.dirname(__file__), "dados")
    os.makedirs(pasta_destino, exist_ok=True)
    caminho_csv = os.path.join(pasta_destino, "imoveis_brasil.csv")

    print("Gerando dados imobiliarios do Brasil...")
    df = gerar_dados(n_amostras=12000, seed=42)

    df.to_csv(caminho_csv, index=False, encoding="utf-8")
    print(f"-> Dataset salvo com sucesso: {caminho_csv}")
    print(f"-> Total de registros: {len(df):,}")
    print(f"-> Colunas: {list(df.columns)}")
    print(f"-> Cidades: {df['cidade'].unique().tolist()}")

if __name__ == "__main__":
    salvar_dataset()
