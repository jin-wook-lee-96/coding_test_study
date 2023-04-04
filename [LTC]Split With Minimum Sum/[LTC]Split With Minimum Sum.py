class Solution:
    def splitNum(self, num: int) -> int:
        num = list(map(int,str(num)))
        num.sort()
        num1, num2 = int(''.join(map(str,num[0::2]))), int(''.join(map(str,num[1::2])))
        return num1+num2