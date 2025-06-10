from datetime import datetime

# datetime(year, month, day)
# Por ser um número inteiro o zero a esquerda não existe 
date = datetime(2025, 5, 29)


# Utilizando o __repr__ do obj "date" do tipo "datetime"
print(date)
# 2025-05-29 00:00:00
  
##########################################

# Data Completa
# datetime(year, month, day, hour, minutes, seconds)
complete_date = datetime(2025, 5, 29, 11, 15, 00)
print(complete_date)
# 2025-05-29 11:15:00


# Convertendo STRINGS em DATETIME
# datetime.strptime(string_to_parse, date_model)
# Podemos converter uma string que representa uma data em um obj datetime
string = '2025-10-22'
date_formater = '%Y-%m-%d'

new_date = datetime.strptime(string, date_formater)
print(new_date)

string2 = '2025-06-01 15:26:00'
date_formater2 = '%Y-%m-%d %H:%M:%S'

new_date2 = date.strptime(string2, date_formater2)
print(new_date2)

# A conversão é feita utilizando uma string que se deseja converter junto a uma string que contém o modelo de conversão 
# O módelo de cobversão utiliza uma série de código a srem decoradas para transformar a string em um datetime de modelo correto 
# isso permite uma customização na hora de transformar a string conforme sua necessidade 

here = datetime.now()
print(here)