from datetime import datetime, timedelta
# Comparação de datas 

date_formater = '%Y/%m/%d'

minor_date = datetime.strptime('2004/10/22', date_formater)
greater_date = datetime.now()

# Operadores Lógicos
print(greater_date == minor_date) # Is it equal 
print(greater_date != minor_date) # Is it different 
print(greater_date > minor_date) # is it minor 
print(greater_date < minor_date) # is it greater

# Operadores matemáticos 
print(greater_date - minor_date)
# Tantos dias en tantas horas de diferanças
# A difrença entre as datas é conhcido como "delta"  

