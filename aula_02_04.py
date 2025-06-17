#Tabuada com Limite Personalizado
#Objetivo: Exibir a tabuada de um número até um limite definido.
#Entrada:

#Um número base (ex.: 3).

#Um limite superior (ex.: 5).
#Saída:

#Tabuada de 1 até o limite (ex.: 3x1=3, 3x2=6, ..., 3x5=15).


def tabuada_limite():
    base = int(input("Digite o número base: "))
    limite = int(input("Digite o limite superior: "))
    i = 1
    while i <= limite:
        print(f"{base} x {i} = {base * i}")
        i += 1
tabuada_limite()