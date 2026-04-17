import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

producao = [100, 102, 98, 105, 500, 101]

# 1. Remover outlier com Z-Score
scores = zscore(producao)
dados_limpos = [v for v, z in zip(producao, scores) if abs(z) <= 2.5]

print("Dados originais:", producao)
print("Z-Scores:", [f"{z:.2f}" for z in scores])
print("Outliers removidos:", [v for v, z in zip(producao, scores) if abs(z) > 2.5])
print("Dados limpos:", dados_limpos)
print()

# 2. Normalização Min-Max nos dados limpos
dados_array = np.array(dados_limpos).reshape(-1, 1)
scaler = MinMaxScaler()
dados_normalizados = scaler.fit_transform(dados_array).flatten()

print("Dados normalizados (Min-Max):")
for original, norm in zip(dados_limpos, dados_normalizados):
    print(f"  {original} -> {norm:.4f}")

print()
print("""Explicação — por que normalizar DEPOIS de remover outliers:

Se normalizarmos com o 500 ainda presente:
  - min = 98, max = 500  -> escala de 0 a 1 cobre 402 unidades
  - Todos os valores normais (98-105) ficariam comprimidos entre 0.0 e ~0.017
  - A variação real entre os dias normais (7 peças) seria invisível na escala

Após remover o 500:
  - min = 98, max = 105  -> escala de 0 a 1 cobre apenas 7 unidades
  - Cada peça a mais representa uma diferença significativa na escala
  - Os dados ficam bem distribuídos entre 0.0 e 1.0

Conclusão: o outlier 'sequestra' toda a escala para si, esmagando a variação
legítima dos dados normais. Remover primeiro garante uma normalização útil.""")
