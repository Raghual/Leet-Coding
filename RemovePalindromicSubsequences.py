class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if(n==0):
            return 0
        ind1=0
        ind2=n-1
        while(ind1<ind2):
            if(s[ind1]!=s[ind2]):
                return 2
            ind1+=1
            ind2-=1
        return 1
        
