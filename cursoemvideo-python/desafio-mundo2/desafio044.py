# Elabore um programa que calcule o valor do produto, considerando o seu *Preço normal* e *condição de pagamento* 
# - à vista dinheiro/cheque 10% de desconto 
# - À vista no cartão 5% de desconto 
# - em até 2x no cartão : preço normal 
# - 3x ou mais no cartão : 20% de juros 

preço = float(input('Coloque o preço : R$ '))
pagamento = int(input("""
Coloque [ 1 ] - dinheiro/cheque
Coloque [ 2 ] - Cartão a vista 
Coloque [ 3 ] - 2x no cartão 
coloque [ 4 ] - 3x no cartão 
"""))

if pagamento == 1 :
    preço = preço - (preço * 0.1)
    print(preço)
elif pagamento == 2 :
    preço = preço - (preço * 0.05)
    print(preço)
elif pagamento == 3 : 
    print(preço)
elif pagamento == 4 :
    preço = preço + (preço * 0.2)
    print(preço)
else : 
    print('ERRO. TENTE NOVAMENTE')