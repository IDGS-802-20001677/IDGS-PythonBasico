'''
leer el numero 5
5x1=5
...
5x10=50
'''

print("Tabla de multiplicar")
num1=int(input('Dame num1: '))

for x in range(1,11):
    print("{} * {} = {}".format(num1,x,(num1*x)))

