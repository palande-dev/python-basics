class Solution(object):
    def isAnagram(self, s, t):
      found = False
      arr1 = list(s)
      arr2 = list(t)
      Mydict1 = {}
      Mydict2 = {}
      
      for i in range (len(arr1)):
        curr1 = arr1[i]
        if not curr1 in Mydict1:
          Mydict1[curr1] = 1
          
        else:
          Mydict1[curr1]+=1
          
      print Mydict1
      
      
      for i in range (len(arr2)):
        curr2 = arr2[i]
        if not curr2 in Mydict2:
          Mydict2[curr2] = 1
          
        else:
          Mydict2[curr2]+=1
          
      print Mydict2
      
      if Mydict1 == Mydict2:
        found = True
        
      else:
        found = False
        
      return found
      
        
Mystring = Solution()
print Mystring.isAnagram("car","rac")