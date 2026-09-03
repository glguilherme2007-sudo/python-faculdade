# valores
# 1	Consulta médica	R$ 180,00
# 2	Psicologia	R$ 150,00
# 3	Nutrição	R$ 120,00
# 4	Fisioterapia	R$ 100,00=

#Entrada de dados
nome = input("Digite o nome do paciente: ")
idade = int(input("Digite sua idade: "))

#codigos de atendimentos
print("\nCódigos de Atendimento: ")

print("1-Consulta médica (R$ 180,00)")
print("2-Psicologia	(R$ 150,00) ")
print("3-Nutrição (R$ 120,00) ")
print("4-Fisioterapia (R$ 100,0) ")

codigo = int(input("Digite o codigo de atendimento (1 a 4): "))
convenio = input("Possui convenio? (S/N:)")

if codigo == 1:
 atendimento = "Consulta Medica"
 valor = 180

elif codigo == 2:
  antendimento =  "Psicologia"
  valor = 150

elif codigo == 3:
  antendimento = "Nutrição"
  valor = 120

elif codigo == 4:
  antendimento = "Fisioterapia"
  valor = 100

#idade

if idade < 12 or idade >=60:
  prioritario = True
else:
  prioritario = False  

#convenio

if convenio == "S" and prioritario == True:
  Desconto = 0.25
     


