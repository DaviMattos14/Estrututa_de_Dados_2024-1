numero = int(input())
binario = int(0)
p = 0

while numero > 0:
    binario += ((numero % 2) * (pow(10,p)))
    numero = int((numero - (numero % 2))/2)
    p += 1
print(binario)

#------------------------------------------------#

for numero in range(21):
    n = numero
    binario = 0
    p=0
    while n > 0:
        binario += ((n % 2) * (pow(10,p)))
        n = int((n - (n % 2))/2)
        p += 1
    print(numero, " = ", binario)
