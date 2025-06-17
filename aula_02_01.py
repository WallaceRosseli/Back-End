#1. Validador de Senha
#Objetivo: Criar um programa que valide uma senha de acordo com regras específicas.
#Requisitos: 

#A senha deve ter pelo menos 8 caracteres.
#Deve conter pelo menos 1 número.
#Deve conter pelo menos 1 letra maiúscula.

#Saída:

#Mensagens específicas indicando qual regra falhou (se aplicável).
#"Senha válida!" se atender a todos os critérios.

def validador_senha(): 

    senha = input("Digite a senha: ")
    
    temNumero = False 
    temMaiuscula = False
    
    for c in senha:
        if c.isdigit(): #isdigit() verifica se o caractere eh um numero
            temNumero = True
        if c.isupper(): #isupper() verifica se o caractere eh maiusculo
            temMaiuscula =True 
    
    if len(senha) < 8: #len() verifica o comprimento da string
        print("A senha deve ter pelo menos 8 caracteres.")
    if not temNumero:
        print("A senha deve conter pelo menos 1 número.")
    if not temMaiuscula:
        print("A senha deve conter pelo menos 1 letra maiúscula.")
    if len(senha) >= 8 and temNumero and temMaiuscula: 
        print("Senha válida!")

validador_senha()