class MathOperations:
    def __init__(self,a,b,c=0):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def add(self):
        total = (self.num1 + self.num2 )+ self.num3

        print(f"the sum is : {total}")
    
    
    
numbers = MathOperations(2,3,4)

numbers.add()