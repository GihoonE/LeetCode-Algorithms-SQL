class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        for i in range(1,x//2+2):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
            else:
                continue