#Given a string s, return the longest palindromic substring in s.

#Example:
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

#Code:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_diff = 0
        i = 0
        j = len(s) - 1
        res = ''
        
        if len(s) == 1:
            return s
        
        while i<(len(s)):
            while i<j:
                if s[j] == s[i]:
                    break
                else:
                    j -= 1
           
            new = s[i:j+1]
    
                
            if new == new[::-1]:
                if ((j-i) > max_diff):
                    max_diff = j - i
                    res = s[i:j+1]
            else:
                j -= 1
                continue
             
            i = i + 1
            j = len(s)-1
        
        if res == '':
            return s[0] 
        else:
            return res
