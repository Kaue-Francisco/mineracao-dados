import pandas as pd
import numpy as np

np.random.seed(15)

# ── TABELA: df_usuarios ───────────────────────────────────────────────────────
df_usuarios = pd.DataFrame({
    'id_usuario': range(1, 11),
    'nome_usuario': [
        'André Faria', 'Beatriz Lopes', 'Caio Esteves', 'Débora Campos', 'Eduardo Ribeiro',
        'Fabiana Monteiro', 'Gustavo Araújo', 'Heloísa Carvalho', 'Ivan Barbosa', 'Juliana Pires'
    ],
    'departamento': [
        'TI', 'RH', 'Financeiro', 'Vendas', 'TI',
        'RH', 'Logística', 'Financeiro', 'Vendas', 'TI'
    ],
    'email': [f'usuario{i}@empresa.com.br' for i in range(1, 11)],
    'ramal': [f'40{i:02d}' for i in range(1, 11)]
})

# ── TABELA: df_equipamentos ───────────────────────────────────────────────────
df_equipamentos = pd.DataFrame({
    'id_equipamento': range(1, 13),
    'modelo': [
        'Dell Latitude 5520', 'HP EliteBook 840', 'Lenovo ThinkPad X1',
        'MacBook Pro M2', 'Dell OptiPlex 7080', 'Acer Aspire 5',
        'HP ZBook Studio', 'Lenovo IdeaPad 5', 'Dell Precision 5570',
        'Asus ZenBook 14', 'Samsung Galaxy Tab S8', 'iPad Pro 12.9'
    ],
    'sistema_operacional': [
        'Windows 11', 'Windows 10', 'Windows 11', 'macOS Ventura', 'Windows 10',
        'Linux Ubuntu 22.04', 'Windows 11', 'Windows 10', 'Windows 11',
        'Linux Ubuntu 22.04', 'Android 13', 'iOS 17'
    ],
    'tipo_equipamento': [
        'Notebook', 'Notebook', 'Notebook', 'Notebook', 'Desktop',
        'Notebook', 'Workstation', 'Notebook', 'Workstation',
        'Notebook', 'Tablet', 'Tablet'
    ],
    'id_usuario': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 7]
})

# ── TABELA: df_chamados ───────────────────────────────────────────────────────
n_chamados = 50
categorias   = ['Hardware', 'Software', 'Rede', 'Acesso/Senha', 'Impressora', 'E-mail']
prioridades  = ['Baixa', 'Média', 'Alta', 'Crítica']
status_opts  = ['Resolvido', 'Em andamento', 'Pendente', 'Cancelado']

ids_usuario    = np.random.randint(1, 11, n_chamados)
ids_equip      = np.random.randint(1, 13, n_chamados)
horas_res      = np.round(np.random.uniform(0.5, 16.0, n_chamados), 1)
datas_abertura = pd.date_range(start='2024-01-03', periods=n_chamados, freq='3D')

df_chamados = pd.DataFrame({
    'id_ticket':         range(1, n_chamados + 1),
    'id_usuario':        ids_usuario,
    'id_equipamento':    ids_equip,
    'categoria':         np.random.choice(categorias, n_chamados,
                             p=[0.20, 0.25, 0.20, 0.15, 0.10, 0.10]),
    'prioridade':        np.random.choice(prioridades, n_chamados,
                             p=[0.30, 0.40, 0.20, 0.10]),
    'descricao':         [f'Chamado #{i} registrado pelo usuário' for i in range(1, n_chamados + 1)],
    'horas_resolucao':   horas_res,
    'data_abertura':     datas_abertura,
    'status':            np.random.choice(status_opts, n_chamados,
                             p=[0.65, 0.15, 0.15, 0.05])
})