produtos = [
    {"produto": "A", "vendas": 300},
    {"produto": "B", "vendas": 150},
    {"produto": "C", "vendas": 480},
    {"produto": "D", "vendas": 90},
    {"produto": "E", "vendas": 220},
]

ordenados = sorted(produtos, key=lambda x: x["vendas"], reverse=True)

for rank, p in enumerate(ordenados, start=1):
    p["ranking"] = rank

produtos_com_rank = sorted(ordenados, key=lambda x: x["produto"])

for p in produtos_com_rank:
    print(p)
