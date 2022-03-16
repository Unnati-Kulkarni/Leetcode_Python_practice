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
        s = s.replace(" ","")
        res = ''
        
        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i]
            
        return res[:] == res[::-1]
