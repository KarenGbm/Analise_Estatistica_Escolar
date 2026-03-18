import pandas as pd
import matplotlib.pyplot as plt

def Dispersao(dados:pd.DataFrame):
    print('Verificação de Outliers')
    print('-------------------------------------------')
    plt.figure(figsize=(8, 5))
    plt.boxplot([
        dados['exam_score'],
        dados['hours_studied'],
        dados['attendance_percent']
    ])

    plt.xticks([1, 2, 3], ['Nota exame', 'Horas estudadas', 'Frequência %'])
    plt.title('Distribuição dos Dados')
    plt.ylabel('Valores')
    plt.show()
    print('-----------------------------------------------')
    