class Solution:
    def addDigits(self, num: int) -> int:
        
        def sum(number):
            if (number<10):
                return number
            else:
                a = int(number / 10)
                b = int(number % 10)
                
                sums = a + b
                
                x = sum(sums)
                
                return x
            
        return sum(num)
