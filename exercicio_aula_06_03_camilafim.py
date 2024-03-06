# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:43:47 2024

@author: 20232enpro0010
"""

# Camila Antonia Fiorin Fim - Fundamentos e Ciência de Dados
# Exercicio em laboratorio 06/03/2024


# importando o pacote pandas
import pandas as pd

# carregando os dados do dataset e inserindo na variavel pokemon
pokemon = pd.read_csv("C:/Users/20232enpro0010/Downloads/pokemon_data.csv")
# Exitem 12 variáveis e 800 casos

# descrição dos dados
pokemon.describe()

# selecionar colunas especificas (data frame com defesa, type 1, e type 2)
pokemon_2 = pokemon[['Defense','Type 1','Type 2']]

# Ordenação do que tem mais ponto de defesa para o que tem menos (decrescente)
pokemon_defesa = pokemon_2.sort_values('Defense', ascending=False)

# tabela de frequencias
pokemon['Type 1'].value_counts()
# Water é o tipo predominante
pokemon['Type 2'].value_counts()
# Flying é o tipo predominante

# acrescentando nova coluna na base de dados: comparando média
pokemon['ataque_defesa']= pokemon['Attack']/pokemon['Defense']

# estatísticas de agregação (groupby faz separado para cada grupo): comparando média
pokemon_agrupado1 = pokemon.groupby(['Type 1']) #(guarda o conjunto de dados)
pokemon_agrupado1['Defense'].median()

# estatísticas de agregação (groupby faz separado para cada grupo)
pokemon_agrupado2 = pokemon.groupby(['Type 2']) #(guarda o conjunto de dados)
pokemon_agrupado2['Defense'].median()
# existe diferanças por grupo

# desvio padrão
pokemon_agrupado1['Defense'].std()
pokemon_agrupado2['Defense'].std()
# o desvio padrao do tipo 1 é maior

