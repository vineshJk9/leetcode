class Solution(object):
    l = []
    def letterCasePermutation1(self, s, n):
        s = list(s) 
        if n==0:
            return self.l.append("".join(s))

            
        self.letterCasePermutation1(s, n-1)
        if n>0 and s[n-1].isalpha():
            if s[n-1].islower():
                s[n-1] = s[n-1].upper()
            else:                     
                s[n-1] = s[n-1].lower() 
            self.letterCasePermutation1(s, n-1)
        return self.l
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.letterCasePermutation1(s, len(s))
sol = Solution()
str =  "3z4"
print(sol.letterCasePermutation(str))