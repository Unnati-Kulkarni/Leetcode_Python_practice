#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
#removing all non-alphanumeric characters, it reads the same forward and backward. 
#Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

#Example:
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

#Code:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        without_space = s.replace(" ","")
        res = ''
        
        for i in range(len(s)):
            let = s[i]
            if let.isalnum():
                res += let
            
        if res[:] == res[::-1]:
            return True
        else:
            return False
