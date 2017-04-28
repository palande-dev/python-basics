''' Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.'''
class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = False
        arr = list(nums)
        Mydict = {}
        
        for i in range (len(arr)):
            curr = arr[i]
            if not curr in Mydict:
                Mydict[curr] = 1
            else:
               Mydict[curr]+=1
        print "Mydict is ",Mydict
                
        arr1 = list(Mydict.values()) 
        print "values are ",arr1
        for i in range (len(arr1)):
            if arr1[i] > 1:
                print arr1[i]
                duplicate = True
                break
            else:
                duplicate = False
                
        return duplicate
        

Mylist = Solution()
print Mylist.containsDuplicate([1,2,3,1])