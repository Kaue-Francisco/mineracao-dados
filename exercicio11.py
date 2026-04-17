from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()
resultado = scaler.fit_transform(temps)

print("Normalização de temperaturas:")
for t, r in zip(temps, resultado):
    print(f"  {t[0]:>4}°C  ->  {r[0]:.4f}")

print()
print(f"O valor 0°C foi normalizado para: {resultado[2][0]:.4f}")
print()
print("""Explicação:
O 0°C NÃO continua sendo 0 após a normalização.
O MinMaxScaler aplica: (valor - min) / (max - min)
  -> (0 - (-20)) / (20 - (-20)) = 20 / 40 = 0.5

O zero da escala normalizada (0.0) representa o menor valor original, que é -20°C.
O um (1.0) representa o maior valor original, que é 20°C.
O zero original (0°C) agora está no meio da escala normalizada (0.5),
pois é exatamente o ponto médio entre -20°C e 20°C.""")
