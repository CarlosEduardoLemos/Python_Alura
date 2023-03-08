url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

paremetro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(paremetro_busca)

indice_valor = indice_parametro + len(paremetro_busca) +1
valor = url_parametros[indice_valor:]

print(valor)