import pandas as pd

ANO_ATUAL = 2026

dados = {
    "Aluno": ["Alice", "Bruno", "Carla", "Diego", "Elena"],
    "Ano_Nascimento": [2000, 1998, 2003, 1995, 2001],
    "Idade_Declarada": [26, 28, 20, 35, 24]
}

df = pd.DataFrame(dados)

df["Idade_Real"] = ANO_ATUAL - df["Ano_Nascimento"]

contradicoes = df[df["Idade_Real"] != df["Idade_Declarada"]]

print(contradicoes)
