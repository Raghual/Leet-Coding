20. Valid Parentheses
Easy

6039

248

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        flag=1
        if(len(s)==1):
            return False
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                stack.append(s[i])
            else:
                if(len(stack)!=0):
                    if(s[i]==')' and stack[-1]=='(' or s[i]=='}' and stack[-1]=='{' or s[i]==']' and    stack[-1]=='['):
                        stack.pop()
                    else:
                        flag=0
                        break
                else:
                    flag=0
                    break
        if(len(stack)==0 and flag==1):
            return True
        else:
            return False
                
            






















