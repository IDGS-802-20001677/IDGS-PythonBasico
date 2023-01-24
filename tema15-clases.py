import os

class OperasBas:
    #declaración de propiedades
    num1=0
    num2=0
    res=0
    #declaración de constructor
    def __init__(self, a, b):
        self.num1=a
        self.num2=b

    
     #declaración de métodos de clase
    def suma(self):
        #num1=12
        #num2=10
        self.res = self.num1 + self.num2
        print("la suma es: {}".format(self.res))

    def resta(self):
        #num1=12
        #num2=10
        self.res = self.num1 - self.num2
        print("la resta es: {}".format(self.res))

    def multiplicacion(self):
        #num1=12
        #num2=10
        self.res = self.num1 * self.num2
        print("la multiplicación es: {}".format(self.res))

    def division(self):
        #num1=12
        #num2=10
        self.res = self.num1 / self.num2
        print("la división es: {}".format(self.res))
    
    

def main():
    os.system('cls')
    op=0

    while op !=5:
        
        print("Menu")
        print("1-suma")
        print("2-resta")
        print("3-multiplicación")
        print("4-división")
        print("5-salir")
        print("")

        op=int(input('Dame operacion: '))
        if op < 5:
            num1=int(input('Dame primer número: '))
            num2=int(input('Dame segundo número: '))
            obj = OperasBas(num1, num2)
        if op==1:
            os.system('cls')
            obj.suma()
        elif op==2:
            os.system('cls')
            obj.resta()
        elif op==3:
            os.system('cls')
            obj.multiplicacion()
        elif op==4:
            os.system('cls')
            obj.division()
        else:
            print("termino")
            break


    

        

if __name__ == "__main__":
        main()

   


