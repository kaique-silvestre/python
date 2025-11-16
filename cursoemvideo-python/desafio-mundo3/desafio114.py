# Crie um código em Python que teste se o site pudim está acessivel pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')

except urllib.error.URLError:
    print('O site não está acessivel no momento')
else: 
    print('O site está acessivel no momento')