leituras = [
    {"momento": "T1", "valor": 120.0},
    {"momento": "T2", "valor": 135.0},
]

v1 = leituras[0]["valor"]
v2 = leituras[1]["valor"]

delta = v2 - v1
evolucao_pct = (delta / v1) * 100
tendencia = "crescimento" if delta > 0 else "queda"

print(f"Leitura T1: {v1}")
print(f"Leitura T2: {v2}")
print(f"Delta: {delta:.2f}")
print(f"Evolucao Percentual: {evolucao_pct:.2f}%")
print(f"Tendencia: {tendencia}")
