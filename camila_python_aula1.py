# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Camila Antonia Fiorin Fim - Fundamentos e Ciência de Dados


# importando o pacote pandas
import pandas as pd

# carregando os dados do dataset e inserindo na variavel pokemon
pokemon = pd.read_csv("C:/Users/Downloads/pokemon_data.csv")

# descrição dos dados
pokemon.describe()

# selecionar colunas especificas (data frame com name, type 1, e type 2)
pokemon_2 = pokemon[['Name','Type 1','Type 2']]

# filtrar por tipo do pokemon (função loc que localiza pelo nome da coluna)
pokemon_fogo = pokemon.loc[pokemon['Type 1']=='Fire']

# Usando indice numerico ( todos pokemons cuja coluna dois for fire)
pokemon_fogo2 = pokemon[pokemon.iloc[:,2]=="Fire"]

# Usando indice numerico ( todos pokemons cuja coluna dois for fire)
pokemon_fogo3 = pokemon.loc[(pokemon['Type 1']=='Fire')|(pokemon['Type 2']=="Fire")]

# Ordenação do que tem mais ponto de ataque para o que tem menos (crescente)
pokemon_ataque = pokemon.sort_values('Attack')

# Ordenação decrescente
pokemon_ataque = pokemon.sort_values('Attack', ascending=False)

# estatísticas de agregação (groupby faz separado para cada grupo)
pokemon_agrupado = pokemon.groupby(['Type 1']) #(guarda o conjunto de dados)
pokemon_agrupado['Attack'].mean()   # faz estatistica so de uma coluna
pokemon_agrupado['Attack'].std()
pokemon_agrupado['Attack'].median()

