url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrompe = url.find("?")
url_base = url[:indice_interrompe]
print(url_base)

url_parametros = url[indice_interrompe+1:]
print(url_parametros)
