# valores
# 1	Consulta médica	R$ 180,00
# 2	Psicologia	R$ 150,00
# 3	Nutrição	R$ 120,00
# 4	Fisioterapia	R$ 100,00=

#repetição
totalpaciente = 0
totalatendimento = 0
totalconvenio = 0
fatbruto = 0
fatliquido = 0
totaldesc = 0
maior = 0
menor = 0
continuar = "s"
while continuar == "s":
 

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
  print()

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

  if convenio == "s" and prioritario == True:
    desconto = 0.25
    

  elif convenio == "s" and prioritario == False:
    desconto = 0.20
    

  elif convenio == "n" and prioritario == True:
    desconto = 0.05
    

  else:
    desconto = 0

  #calculo paciente
  custo = valor - (valor * desconto) 

  print(f"Voce devera pagar: {custo:.2f}")


  #acumulo
  totalpaciente = totalpaciente + 1
  fatbruto += valor 
  
  if convenio == "s":
    totalconvenio = totalconvenio +1

  if prioritario == True:  
   totalatendimento = totalatendimento + 1

  if totalpaciente == 1:
    maior = custo
    menor = custo
  else:
    if custo > maior:
      maior = custo
    if custo < menor:
      menor = custo    
   

  totaldesc += (valor * desconto)  
  
  print()

 #continuar
  continuar = input("Deseja cadastrar outro paciente? (S/N):").lower() 

fatliquido = fatbruto - totaldesc

if totalpaciente> 0:
  media = fatliquido/  totalpaciente
else:
  media = 0   

if fatliquido <= 500:
  classificacao = "movimento baixo"  
elif fatliquido <= 1500:
  classificacao = "movimento moderado"
else:
  classificacao = "movimento alto"   

#exibir acumulo
print(f"O total de pacientes foi: {totalpaciente:}")
print(f"O total de atendimentos prioritarios foi de: {totalatendimento:}")
print(f"O total de pacientes com convenio foi: {totalconvenio:}")
print(f"O faturamento bruto foi de: {fatbruto:.2f}")
print(f"O faturamento liquido foi de: {fatliquido:.2f}")
print(f"o total de descontos aplicados foram de: {totaldesc:.2f}")
print(f"Classificação do movimento: {classificacao}")
print(f"O maior valor pago foi: {maior:.2f}")
print(f"O menor valor pago foi: {menor:.2f}")
print(f"A media foi: {media:.2f}")

 
         


