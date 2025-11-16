print('Bem-vindo a empresa. Digíte suas credencias para ser autorizado')
pessoa = str(input('Nome ou credencial : ')).strip().upper()

if pessoa == 'KAIQUE' : 
    print('Olá, senhor chairman do supermarket, vamos liberar o acesso para você.')
elif pessoa == 'HELOISA' :
    print('Olá Dama da empresa, bem-vinda')
elif pessoa == 'SAMUEL' :
    print('Olá senhor samuel vacilão, O senhor kaique te autoriza entrar')
elif pessoa == '0000' :
    print('Olá senhor diretor financeiro do supermarket, o acesso a sua sala está liberado')
elif pessoa == '1111' : 
    print('Olá senhor do conselho administrativo da empresas')
else : 
    print('Credenciais não conhecidas, acesso negado.')