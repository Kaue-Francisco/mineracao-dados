from datetime import datetime

timestamps = [
    "2024-03-15 10:30:00",
    "2024-03-16 14:00:00",
    "2024-03-17 09:00:00",  # domingo
    "2024-03-23 20:00:00",  # sabado
    "2024-04-01 08:00:00",
]

resultado = []
for ts in timestamps:
    dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    dia_semana = dt.strftime("%A")
    flag_fim_semana = 1 if dt.weekday() >= 5 else 0
    resultado.append({
        "timestamp": ts,
        "mes": dt.month,
        "dia_semana": dia_semana,
        "flag_fim_semana": flag_fim_semana,
    })

for r in resultado:
    print(r)
