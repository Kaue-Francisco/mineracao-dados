from scipy.stats import zscore

temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]
scores = zscore(temp)

print("Anomalias detectadas (Z-Score > 2.5):")
for t, z in zip(temp, scores):
    if z > 2.5:
        print(f"  Temperatura: {t}°C | Z-Score: {z:.2f}")
