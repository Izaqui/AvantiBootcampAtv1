import pandas as pd

dados = pd.read_csv('./athlete_events.csv')

dados.head()
tamanho = dados.shape()
dados_leitura = dados.dropna()

print(dados_leitura)