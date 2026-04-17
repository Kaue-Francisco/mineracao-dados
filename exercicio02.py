import pandas as pd

dados = {
    "Produto": ["Teclado", "Mouse", "Monitor", "Cabo HDMI", "Pendrive"],
    "Data_Compra": ["2024-01-10", "2024-02-05", "2024-03-01", "2024-04-15", "2024-05-20"],
    "Data_Entrega": ["2024-01-15", "2024-02-01", "2024-03-10", "2024-04-10", "2024-05-25"]
}

df = pd.DataFrame(dados)

df["Data_Compra"] = pd.to_datetime(df["Data_Compra"])
df["Data_Entrega"] = pd.to_datetime(df["Data_Entrega"])

erros = df[df["Data_Entrega"] < df["Data_Compra"]]

print(erros)
