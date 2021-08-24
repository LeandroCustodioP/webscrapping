from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


'''def obtendo_tag(url,tag1):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    # devolve null, executa um break ou algum outro "Plano B"
    # Tratando URLError
    except URLError as e:
        print('Este servidor não pode ser encontrado.')
    else:
# o programa continua. Nota: se você retornar ou executar um break no
# catch da exceção, não será necessário usar a instrução "else"
        try:
            bs = BeautifulSoup(html.read(), tag1.read(), 'html.parser')
            if tag1 in  html:
                tag_desejada = bs.tag1
        
        # Tratando AttributeError
        except AttributeError as e:
            print('Tag não encontrada.')
        else:
            if tag_desejada == 'none':
                print('tag não encontrada')
            else:
                print(tag_desejada)
    

url = input('Digite o site: ')
tag1 = input('Digite a tag buscada: ')

obtendo_tag(url,tag1)'''

url = 'http://www.g1.globo.com'

# Tratando HTTPError
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
# devolve null, executa um break ou algum outro "Plano B"

# Tratando URLError
except URLError as e:
    print('Este servidor não pode ser encontrado.')
else:
# o programa continua. Nota: se você retornar ou executar um break no
# catch da exceção, não será necessário usar a instrução "else"

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        tag_desejada = bs.head
    # Tratando AttributeError
    except AttributeError as e:
        print('Tag não encontrada.')
    else:
        if tag_desejada == 'none':
            print('tag não encontrada')
        else:
            print(tag_desejada.prettify())
