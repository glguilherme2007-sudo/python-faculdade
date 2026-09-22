continuar = "s"

Digite_nome = input("Digite o nome do aluno: ")
soma = 0.0
contador = 0

while continuar == "s":
    nota = float(input("Digite sua nota: "))

    soma = soma + nota
    contador =  contador + 1

    continuar = input("Deseja inserir mais alguma nota? (s/n)")

media = soma / contador
print(f"A media do(a) aluno(a) {Digite_nome} e: {media}")