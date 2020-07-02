from google import google
import os
import traceback
<<<<<<< HEAD:webarchive.py
import csv 


# from main import main
print('Informe palavras-chaves para a pesquisa')
pesquisa = input()

print('Informe os sites específicos. Digite o link dos sites Ex: g1.com.br\n Caso não tenha sites específicos, apenas dê Enter')
sites = input()

print('Informe o numero de páginas do Google a serem retornados')
numeroPag = input()

print('Informe o nome do arquivo .csv desejado (Informe apenas o nome, não é preciso escrever .csv)')
arquivo = input()
=======
from interface.interface import TelaPython
tela = TelaPython()
pesquisa, sites, numeroPag, arquivo = tela.Iniciar()
>>>>>>> e55f841c6e8ba7948f41b78792c2f387e48603b8:src/main.py

dir_path = os.path.join('./resultados', arquivo)
if not os.path.exists('./resultados'):
    os.makedirs('./resultados')

pesquisas = 0
try:
    if(sites):
        resultados = google.search('site: {}'.format(
            sites) + '"{}"'.format(pesquisa), int(numeroPag))
        with open('{}.csv'.format(dir_path), 'w') as csv_file:
            for res in resultados:
                csv_file.write(
                    f"{res.name},{res.link},{res.description}\n")
                pesquisas = pesquisas + 1

    else:
        sites = 'Nenhum site inserido'
        resultados = google.search('"{}"'.format(
            pesquisa), int(numeroPag))
        with open('{}.csv'.format(dir_path), 'w') as csv_file:
            for res in resultados:
                csv_file.write(
                    f"{res.name},{res.link},{res.description}\n")
                pesquisas = pesquisas + 1

    if(resultados):
        print('\n\n\nPesquisa feita com sucesso.\n Palavras-chaves:' + '"{}"'.format(pesquisa) +
                '\n Sites: ' + '"{}"'.format(sites) + '\n Nome do arquivo: ' + '"{}"'.format(arquivo) + '\n Resultados obtidos em ' + '"{}"'.format(numeroPag) + ' páginas do Google: ' + '"{}"'.format(pesquisas))

except Exception as err:
    print(err)
    print('Nenhum resultado encontrado. Isso pode ter acontecido por algum erro interno durante a execução do código ou por uma pesquisa muito restrita/específica.')


with open('{}.csv'.format(dir_path), 'w') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))