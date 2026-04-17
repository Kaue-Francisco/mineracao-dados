import pandas as pd
import numpy as np

np.random.seed(42)

df_clientes = pd.DataFrame({
    'id_cliente': range(1, 11),
    'nome_cliente': [
        'Ana Silva', 'Bruno Costa', 'Carlos Mendes', 'Diana Rocha', 'Eduardo Lima',
        'Fernanda Souza', 'Gabriel Santos', 'Helena Ferreira', 'Igor Oliveira', 'Julia Martins'
    ],
    'email': [f'cliente{i}@email.com' for i in range(1, 11)],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'PR', 'BA', 'SP', 'RJ', 'SC', 'SP'],
    'cidade': [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Campinas', 'Curitiba',
        'Salvador', 'São Paulo', 'Rio de Janeiro', 'Florianópolis', 'São Paulo'
    ]
})

df_produtos = pd.DataFrame({
    'id_produto': range(1, 9),
    'nome_produto': [
        'Placa de Vídeo RTX 4060',
        'Processador Ryzen 5 7600',
        'Memória RAM 16GB DDR5',
        'SSD NVMe 1TB',
        'Placa-Mãe B650',
        'Fonte 650W',
        'Cooler RGB',
        'Gabinete Mid Tower'
    ],
    'categoria': [
        'GPU', 'CPU', 'Memória', 'Armazenamento',
        'Placa-Mãe', 'Fonte', 'Refrigeração', 'Gabinete'
    ],
    'preco_unitario': [2500.00, 1200.00, 350.00, 450.00, 800.00, 400.00, 180.00, 320.00],
    'estoque': [15, 20, 50, 40, 18, 30, 25, 12]
})

n_vendas = 40
ids_cliente = np.random.randint(1, 11, n_vendas)
ids_produto  = np.random.randint(1, 9,  n_vendas)
quantidades  = np.random.randint(1, 5,  n_vendas)

precos = df_produtos.set_index('id_produto')['preco_unitario']
valores_totais = [qtd * precos[id_p] for qtd, id_p in zip(quantidades, ids_produto)]

df_vendas = pd.DataFrame({
    'id_venda':    range(1, n_vendas + 1),
    'id_cliente':  ids_cliente,
    'id_produto':  ids_produto,
    'quantidade':  quantidades,
    'valor_total': [round(v, 2) for v in valores_totais],
    'data_venda':  pd.date_range(start='2024-01-05', periods=n_vendas, freq='4D'),
    'forma_pagamento': np.random.choice(
        ['Pix', 'Cartão Crédito', 'Cartão Débito', 'Boleto'],
        n_vendas, p=[0.40, 0.35, 0.15, 0.10]
    )
})
