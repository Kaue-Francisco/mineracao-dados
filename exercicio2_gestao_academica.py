import pandas as pd
import numpy as np

np.random.seed(7)

df_cursos = pd.DataFrame({
    'id_curso': range(1, 5),
    'nome_curso': [
        'Análise e Desenvolvimento de Sistemas',
        'Redes de Computadores',
        'Banco de Dados',
        'Segurança da Informação'
    ],
    'carga_horaria': [2400, 2000, 2200, 2100],
    'turno': ['Noturno', 'Matutino', 'Noturno', 'Matutino']
})

df_disciplinas = pd.DataFrame({
    'id_disciplina': range(1, 13),
    'nome_disciplina': [
        'Programação I', 'Programação II', 'Estruturas de Dados',
        'Desenvolvimento Web', 'Redes I', 'Redes II',
        'Segurança de Redes', 'Banco de Dados I', 'Banco de Dados II',
        'Segurança da Informação', 'Matemática Discreta', 'Sistemas Operacionais'
    ],
    'id_curso': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 2],
    'carga_horaria': [80, 80, 60, 80, 80, 60, 80, 80, 80, 80, 60, 60]
})

df_professores = pd.DataFrame({
    'id_professor': range(1, 7),
    'nome_professor': [
        'Prof. Roberto Alves', 'Prof. Márcia Santos', 'Prof. Fábio Lima',
        'Prof. Carla Mendes', 'Prof. Adriano Costa', 'Prof. Lúcia Ferreira'
    ],
    'formacao': [
        'Doutorado em Ciência da Computação',
        'Mestrado em Sistemas de Informação',
        'Doutorado em Redes',
        'Mestrado em Banco de Dados',
        'Doutorado em Inteligência Artificial',
        'Mestrado em Matemática'
    ],
    'id_curso': [1, 1, 2, 3, 4, 4]
})

# Mapeamento: disciplina → professor responsável
disc_prof = {
    1: 1, 2: 1, 3: 2, 4: 2,   # ADS → Prof. Roberto e Márcia
    5: 3, 6: 3, 7: 3, 12: 3,  # Redes → Prof. Fábio
    8: 4, 9: 4,                 # BD → Prof. Carla
    10: 5, 11: 6               # SI e Mat. Discreta
}

nomes_alunos = [
    # ADS — 15 alunos (curso mais popular)
    'Alice Nunes', 'Bernardo Dias', 'Cecília Porto', 'Daniel Melo', 'Elisa Viana',
    'Felipe Assis', 'Giovanna Ramos', 'Henrique Lins', 'Isabela Cruz', 'João Pedro Luz',
    'Karen Pinto', 'Leonardo Braga', 'Marina Fonseca', 'Nicolas Teixeira', 'Olivia Doria',
    # Redes — 6 alunos
    'Paulo Rezende', 'Quesia Borges', 'Rafael Macedo', 'Sofia Guimarães', 'Thiago Neto',
    'Ursula Campos',
    # Banco de Dados — 5 alunos
    'Vinícius Serra', 'Wanessa Leal', 'Xênia Rocha', 'Yago Monteiro', 'Zara Freitas',
    # Segurança da Informação — 4 alunos
    'Alan Borges', 'Bianca Teles', 'Caio Drummond', 'Débora Salles'
]

# Distribuição de alunos por curso (15 ADS, 6 Redes, 5 BD, 4 SI)
cursos_alunos = [1]*15 + [2]*6 + [3]*5 + [4]*4

df_alunos = pd.DataFrame({
    'id_aluno': range(1, 31),
    'nome_aluno': nomes_alunos,
    'id_curso': cursos_alunos,
    'semestre': np.random.choice([1, 2, 3, 4, 5, 6], 30)
})

matriculas = []
id_mat = 1
for _, aluno in df_alunos.iterrows():
    discs_do_curso = df_disciplinas[
        df_disciplinas['id_curso'] == aluno['id_curso']
    ]['id_disciplina'].tolist()

    # Cada aluno cursando até 4 disciplinas do seu curso
    n_discs = min(4, len(discs_do_curso))
    discs_escolhidas = np.random.choice(discs_do_curso, n_discs, replace=False)

    for id_disc in discs_escolhidas:
        id_prof = disc_prof.get(id_disc, np.random.randint(1, 7))
        nota = round(np.random.uniform(4.0, 10.0), 1)
        matriculas.append({
            'id_matricula':  id_mat,
            'id_aluno':      aluno['id_aluno'],
            'id_disciplina': int(id_disc),
            'id_professor':  id_prof,
            'id_curso':      aluno['id_curso'],
            'nota':          nota,
            'status':        'Aprovado' if nota >= 5.0 else 'Reprovado',
            'ano_semestre':  '2024-1'
        })
        id_mat += 1

df_matriculas = pd.DataFrame(matriculas)