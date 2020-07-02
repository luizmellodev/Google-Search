from google.modules.utils import get_html
import html2text

handler = html2text.HTML2Text()
handler.ignore_links = True


url = "https://link.estadao.com.br/noticias/inovacao,as-pessoas-estao-repensando-suas-casas-diz-presidente-do-quinto-andar,70003324028"
html = get_html(url)
html = html.decode('utf-8')
md = handler.handle(html)
print(md)