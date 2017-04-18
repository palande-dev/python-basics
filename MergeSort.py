''' Merge Sort algorithm '''

def MergeSort(array):
  if len(array)== 0 or len(array) == 1:
    return array
  else:
    middle = len(array)/2
    a = MergeSort(array[:middle])
    b = MergeSort(array[middle:])
    return merge(a,b)
  
def merge(a,b):
  c= []
  while len(a)!=0 and len(b)!= 0:
    if a[0] > b[0]:
      c.append(b[0])
      b.remove(b[0])
    else:
      c.append(a[0])
      a.remove(a[0])
      
  if len(a)==0:
      c+=b
  else:
      c+=a
      
  return c
  
 
Myarray = [10,5,11,15,18,8,9,67,7]
print Myarray
print MergeSort(Myarray)
