from sklearn.preprocessing import MinMaxScaler

# Cálculo manual: (valor - min) / (max - min)
# (200 - 100) / (500 - 100) = 100 / 400 = 0.25
valor_manual = (200 - 100) / (500 - 100)
print(f"Cálculo manual para 200 psi: {valor_manual:.4f}")

pressao = [[100], [200], [500]]

scaler = MinMaxScaler()
resultado = scaler.fit_transform(pressao)

print("\nResultado do MinMaxScaler:")
for p, r in zip(pressao, resultado):
    print(f"  {p[0]} psi -> {r[0]:.4f}")

print(f"\nO valor normalizado de 200 psi pelo MinMaxScaler bate com o cálculo manual: {resultado[1][0]:.4f} == {valor_manual:.4f}")
