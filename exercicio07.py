from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

dados = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]
notas = [d[0] for d in dados]

# Z-Score apenas nas notas (análise univariada)
z_notas = zscore(notas)
print("Z-Score individual das notas:")
for i, (d, z) in enumerate(zip(dados, z_notas)):
    print(f"  Aluno {i+1} [Nota: {d[0]}, Faltas: {d[1]}] -> Z-Score nota: {z:.2f}")

print()
print("Pelo Z-Score de notas, o aluno [9, 25] não é detectado (nota alta é 'normal').")
print()

# Isolation Forest com ambas as dimensões (análise multivariada)
modelo = IsolationForest(contamination=0.33, random_state=42)
predicoes = modelo.fit_predict(dados)

print("Isolation Forest (Nota + Faltas):")
for i, (d, pred) in enumerate(zip(dados, predicoes)):
    rotulo = "ANOMALIA" if pred == -1 else "Normal"
    print(f"  Aluno {i+1} [Nota: {d[0]}, Faltas: {d[1]}] -> {pred} ({rotulo})")

print()
print("A combinação nota alta + muitas faltas é incomum no conjunto, portanto")
print("o Isolation Forest detecta [9, 25] como anomalia ao analisar as duas dimensões.")
