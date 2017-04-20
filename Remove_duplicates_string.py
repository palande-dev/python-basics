''' remove duplicates from a string '''


string = 'aaabbccdeeeeeeffgghhh'
arr = list(string)
myString = ""
mydict = {}
for i in range(len(arr)):
  curr = arr[i]
  if not curr in mydict:
    mydict[curr] = 1
    myString += curr
  else:
    mydict[curr]+=1
    
  
print mydict
print myString