import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np

def visualiza_rl_hora_estudo_nota(dados:pd.DataFrame):

    print('regressao linear = horas de estudo e nota')
    print('-----------------------------------------')
    x = np.array(dados['hours_studied'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_
    plt.scatter(x, y)
    plt.plot(x, (x * inclinacao + intersecao), color='purple')
    plt.legend(['Dispersão dos dados', 'Reta de Ajustamento'])
    plt.title('Regressão Linear Simples: Horas estudadas e Nota')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Horas estudadas')
    plt.ylabel('Nota')
    sns.despine()
    plt.show()

def visualiza_hora_dormida_nota(dados:pd.DataFrame):
    print('regressao linear = horas de sono e nota')
    print('---------------------------------------')
    x = np.array(dados['sleep_hours'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    plt.scatter(x, y)
    plt.plot(x, (x * inclinacao + intersecao), color='orange')
    plt.legend(['Dispersão dos dados', 'Reta de Ajustamento'])
    plt.title('Regressão Linear Simples: Horas dormidas e Nota')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Horas dormidas')
    plt.ylabel('Nota')
    sns.despine()
    plt.show()

def visualiza_frequencia_nota(dados:pd.DataFrame):
    x = np.array(dados['attendance_percent'])
    x = x.reshape(-1,1)
    y = np.array(dados['exam_score'])

    modelo= LinearRegression()
    modelo.fit(x,y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    plt.scatter(x, y)
    plt.plot(x, (x * inclinacao + intersecao), color='red')
    plt.legend(['Dispersão dos dados', 'Reta de Ajustamento'])
    plt.title('Regressão Linear Simples: Frequencia e Nota')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Frequencia')
    plt.ylabel('Nota')
    sns.despine()
    plt.show()