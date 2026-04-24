# A Razao de Comprometimento captura a relacao entre divida e renda,
# algo que as variaveis isoladas nao expressam: alguem com R$5000 de divida
# e renda de R$5000 esta muito mais comprometido do que alguem com a mesma
# divida mas renda de R$20000.

clientes = [
    {"id": 1, "divida_total": 5000.0, "renda_mensal": 5000.0},
    {"id": 2, "divida_total": 5000.0, "renda_mensal": 20000.0},
    {"id": 3, "divida_total": 1200.0, "renda_mensal": 3000.0},
]

for c in clientes:
    razao = c["divida_total"] / c["renda_mensal"]
    print({
        "id": c["id"],
        "divida_total": c["divida_total"],
        "renda_mensal": c["renda_mensal"],
        "razao_comprometimento": round(razao, 4),
    })
