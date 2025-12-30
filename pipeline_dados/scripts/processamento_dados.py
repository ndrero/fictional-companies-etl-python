import json
import csv


class Dados:
    def __init__(self, path, tipo_arquivo):
        self.path = path
        self.tipo_arquivo = tipo_arquivo
        self.dados = self.leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()
        
    def __leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(self):

        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    def leitura_dados(self):
        dados = []

        if self.tipo_arquivo == 'csv':
            dados = self.__leitura_csv()
        
        elif self.tipo_arquivo == 'json':
            dados = self.__leitura_json()

        elif self.tipo_arquivo == 'list':
            dados = self.path
            self.path = 'lista em memória'

        return dados

    def __get_columns(self):
        return list(self.dados[-1].keys())

    def rename_columns(self, key_mapping):
        new_dados_csv = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados_csv.append(dict_temp)
        
        self.dados = new_dados_csv
        self.nome_colunas = self.__get_columns()

    def __size_data(self):
        return len(self.dados)


    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list, 'list')
    
    def __transformando_dados_tabela(self):
    
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela

    def salvando_dados(self, path): 
        dados_combinados = self.__transformando_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados)

