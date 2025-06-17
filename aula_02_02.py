#Classificador de Notas
#Objetivo: Classificar uma nota em categorias pré-definidas.
#Funcionamento:

#Solicitar ao usuário uma nota entre 0 e 10 (validar a entrada).

#Classificar conforme:

#9 a 10: "Excelente"

#7 a 8: "Bom"

#5 a 6: "Regular"

#0 a 4: "Insatisfatório"
#Observação: Repetir a solicitação até que a nota seja válida.



def classificador_notas(): #Definindo a funcao
    nota = 0
    while nota < 5:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if nota < 5:
            print("Insuficiente, tente novamente.")
    if nota >= 9 and nota <= 10:
        print("Excelente")
    elif nota == 7 or nota == 8:
        print("Bom")
    else:
        print("Regular")

classificador_notas()
