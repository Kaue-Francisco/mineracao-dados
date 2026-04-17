import pandas as pd
import numpy as np

np.random.seed(99)

df_ambientes = pd.DataFrame({
    'id_ambiente': range(1, 6),
    'nome_setor': [
        'Linha de Produção A',
        'Linha de Produção B',
        'Almoxarifado',
        'Sala de Servidores',
        'Área Administrativa'
    ],
    'descricao': [
        'Área de manufatura principal com fornos industriais',
        'Área de manufatura secundária',
        'Estoque de matérias-primas e produtos acabados',
        'CPD e infraestrutura de rede',
        'Escritórios e salas de reunião'
    ],
    'temp_alerta_c': [45.0, 42.0, 35.0, 30.0, 28.0]
})

tipos = ['Raspberry Pi 4', 'Orange Pi 5', 'ESP32']
df_dispositivos = pd.DataFrame({
    'id_dispositivo': range(1, 13),
    'nome_dispositivo': [f'DEV-{str(i).zfill(3)}' for i in range(1, 13)],
    'tipo': [
        'Raspberry Pi 4', 'Orange Pi 5', 'ESP32',    # Linha Prod. A (3 devs)
        'Raspberry Pi 4', 'ESP32',                    # Linha Prod. B (2 devs)
        'Orange Pi 5', 'ESP32',                       # Almoxarifado   (2 devs)
        'Raspberry Pi 4', 'Orange Pi 5',              # Sala Servidores(2 devs)
        'ESP32', 'Raspberry Pi 4', 'Orange Pi 5'      # Área Adm.      (3 devs)
    ],
    'id_ambiente': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5],
    'mac_address': [
        'B8:27:EB:AA:01', 'B8:27:EB:AA:02', 'B8:27:EB:AA:03',
        'B8:27:EB:AA:04', 'B8:27:EB:AA:05', 'B8:27:EB:AA:06',
        'B8:27:EB:AA:07', 'B8:27:EB:AA:08', 'B8:27:EB:AA:09',
        'B8:27:EB:AA:10', 'B8:27:EB:AA:11', 'B8:27:EB:AA:12'
    ]
})

temp_base = {1: 42.0, 2: 38.0, 3: 27.0, 4: 21.0, 5: 23.0}
umid_base = {1: 55.0, 2: 58.0, 3: 65.0, 4: 45.0, 5: 50.0}

n_leituras = 300
telemetria_rows = []

timestamps = pd.date_range(start='2024-03-01 00:00', periods=n_leituras, freq='2h24min')

for i in range(n_leituras):
    id_disp = np.random.randint(1, 13)
    id_amb  = df_dispositivos.loc[
        df_dispositivos['id_dispositivo'] == id_disp, 'id_ambiente'
    ].values[0]

    temp   = round(temp_base[id_amb] + np.random.uniform(-3.0, 5.0), 1)
    umidad = round(umid_base[id_amb] + np.random.uniform(-5.0, 5.0), 1)

    telemetria_rows.append({
        'id_leitura':     i + 1,
        'id_dispositivo': id_disp,
        'data_hora':      timestamps[i],
        'temperatura_c':  temp,
        'umidade_pct':    umidad,
        'status':         'Normal' if temp < temp_base[id_amb] + 4 else 'Alerta'
    })

df_telemetria = pd.DataFrame(telemetria_rows)