class Solution:

    def lookup(NumChar):
        lk_table = {}
        lk_table["0"] = 0
        lk_table["1"] = 1
        lk_table["2"] = 2
        lk_table["3"] = 3
        lk_table["4"] = 4
        lk_table["5"] = 5
        lk_table["6"] = 6
        lk_table["7"] = 7
        lk_table["8"] = 8
        lk_table["9"] = 9
        return lk_table[NumChar]

    def getNum(NumString):

        counter = 1

        IntNum = 0

        index = len(NumString)-1

        while(index >= 0):

            IntNum += counter * Solution.lookup(NumString[index])
            index-=1
            counter*=10

        return IntNum

    def multiply(self, num1: str, num2: str) -> str:

        num1 = Solution.getNum(num1)
        num2 = Solution.getNum(num2)

        return str(num1*num2)
