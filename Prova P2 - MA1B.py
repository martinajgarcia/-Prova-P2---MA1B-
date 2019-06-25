#ex1
def resumir(texto):
    lista = texto.split
    if len(lista) > 140:
        for k in range (0, 140):
            print (lista[i],'...')
    else:
        for k in range (0, len(lista)):
            print (lista[i])
    return lista

#ex3
dic = {'2013': {'filmes': ['Frozen'], 'us$': [1276480335]},
       '2012': {'filmes': ["Marvel's The Avengers"], 'us$':[1518812988]},
       '1997': {'filmes': ['Titanic'], 'us$': [2187463944]},
       '2018': {'filmes': ['Black Panther', 'Avengers: Infinity War', 'Jurassic World: Fallen Kingdom'], 'us$': [1346913161, 2048359754, 1309484461]},
       '2015': {'filmes': ['Avengers: Age of Ultron', 'Star Wars: The Force Awakens', 'Furious 7', 'Jurassic World'], 'us$': [1405403694, 2068223624, 1516045911, 1671713208]},
       '2009': {'filmes': ['Avatar'], 'us$': [2787965087]},
       '2017': {'filmes': ['Star Wars: The Last Jedi', 'Beauty and the Beast'], 'us$': [1332539889, 1263521126]},
       '2011': {'filmes': ['Harry Potter and the Deathly Hallows – Part 2'], 'us$': [1341693157]},
       '2019': {'filmes': ['Avengers: Endgame'], 'us$': [2750667499]}}
print (dic)

#ex4
print ('valor arrecadado em 2013: US$', dic['2013']['us$'])
print ('valor arrecadado em 2012: US$', dic['2012']['us$'])
print ('valor arrecaado em 1997: US$', dic['1997']['us$'])
a = dic['2018']['us$'][0] + dic['2018']['us$'][1] + dic['2018']['us$'][2]
b = dic['2015']['us$'][0] + dic['2015']['us$'][1] + dic['2015']['us$'][2] + dic['2015']['us$'][3]
print ('valor arrecadado em 2018: US$', a)
print ('valor arrecadado em 2015: US$', b)

print ('valor arrecaado em 2009: US$', dic['2009']['us$'])
c = dic['2017']['us$'][0] + dic['2017']['us$'][1]
print ('valor arrecadado em 2017: US$', c)

print ('valor arrecaado em 2011: US$', dic['2011']['us$'])
print ('valor arrecaado em 2019: US$', dic['2019']['us$'])
