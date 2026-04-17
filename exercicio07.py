import pandas as pd

dados = {
    "Paciente": ["Joao", "Maria", "Carlos", "Ana", "Pedro", "Lucia"],
    "Altura_Metros": [1.75, 170.0, 1.60, 0.30, 1.82, 2.90]
}

df = pd.DataFrame(dados)

impossiveis = df[(df["Altura_Metros"] < 0.5) | (df["Altura_Metros"] > 2.5)]

print(impossiveis)
