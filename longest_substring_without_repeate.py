#Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Code:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = len(set(s))
        
        if x <= 1:
            return x
        
        while x > 1:
            d = len(s) - x
            for i in range(0, d+1):
                if len(set(s[i:x+i])) == x:
                    return x
                    break
                else:
                    pass
           
            if len(set(s[i:x+i])) == x:
                break
            else:
                x = x -1
            
    
