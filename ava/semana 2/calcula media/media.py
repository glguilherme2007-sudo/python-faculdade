#Variaveis
num1 = 0.0
num2 = 0.0
num3 = 0.0


#Função para leitura
def ler_numeros(): 
 global num1, num2,num3
 num1 = float(input("Digite 1o valor: "))
 num2 = float(input("Digite 2o valor: "))
 num3 = float(input("Digite 3o valor: "))
 print(f"Os numeros lidos são: {num1}, {num2}, {num3}")

#Funçãp para calular soma
def calcular_soma():
 soma = num1 + num2 + num3
 print(f"A soma e: {soma}")

#Função para calcular media
def calcular_media():
 media = (num1 + num2 + num3) / 3
 print(f"A media e: {media}")

#Chamada das funções
ler_numeros()
calcular_soma()
calcular_media() 