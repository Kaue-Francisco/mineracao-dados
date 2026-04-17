import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    'idade':           [20, 22, 21, 23, 19, 150],
    'horas_estudo':    [10, 12,  9, 11, 10,   8],
    'nota_final':      [7.5, 8.0, 7.0, 8.5, 7.2, 6.0]
})

modelo = IsolationForest(contamination=0.17, random_state=42)
df['Outlier'] = modelo.fit_predict(df)

print("DataFrame completo:")
print(df.to_string())

print("\nLinha(s) detectada(s) como anomalia (Outlier == -1):")
print(df[df['Outlier'] == -1].to_string())
