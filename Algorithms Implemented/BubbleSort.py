''' Bubble Sort Algorithm '''

def BubbleSort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - 1):
        if (array[j]> array[j+1]):
        temp = array[j]  
        array[j] = array[j+1]
        array[j+1] = temp
      
  print "Sorted array is : ", array
    

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array
BubbleSort(num_array)