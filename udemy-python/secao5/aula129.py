class Calculator:
    
    @staticmethod
    def soma(*value):
        result = 0
        for i in value:
            result += i
        return result
    
var = Calculator.soma(100, 100, 100, 100, 100)
print(var)