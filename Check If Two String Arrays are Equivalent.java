 Check If Two String Arrays are Equivalent
 
 class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1=""
        str2=""
        for i in range(0,len(word1)):
            str1=str1+word1[i]
        for j in range(0,len(word2)):
            str2=str2+word2[j]
        if(str1==str2):
            return True
        else:
            return False
        
