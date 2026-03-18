import pandas as pd

def analise_dados(dados:pd.DataFrame):
    print('Análise dos dados')
    print('--------------------------------------------')
    print(dados.head())
    print(f'linhas e colunas: {dados.shape}\n')
    print(dados.describe())
    print(f'colunas: {list(dados.columns)}')
    print(f"tipo de dados:\n {dados.dtypes}")

    print(f"máximo de horas estudadas: {max(dados['hours_studied'])}")
    print(f"mínimo de horas estudadas: {min(dados['hours_studied'])}")

    print(f"maior nota: {max(dados['exam_score'])}")
    print(f"maior nota: {max(dados['exam_score'])}")

    print(f'informações dos dados:\n {dados.info}') 
    print(f'contagem de dados nulos:\n {dados.isnull().sum()}') 
    print(f'contagem de dados duplicados: {dados.duplicated().sum()}')
    print('----------------------------------------------------')
