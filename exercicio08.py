import pandas as pd

dados = {
    "Componente": ["Resistor", "Capacitor", "LED", "Transistor", "Diodo", "Fusivel"],
    "Quantidade_Estoque": [150, -20, 0.75, -1, 300, -5]
}

df = pd.DataFrame(dados)

invalidos = df[df["Quantidade_Estoque"] < 0]

print(invalidos)
