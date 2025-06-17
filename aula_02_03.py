#Soma de Números Ímpares
#Objetivo: Calcular a soma dos números ímpares em um intervalo.
#Entrada: Dois números inteiros (início e fim).
#Saída:

#Soma de todos os números ímpares no intervalo (incluindo os extremos, se forem ímpares).
#Exemplo:

#Entrada: 3 e 7 → Saída: 15 (3 + 5 + 7).



def soma_impares():
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))
    soma = 0
    i = inicio
    while i <= fim:
        if i % 2 != 0:
            soma += i
        i += 1
    print(f"Soma dos ímpares: {soma}")




#soma_impares()