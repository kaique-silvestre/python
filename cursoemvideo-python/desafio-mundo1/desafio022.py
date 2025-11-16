# Crie um programa que leia o nome completo de uma pessoa e mostre : 
# • O nome com todas as letras maiúsculas 
# • o nome com todas as letras minusculas  
# • Quantas letras ao todo ( sem considerar espaços )
# • Quantas letras tem o primeiro nome

nome = str(input('Digíte seu nome completo : ')).strip()
print(f'O seu nome em letras maiúsculas : {nome.upper()}')
print(f'O seu nome em letras minusculas : {nome.lower()}')
print(f'O seu nome tem ao todo : {len(nome.replace(" ", ""))} letras')
print(f'O seu primeiro nome tem ao todo : {nome.find(" ")} letras')
    
    
    
