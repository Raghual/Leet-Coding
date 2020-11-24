class Solution(object):
    def kWeakestRows(self, mat, b):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        m=len(mat)
        n=len(mat[0])
        l=[]
        for i in range(0,m):
            count=0
            for j in range(0,n):
                if(mat[i][j]==1):
                    count+=1
            l.append(count)
        k=[]
        for i in range(0,m):
            k.append(i)
        for i in range(0,m-1):
            for j in range(i+1,m):
                if(l[i]>l[j]):
                    l[i],l[j]=l[j],l[i];
                    k[i],k[j]=k[j],k[i]
                elif(l[i]==l[j] and k[i]>k[j]):
                    l[i],l[j]=l[j],l[i];
                    k[i],k[j]=k[j],k[i]
        return k[0:b]
                    
