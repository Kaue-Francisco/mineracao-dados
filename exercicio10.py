import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    'Cliente': ['A', 'B'],
    'Saldo':   [1_000_000, 1_000_010],
    'Risco':   [0.1, 0.9]
})

print("Dados originais:")
print(df.to_string(index=False))
print()

"""
Explicação:
Sem normalização, a distância entre os clientes é dominada pelo Saldo, pois a
diferença absoluta é de apenas R$10 em uma escala de ~1.000.000. Já o Risco
varia de 0.1 a 0.9 (diferença de 0.8), mas na escala bruta esse número é
minúsculo comparado ao milhão. Algoritmos baseados em distância (KNN, KMeans,
etc.) tratarão os clientes como quase idênticos porque o Saldo 'domina' o
cálculo e o Risco 'some' na comparação. O resultado é errado: Cliente B tem
risco 9x maior que Cliente A, mas a IA os confunde.
"""

scaler = MinMaxScaler()
valores_normalizados = scaler.fit_transform(df[['Saldo', 'Risco']])

df_norm = pd.DataFrame(valores_normalizados, columns=['Saldo_norm', 'Risco_norm'])
df_norm.insert(0, 'Cliente', ['A', 'B'])

print("Dados normalizados (MinMaxScaler):")
print(df_norm.to_string(index=False))
print()
print("Após normalização:")
print(f"  Diferença de Saldo normalizado:  {abs(df_norm['Saldo_norm'][1] - df_norm['Saldo_norm'][0]):.4f}  (quase zero)")
print(f"  Diferença de Risco normalizado:  {abs(df_norm['Risco_norm'][1] - df_norm['Risco_norm'][0]):.4f}  (máxima = 1.0)")
print()
print("Os R$10 de diferença se tornam irrelevantes (0.0000 na escala normalizada),")
print("enquanto a variação de risco ocupa toda a escala de 0.0 a 1.0.")
