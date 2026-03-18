import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

def regressao_linear_horas_estudadas_nota(dados:pd.DataFrame):
    print('regressao linear = horas de estudo e nota')
    print('-----------------------------------------')
    x = np.array(dados['hours_studied'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    print(f'a - interseção: \t{format(intersecao)}')
    print(f'b - inclinação: \t{format(inclinacao[0])}')
    print(f'Equação: \t\tŶ = {intersecao} + {inclinacao[0]} * X')


    r2 = modelo.score(x.reshape(-1,1),y)
    print(f'r2 do modelo: {r2:.3f}')

    if r2 >= 0.9:
        print('Modelo excelente para análise')
    elif r2 >= 0.7:
        print('Modelo bom para análise')
    elif r2 >= 0.5 and r2 < 0.7:
        print('Modelo razoavel para análise')
    else:
        print('Modelo fraco para análise')
    print('-------------------------------------------')
    

def regressao_linear_horasdormidas_nota(dados:pd.DataFrame):
    print('regressao linear = horas de sono e nota')
    print('---------------------------------------')
    x = np.array(dados['sleep_hours'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    print(f'a - interseção: \t{format(intersecao)}')
    print(f'b - inclinação: \t{format(inclinacao[0])}')
    print(f'Equação: \t\tŶ = {intersecao} + {inclinacao[0]} * X')


    r2 = modelo.score(x.reshape(-1,1),y)
    print(f'r2 do modelo: {r2:.3f}')

    if r2 >= 0.9:
        print('Modelo excelente para análise')
    elif r2 >= 0.7:
        print('Modelo bom para análise')
    elif r2 >= 0.5 and r2 < 0.7:
        print('Modelo razoavel para análise')
    else:
        print('Modelo fraco para análise')
    print('--------------------------------------')
    

def regressao_linear_frequencia_nota(dados:pd.DataFrame):
    print('regressao linear = frequencia e nota')
    print('------------------------------------')
    x = np.array(dados['attendance_percent'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    print(f'a - interseção: \t{format(intersecao)}')
    print(f'b - inclinação: \t{format(inclinacao[0])}')
    print(f'Equação: \t\tŶ = {intersecao} + {inclinacao[0]} * X')


    r2 = modelo.score(x.reshape(-1,1),y)
    print(f'r2 do modelo: {r2:.3f}')

    if r2 >= 0.9:
        print('Modelo excelente para análise')
    elif r2 >= 0.7:
        print('Modelo bom para análise')
    elif r2 >= 0.5 and r2 < 0.7:
        print('Modelo razoavel para análise')
    else:
        print('Modelo fraco para análise')
    print('----------------------------------------')
