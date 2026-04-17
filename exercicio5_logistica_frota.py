import pandas as pd
import numpy as np

np.random.seed(33)

df_motoristas = pd.DataFrame({
    'id_motorista': range(1, 8),
    'nome_motorista': [
        'Antônio Vieira', 'Bruna Campos', 'Cláudio Sousa',
        'Daniela Rocha', 'Emerson Lima', 'Fátima Cunha', 'Geraldo Neves'
    ],
    'cnh': ['AB', 'B', 'C', 'D', 'AB', 'B', 'CE'],
    'anos_experiencia': [12, 5, 8, 15, 3, 7, 20],
    'ativo': [True, True, True, True, True, True, False]
})

df_veiculos = pd.DataFrame({
    'id_veiculo': range(1, 10),
    'placa': [
        'ABC-1234', 'DEF-5678', 'GHI-9012',
        'JKL-3456', 'MNO-7890', 'PQR-1357',
        'STU-2468', 'VWX-9753', 'YZA-6420'
    ],
    'tipo_veiculo': [
        'Van', 'Caminhão', 'Van',
        'Moto', 'Caminhão', 'Van',
        'Moto', 'Caminhão', 'Van'
    ],
    'marca_modelo': [
        'Fiat Ducato', 'Mercedes Atego 1719', 'Renault Master',
        'Honda CG 160', 'Volvo FH 460', 'Volkswagen Crafter',
        'Yamaha Fazer 250', 'Scania R 450', 'Peugeot Boxer'
    ],
    'ano': [2020, 2019, 2022, 2021, 2018, 2023, 2020, 2021, 2022],
    'capacidade_kg': [1500, 8000, 1500, 150, 15000, 1500, 150, 20000, 1500]
})

n_entregas = 60
status_opts  = ['Entregue', 'Em trânsito', 'Atrasado', 'Cancelado']
cidades      = [
    'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba',
    'Porto Alegre', 'Salvador', 'Recife', 'Fortaleza', 'Manaus'
]

id_veiculos   = np.random.randint(1, 10, n_entregas)
id_motoristas = np.random.randint(1, 7,  n_entregas)   # motorista 7 inativo

distancias = []
for id_v in id_veiculos:
    tipo = df_veiculos.loc[df_veiculos['id_veiculo'] == id_v, 'tipo_veiculo'].values[0]
    if tipo == 'Moto':
        dist = round(np.random.uniform(20, 150), 1)
    elif tipo == 'Van':
        dist = round(np.random.uniform(80, 500), 1)
    else:  # Caminhão
        dist = round(np.random.uniform(300, 1200), 1)
    distancias.append(dist)

df_entregas = pd.DataFrame({
    'id_entrega':      range(1, n_entregas + 1),
    'id_motorista':    id_motoristas,
    'id_veiculo':      id_veiculos,
    'cidade_destino':  np.random.choice(cidades, n_entregas),
    'distancia_km':    distancias,
    'data_entrega':    pd.date_range(start='2024-01-02', periods=n_entregas, freq='2D'),
    'status':          np.random.choice(status_opts, n_entregas, p=[0.70, 0.12, 0.12, 0.06]),
    'peso_carga_kg':   np.round(np.random.uniform(50, 8000, n_entregas), 0)
})