from scipy.stats import zscore

voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]
scores = zscore(voltagem)

print("Monitoramento de voltagem:")
for i, (v, z) in enumerate(zip(voltagem, scores)):
    status = ""
    if z < -2.0:
        status = " --> ALERTA: Falha de Energia!"
    print(f"  Dispositivo {i+1}: {v}V | Z-Score: {z:.2f}{status}")
