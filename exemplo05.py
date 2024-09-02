notas = [5, 10, 3.4, 8, 3.8]

#Função regular para calcular a media 
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

#Função lambda para arrendodar a media para duas casas decimais 
arrendodar_media = lambda media : round(media, 2)

#Calcular a media
media = calcular_media(notas)
media_arrendondada = arrendodar_media(media)

#verificar se os alunos foram aprovados
situacao = "aprovado" if media_arrendondada >= 7 else "reprovado"

#resultados
print("Notas dos estudantes:", notas)
print("media das notas:", media_arrendondada)
print("situação do aluno", situacao)