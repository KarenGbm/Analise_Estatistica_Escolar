import pandas as pd
from src.analisedados import analise_dados
from src.correlacao import correlacao
from src.dispersao import Dispersao
from src.RegressaoLinear import regressao_linear_horas_estudadas_nota, regressao_linear_horasdormidas_nota,regressao_linear_frequencia_nota
from src.RegressaoMultipla import regressao_multipla
from src.visualizacoes import visualiza_rl_hora_estudo_nota, visualiza_hora_dormida_nota, visualiza_frequencia_nota

dados = r'data\data\student_exam_scores.csv'

dados = pd.read_csv(dados)

#funções para analisar

analise_dados(dados)

correlacao(dados)

Dispersao(dados)

regressao_linear_horas_estudadas_nota(dados)

regressao_linear_horasdormidas_nota(dados)

regressao_linear_frequencia_nota(dados)

regressao_multipla(dados)

visualiza_rl_hora_estudo_nota(dados)

visualiza_hora_dormida_nota(dados)

visualiza_frequencia_nota(dados)