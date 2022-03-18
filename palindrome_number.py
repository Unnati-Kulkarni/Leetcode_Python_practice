#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is a palindrome while 123 is not.

#Example 1:

#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

#Example 2:

#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Code:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num1 = x
        if x<0:
            return False
        
        while(x != 0):
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
            
        return num1==rev
      
#Another approach:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = a[::-1]
        
        if a == b:
            return(True)
