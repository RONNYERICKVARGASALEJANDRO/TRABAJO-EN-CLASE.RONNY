class ciclos:
    def __init__(self,num1=5):
        self.numero=num1
    
    def uso_de_while(self):
        car=input("ingrese una vocal: ")
        car=car.lower()
        while car not in('a','e','i','o','u'):
            car=input("ingrese vocal: ").lower()
        print('el caracter({}) es una vocal'.format(car))
            
clase=ciclos()
clase.uso_de_while()
        