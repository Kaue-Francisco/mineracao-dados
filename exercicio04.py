from scipy.stats import zscore

medidas = [10, 12, 11, 10, 10000]
scores = zscore(medidas)

import numpy as np
media = np.mean(medidas)
desvio = np.std(medidas)

z_10000 = scores[-1]

print(f"Média da lista:        {media:.2f}")
print(f"Desvio padrão:         {desvio:.2f}")
print(f"Z-Score do valor 10000: {z_10000:.4f}")
print()

if abs(z_10000) > 3:
    print("O valor 10000 ULTRAPASSA a marca de 3 sigmas.")
else:
    print("O valor 10000 NÃO ultrapassa a marca de 3 sigmas.")
    print("Motivo: o outlier colossal infla o desvio padrão de tal forma que")
    print("a distância relativa de 10000 até a média fica menor que 3 sigmas.")
    print("Isso demonstra a limitação do Z-Score em listas pequenas com outliers extremos.")
