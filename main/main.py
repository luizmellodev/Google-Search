from google import google
import os

print('Informe palavras-chaves para a pesquisa')
pesquisa = input()

print('Informe os sites específicos. Digite o link dos sites Ex: g1.com.br\n Caso não tenha sites específicos, apenas dê Enter')
sites = input()

print('Informe o numero de páginas do Google a serem retornados')
numeroPag = input()

print('Informe o nome do arquivo .csv desejado (Informe apenas o nome, não é preciso escrever .csv)')
arquivo = input()

dir_path = os.path.join('./resultados', arquivo)
if not os.path.exists('./resultados'):
    os.makedirs('./resultados')

if(sites):
    resultados = google.search('site: {}'.format(sites) + '"{}"'.format(pesquisa), int(numeroPag))
    with open('{}.csv'.format(dir_path), 'w') as csv_file:
        for res in resultados:
            csv_file.write(f"{res.name},{res.link},{res.description}\n")

else:
    resultados = google.search('"{}"'.format(pesquisa), int(numeroPag))
    with open('{}.csv'.format(dir_path), 'w') as csv_file:
        for res in resultados:
            csv_file.write(f"{res.name},{res.link},{res.description}\n")

            