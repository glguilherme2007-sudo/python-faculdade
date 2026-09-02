n1 = float(input("digite o numero: "))
n2 = float(input("digite o numero: "))
n3 = float(input("digite o numero: "))

if n1>= n2 and n1>= n3:
   maior = n1

elif n2>=n1 and n2 >= n3:
   maior = n2

else:
   maior = n3

print (f"O maior numero e: {maior}")

