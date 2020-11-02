Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.




class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            rev_num=0
            safe=x
            while(x>0):
                rev_num=rev_num*10+(x%10)
                x//=10
            if(safe==rev_num):
                return True
            else:
                return False
                
        
