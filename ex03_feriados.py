from datetime import datetime

EVENTOS = {
    (12, 25): "Natal",
    (11, 15): "Proclamacao da Republica",
    (1, 1): "Ano Novo",
}

def black_friday(ano):
    from datetime import date, timedelta
    # quarta quinta de novembro
    dia = date(ano, 11, 1)
    quintas = 0
    while quintas < 4:
        if dia.weekday() == 3:
            quintas += 1
        if quintas < 4:
            dia += timedelta(1)
    return dia + timedelta(1)  # sexta apos a quarta quinta

datas = [
    "2024-12-25",
    "2024-11-29",
    "2024-07-10",
    "2024-01-01",
]

for d in datas:
    dt = datetime.strptime(d, "%Y-%m-%d")
    chave = (dt.month, dt.day)
    evento = EVENTOS.get(chave)

    if evento is None and dt.date() == black_friday(dt.year):
        evento = "Black Friday"

    flag_evento = 1 if evento else 0
    print({"data": d, "evento": evento or "Nenhum", "flag_evento": flag_evento})
