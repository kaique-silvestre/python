from datetime import datetime, timedelta
# Time delta é a diferença entre duas datas 
# É possível conseguir um delta a partir de operações matemática com duas datas 
# É possível também conseguir um delta diretamente a partir da classe "deltatime" sendo que nela podemos personalizar dias, horas, minutos e mais 

here = datetime.now()
delta = timedelta(days=10, hours=10)
print(here + delta)
print(here - delta)

