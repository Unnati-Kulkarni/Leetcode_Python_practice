#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#CODE:

class Solution:
    def reverse(self, x: int) -> int:
        if x in range(-2 ** 31, (2 ** 31)):
            if x >= 0:
                s = str(x)
                s = s[::-1]
                if int(s) in range(-2 ** 31, (2 ** 31)):
                    return int(s) 
                else:
                    return 0
            else:
                s = str(-1 * x)
                s = s[::-1]
                if int(s) in range(-2 ** 31, (2 ** 31)):
                    return -1 * int(s)
                else:
                    return 0
        else:
            return 0
        
