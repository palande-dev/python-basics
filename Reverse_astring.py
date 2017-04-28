class Solution():
    
    def reverseString(self,s):
       
        return s[::-1] 
        
    

string = raw_input("enter a string")
Mystring = Solution()
str1 = Mystring.reverseString(string)


print str1
