import pandas as pd

dados = {
    "Sensor_ID": [1, 2, 3, 4, 5, 6, 7],
    "Temperatura_C": ["23.5", "falha_sinal", "19.0", "falha_sinal", "27.3", "erro", "21.1"]
}

df = pd.DataFrame(dados)

df["Temperatura_C"] = pd.to_numeric(df["Temperatura_C"], errors="coerce")

falhas = df[df["Temperatura_C"].isna()]

print(falhas)
