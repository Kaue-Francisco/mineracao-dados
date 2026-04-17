import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "Nome": ["Ana", None, "Carlos", "Diana", None, "Eduardo", "Fernanda", None],
    "Email": ["ana@email.com", "b@email.com", None, None, "e@email.com", None, "f@email.com", "g@email.com"],
    "Telefone": [None, "11999", "21888", None, "31777", "41666", None, None],
    "Cidade": ["SP", "RJ", None, "MG", "RS", None, "BA", "PE"],
    "CEP": ["01001", None, None, "30100", None, "80010", "40020", None]
})

plt.figure(figsize=(8, 5))
sns.heatmap(df.isna(), cbar=False, cmap="viridis", yticklabels=False)
plt.title("Mapa de Calor - Valores Ausentes")
plt.tight_layout()
plt.show()
