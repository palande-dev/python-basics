def Prime(n):
  ''' To convert negative int values to their absolute values '''
  n = abs(n)
  ''' Find square root of n and convert it to a int '''
  r = int(n**0.5)
  if n < 2:
    return "not Prime"
  elif n == 2:
    return "is Prime"
  ''' range starts with 3 and only needs to go up the squareroot of n. for all odd numbers '''  
  for i in range(3,r):
    if n % i == 0:
      return "not Prime"
  return "is Prime"
    
a= int(raw_input("enter a number:"))
print Prime(a)