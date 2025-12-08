class Solution(object):
    l = []
    def letterCasePermutation(self, s, n):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s) 
        if n==0:
            return self.l.append("".join(s))

            
        self.letterCasePermutation(s, n-1)
        if n>0 and s[n-1].isalpha():
            if s[n-1].islower():
                s[n-1] = s[n-1].upper()
            else:                     
                s[n-1] = s[n-1].lower() 
            self.letterCasePermutation(s, n-1)
        return self.l
sol = Solution()
str =  "3z4"
print(sol.letterCasePermutation(str, len(str)))