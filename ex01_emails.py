emails = [
    "joao@gmail.com",
    "maria@empresa.com.br",
    "carlos@hotmail.com",
    "ana@corporacao.com.br",
    "pedro@yahoo.com",
]

resultado = []
for email in emails:
    dominio = email.split("@")[1]
    flag_empresarial = 1 if dominio.endswith(".com.br") else 0
    resultado.append({"email": email, "dominio": dominio, "flag_empresarial": flag_empresarial})

for r in resultado:
    print(r)
