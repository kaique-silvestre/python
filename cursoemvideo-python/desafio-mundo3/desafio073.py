# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação, depois mostre:
# a) Apenas os 5 primeiros colocados 
# b) Os últimos 4 colocados 
# c) Uma lista com todos os times em ordem alfabetica 
# d) Em que posição da tabela está o time da chapecoense  

brasileirão = ( 'Flamengo', 'Palmeiras', 'Botafogo', 'Bahia', 'athletico-PR', 'São Paulo', 'Cruzeiro', 'Fortaleza', 'Red bull bragantino', 'Internacional', 'Atlético-MG', 'juventude', 'Criciúma', 'Cuiaba', 'Vitória', 'Vasco da Gama', 'Atlético-GO', 'Grêmio', 'corinthias', 'fluminense', 'chapecoense')

print('=-'*40)
print(brasileirão[:5])
print('=-'*40)
print(brasileirão[-5:-1])
print('=-'*40)
print(sorted(brasileirão))
print('=-'*40)

for pos, i in  enumerate(brasileirão):
    if i == 'chapecoense':
        print(f'{i} está na posição: {pos+1}º')

# Chapecoense não está no brasileirão 2024, portanto por fins de resolução coloquei ele como o time 21