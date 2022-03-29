#Problem:

'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

#Solution:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        res = 0
        flag = False
        
        if needle == "":
            return 0
        
        while(l <= len(haystack)):
            if haystack[res:l] == needle:
                return res
                flag = True
            else:
                res += 1
                l += 1
                
        if flag == False:
            return -1
       
        
  
