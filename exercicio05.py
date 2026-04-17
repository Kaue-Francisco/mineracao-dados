import pandas as pd

dados = {
    "Veiculo": ["Carro A", "Carro B", "Carro C", "Carro D", "Carro E", "Carro F"],
    "Placa_Veiculo": ["ABC1234", "XYZ5678", "AB123", "DEF-456", "GHI9012", "JK 3456"]
}

df = pd.DataFrame(dados)

invalidas = df[df["Placa_Veiculo"].str.len() != 7]

print(invalidas)
