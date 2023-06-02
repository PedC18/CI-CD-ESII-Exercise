class calculator:
    def __init__(self):
        pass

    def soma(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def multi(self,a,b):
        return a*b
    
    def div(self,a,b):
        if b == 0:
            return "error, can't divide by zero"
        return a / b
    
    def power(self,a,b):
        return pow(a,b)

