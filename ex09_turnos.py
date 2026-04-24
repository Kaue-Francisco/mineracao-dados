logs = [2, 6, 9, 13, 18, 22, 0, 23]

def classificar_turno(hora):
    if 0 <= hora < 6:
        return "Madrugada"
    elif 6 <= hora < 18:
        return "Comercial"
    else:
        return "Noite"

for hora in logs:
    turno = classificar_turno(hora)
    print({"hora": hora, "turno": turno})
