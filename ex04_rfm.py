from datetime import datetime

transacoes = [
    {"cliente_id": 1, "data": "2024-03-01", "valor": 150.0},
    {"cliente_id": 1, "data": "2024-03-15", "valor": 200.0},
    {"cliente_id": 1, "data": "2024-04-01", "valor": 100.0},
    {"cliente_id": 2, "data": "2024-01-10", "valor": 500.0},
    {"cliente_id": 2, "data": "2024-02-20", "valor": 300.0},
    {"cliente_id": 3, "data": "2024-04-10", "valor": 80.0},
]

data_referencia = datetime(2024, 4, 24)

clientes = {}
for t in transacoes:
    cid = t["cliente_id"]
    dt = datetime.strptime(t["data"], "%Y-%m-%d")
    if cid not in clientes:
        clientes[cid] = {"ultima_compra": dt, "frequencia": 0, "monetario": 0.0}
    if dt > clientes[cid]["ultima_compra"]:
        clientes[cid]["ultima_compra"] = dt
    clientes[cid]["frequencia"] += 1
    clientes[cid]["monetario"] += t["valor"]

for cid, dados in clientes.items():
    recencia = (data_referencia - dados["ultima_compra"]).days
    print({
        "cliente_id": cid,
        "recencia_dias": recencia,
        "frequencia": dados["frequencia"],
        "monetario": dados["monetario"],
    })
