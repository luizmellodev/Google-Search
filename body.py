from google.modules.utils import get_html
import html2text
import json

def markdown(site):
    handler = html2text.HTML2Text()
    handler.ignore_links = True
    url = f"https://archive.org/wayback/available?url={site}"
    jhtml = json.loads(get_html(url).decode('utf-8'))
    html = get_html(jhtml["archived_snapshots"]["closest"]["url"])
    html = html.decode('utf-8')
    md = handler.handle(html)
    return md

# Estadão tá com um novo site (link.estadao.com.br)
