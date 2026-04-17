import numpy as np
from sklearn.ensemble import IsolationForest

np.random.seed(42)

# 1000 linhas normais (valores entre 0 e 10)
normais = np.random.normal(loc=5, scale=1, size=(1000, 2))

# 50 linhas absurdas (valores entre 100 e 200)
absurdos = np.random.uniform(low=100, high=200, size=(50, 2))

dataset = np.vstack([normais, absurdos])

# Isolation Forest com contamination=0.05 (espera 5% de anomalias)
modelo_05 = IsolationForest(contamination=0.05, random_state=42)
pred_05 = modelo_05.fit_predict(dataset)
anomalias_05 = (pred_05 == -1).sum()

# Isolation Forest com contamination=0.20 (espera 20% de anomalias)
modelo_20 = IsolationForest(contamination=0.20, random_state=42)
pred_20 = modelo_20.fit_predict(dataset)
anomalias_20 = (pred_20 == -1).sum()

print(f"Dataset: {len(normais)} linhas normais + {len(absurdos)} absurdas = {len(dataset)} total")
print()
print(f"contamination=0.05 -> Anomalias detectadas: {anomalias_05}")
print(f"contamination=0.20 -> Anomalias detectadas: {anomalias_20}")
print()
print("Conclusão: quanto maior o contamination, mais pontos são marcados como -1.")
print("Com 0.05 o modelo é conservador; com 0.20 ele marca até pontos normais como anomalia.")
