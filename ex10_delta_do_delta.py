leituras = [10.0, 15.0, 25.0]  # tres leituras consecutivas do sensor

delta1 = leituras[1] - leituras[0]
delta2 = leituras[2] - leituras[1]
aceleracao = delta2 - delta1

flag_exponencial = 1 if aceleracao > 0 and delta2 > delta1 else 0

print(f"Leituras: {leituras}")
print(f"Delta 1 (T2-T1): {delta1}")
print(f"Delta 2 (T3-T2): {delta2}")
print(f"Aceleracao (Delta do Delta): {aceleracao}")
print(f"Flag tendencia exponencial: {flag_exponencial}")
