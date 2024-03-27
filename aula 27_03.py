# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:26:16 2024

@author: 20232enpro0010
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose

# caminho, pega a primeira coluna com as datas (ano,mes,dia), coluna com datas indice pra se localizar, puxa como objeto de série
data = pd.read_csv("C:/Users/Downloads/st_ds8_birth.csv", parse_dates=[0], index_col=0) 

# Gráfico de linha
grafico=data.plot()
grafico.set_xlabel("Dia")
grafico.set_ylabel("Nascimento")



# ***Amortecimento exponencial simples***

# separação de treino e de teste
treino = data.iloc[:292,] #começa do zero até o 292
teste = data.iloc[292:,] # de 292 em diante

# Usando os dados de treino para obter o valor de alfa (peso da ultima observação)
modelo_aes = SimpleExpSmoothing(treino).fit()

# Ver qual foi o alfa utilizado 
modelo_aes.summary() # resumo do que é o modelo. alpha = 0.0600966

# Previsões na amostra teste usando alpha
modelo_aes_teste = SimpleExpSmoothing(teste).fit(smoothing_level=0.0600966)

# Valores previstos na amostra de teste
prev_aes_teste = modelo_aes_teste.fittedvalues

# Calculamando MAPE (erro)
np.mean(np.abs((prev_aes_teste - teste.squeeze())/teste.squeeze())) # o erro 0.1256987998982875

#mostrando graficamnete
grafico=teste.squeeze().plot()
grafico.plot(prev_aes_teste)
grafico.legend(['Dados de teste','Previsões'])

# Previsão pro futuro 
previsoes = modelo_aes_teste.forecast(1) #só faz 1 previsão seguinte


