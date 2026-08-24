#perguntar o valor gasto com cada alimeto (4)

#informar o percentual

feijao = float(input("digite o valor:"))

macarrao = float(input("digite o valor:"))

arroz = float(input("digite o valor:"))

farinha = float(input("digite o valor:"))

#soma total

soma = (feijao + macarrao + arroz + farinha)

#calculo do percentual

perc_feijao = (feijao / soma) * 100
perc_macarrao = (macarrao / soma) * 100
perc_arroz = (arroz / soma) * 100
perc_farinha = (farinha / soma) * 100


#exibir o percentual
print(f"Total geral gasto: R$ {soma:.2f}")
print("-" * 30)

print(f"Percentual do feijao: {perc_feijao:.2f}")
print(f"Percentual do macarrao: {perc_macarrao:.2f}")
print(f"Percentual do arroz: {perc_arroz:.2f}")
print(f"Percentual do farinha: {perc_farinha:.2f}")