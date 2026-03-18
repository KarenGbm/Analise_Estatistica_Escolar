from pandas import DataFrame
from sklearn.linear_model import LinearRegression



def regressao_multipla(dados:DataFrame):
    print('regressao multipla: horas de sono e horas estudadas, frequencia e nota')
    print('-----------------------------------------------------------------------')
    x= dados[['hours_studied', 'sleep_hours', 'attendance_percent']]
    y = dados['exam_score']

    modelo = LinearRegression()
    modelo.fit(x, y)

    inclinacao = modelo.coef_
    intersecao = modelo.intercept_

    print(f'a - interseção: \t{format(intersecao)}')
    print(f'b - inclinação: \t{format(inclinacao[0])}')
    print(f'Equação: \t\tŶ = {intersecao} + {inclinacao[0]} * X')


    r2 = modelo.score(x, y)
    print("r2:", r2)

    if r2 >= 0.9:
        print('Modelo excelente para análise')
    elif r2 >= 0.7:
        print('Modelo bom para análise')
    elif r2 >= 0.5 and r2 < 0.7:
        print('Modelo razoavel para análise')
    else:
        print('Modelo fraco para análise')
    
    print(f'impacto das variaveis: \n {modelo.coef_}')
    print('-------------------------------------------------')



