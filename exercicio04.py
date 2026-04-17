import pandas as pd

sistemas = (
    ["Ubuntu"] * 500 +
    ["Debian"] * 400 +
    ["Armbian"] * 80 +
    ["Ubunto"] * 10 +
    ["debi4n"] * 7 +
    ["Armb1an"] * 3
)

df = pd.DataFrame({"Sistema_Operacional": sistemas})

proporcoes = df["Sistema_Operacional"].value_counts(normalize=True) * 100

raros = proporcoes[proporcoes < 5]

print("Proporcoes (%):")
print(proporcoes.round(2))
print("\nCategorias com menos de 5%:")
print(raros.round(2))
