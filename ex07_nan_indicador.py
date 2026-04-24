import math

registros = [
    {"id": 1, "idade": 25, "renda": 3000.0},
    {"id": 2, "idade": None, "renda": 5000.0},
    {"id": 3, "idade": 40, "renda": None},
    {"id": 4, "idade": None, "renda": None},
]

MEDIA_IDADE = 30
MEDIA_RENDA = 4000.0

resultado = []
for r in registros:
    flag_idade_nula = 1 if r["idade"] is None else 0
    flag_renda_nula = 1 if r["renda"] is None else 0

    idade = r["idade"] if r["idade"] is not None else MEDIA_IDADE
    renda = r["renda"] if r["renda"] is not None else MEDIA_RENDA

    resultado.append({
        "id": r["id"],
        "idade": idade,
        "flag_idade_nula": flag_idade_nula,
        "renda": renda,
        "flag_renda_nula": flag_renda_nula,
    })

for r in resultado:
    print(r)
