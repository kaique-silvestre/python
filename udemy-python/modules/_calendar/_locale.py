import calendar
import locale 

# Internaciolização do Código 
# Podemos fazer a tradução do código usando o módulo LOCALE 
# Neste caso iremos trazer o código para o idioma padrão do sistema



# Usando o módulo LOCALE, a função SETLOCALE colocamos como primeiro parâmetro 'locale.' a partir daí podemos configurar quais itens queremos que sejam traduzidos como 
## .LC_ALL
## .LC_TIME
## .LC_MONETARY
## .LC_NUMERIC 

# E para setter o idioma padrão como o local do sistema, usamos como o parâmetro seguinte '', aspas vazias

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2025))