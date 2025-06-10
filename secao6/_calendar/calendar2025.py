import calendar

# Calendário do ano

# Calendário completo de 2025
#print(calendar.calendar(2025))

# Calendário de um mês em especifico 
print(calendar.month(2025, 10))


# Último dia de qualquer mês 
print(calendar.monthrange(2025, 10))
# retorna o nome do primeiro dia do mês e o número da data do última dia do mês  

# Para saber o número do dia da semana do dia em questão 
"""
Lembrando que:
0 = Segunda até 6 = Domingo 
"""
print(calendar.weekday(2025, 10, 22))