import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')

dados_empresaB= Dados.leitura_dados(path_csv, 'csv')

print(f"Nome colunas dados json: {dados_empresaA.nome_colunas}")
print(f"Tamanho dos dados json: {dados_empresaA.qtd_linhas}")

print(f"Nome colunas dados csv: {dados_empresaB.nome_colunas}")
print(f"Tamanho dos dados csv: {dados_empresaB.qtd_linhas}")

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.qtd_linhas)


#Salvando dados

dados_fusao.salvando_dados('data_processed/dados_combinados.csv')