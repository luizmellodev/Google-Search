from google import google
import os
import traceback, html2text, json, re
from interface.interface import TelaPython
from google.modules.utils import get_html

tela = TelaPython()
pesquisa, sites, numeroPag, arquivo = tela.Iniciar()

dir_path = os.path.join('./resultados', arquivo)
if not os.path.exists('./resultados'):
    os.makedirs('./resultados')

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
def pesquisageral(sites, pesquisa, numeroPag, dir_path):
    try:
        if(sites):
            resultados = google.search('site: {}'.format(
                sites) + '"{}"'.format(pesquisa), int(numeroPag))
        else:
            sites = 'Nenhum site inserido'
            resultados = google.search('"{}"'.format(
                pesquisa), int(numeroPag))
        with open('{}.csv'.format(os.path.join(dir_path, "resultados_da_pesquisa")), 'w',  encoding='utf-8') as csv_file:
            for res in resultados:
                csv_file.write(
                    f"{res.name}\t{res.link}\t{res.description}\n")
                arquivotxt = re.sub('\W', '_', res.name)
                with open('{}.txt'.format(os.path.join(dir_path, arquivotxt)), 'w', encoding='utf-8') as text:
                    try:
                        content = markdown(res.link)
                    except KeyError:
                        content = "Esta pagina ainda nao existe no Web Archive"
                    text.write(content)
        with open('{}.txt'.format(os.path.join(dir_path, "Parâmetros_de_pesquisa")), 'w', encoding='utf-8') as text:
            text.write(
                f"Sites: {sites}\nPalavras Chaves: {pesquisa}\nNumero de paginas: {numeroPag}\n")

    except Exception as err:
        traceback.print_exc()
        #print('Nenhum resultado encontrado. Isso pode ter acontecido por algum erro interno durante a execução do código ou por uma pesquisa muito restrita/específica.')


def markdown(site):
    handler = html2text.HTML2Text()
    handler.ignore_links = True
    url = f"https://archive.org/wayback/available?url={site}"
    jhtml = json.loads(get_html(url).decode('utf-8'))
    html = get_html(jhtml["archived_snapshots"]["closest"]["url"])
    html = html.decode('utf-8')
    md = handler.handle(html)
    return md


pesquisageral(sites, pesquisa, numeroPag, dir_path)
