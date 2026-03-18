import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlacao(dados:pd.DataFrame):
    print('Correlações')
    print('-------------------------------------------')
    correlaciona1 = dados['hours_studied'].corr(dados['exam_score'])
    correlaciona2 = dados['sleep_hours'].corr(dados['exam_score'])
    correlaciona3 = dados['attendance_percent'].corr(dados['exam_score'])

    print(f'correlação entre horas dormidas e de estudo com nota:{correlaciona1},{correlaciona2},{correlaciona3}')

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].scatter(dados['hours_studied'], dados['exam_score'], color='purple')
    axs[0].set_title('Distribuição de horas estudadas e nota')
    axs[0].set_xlabel('Horas Estudadas')
    axs[0].set_ylabel('Nota')


    axs[1].scatter(dados['sleep_hours'], dados['exam_score'], color='blue')
    axs[1].set_title('Distribuição de horas de sono e nota')
    axs[1].set_xlabel('Horas de Sono')

    axs[2].scatter(dados['attendance_percent'], dados['exam_score'], color='green')
    axs[2].set_title('Distribuição de frequência e nota')
    axs[2].set_xlabel('Frequência (%)')

    sns.despine()
    plt.tight_layout()
    plt.show()
    print('--------------------------------------------------------------')
    

