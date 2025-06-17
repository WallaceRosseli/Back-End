#Contador de Frequência de Letras
#Objetivo: Contar a ocorrência de cada letra em uma frase.
#Regras:

#Ignorar espaços.

#Tratar letras maiúsculas/minúsculas como iguais (case-insensitive).
#Saída:

#Exibir cada letra e sua frequência (ex.: "a: 3", "b: 1").


def contador_frequencia():

    frase = input("Digite a frase: ").lower()
    freq = {} #criando um dicionário 
    frase = frase.replace(" ", "") #removendo os espaços
    for letra in frase:
        freq[letra] = freq.get(letra, 0) + 1 #get() retorna o valor associado a uma chave
    for letra, count in sorted(freq.items()): #sorted() ordena o dicionário 
        print(f"{letra}: {count}")

contador_frequencia()