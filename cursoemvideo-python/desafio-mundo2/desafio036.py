# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai pergguntar o *valor da casa*, o *salário* do comprador e em *quantos anos* ele vai pagar 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado 

valor_da_casa = float(input('Coloque o valor da casa : R$'))
anos_para_pagar = float(input('Coloque em quantos anos pretende pagar : ' ))
salario_mensal =float(input('Coloque o valor do salário mensal : R$'))

prestação_mensal = (valor_da_casa / anos_para_pagar) / 12
porcetagem30 = salario_mensal * 0.3

if prestação_mensal <  porcetagem30 : 
    print('Seu financiamento foi aprovado')
    print(f'O valor da sua prestação mensal será de R${prestação_mensal:.2f}, não passando mais de 30% do valor do seu salário sendo esse equivalente á {porcetagem30:.2f} ')
    
else :
    print('Seu financiamento foi negado')
    print(f'Seu financiamento foi negado devido a parcela mensal de {prestação_mensal:.2f} exceder 30% do seu sálario equivalente á {porcetagem30:.2f} ')