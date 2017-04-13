
''' Binary Search Algorithm '''

def BinarySearch( myarray, myitem):
  first = 0
  last = len(array)
  found = False
  while (first < last):
    midpoint = (last + first)/2
    if (array[midpoint] == x):
      found = True
      break
    elif (x > array[midpoint] ):
      first = midpoint +1
    else:
      last = midpoint - 1
    
  print found
  

array = [6,12,18,24,30,36,42,48,54,60,61,70,77]

y = raw_input("enter search element:")
x = int(y)
BinarySearch(array,x)