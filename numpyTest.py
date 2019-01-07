import numpy as np
#1
'''
arr = np.array([1,2,3,4])
reversed_arr = arr[::-1]
print(reversed_arr)
'''
#2
'''
arr = np.array(['S','T','O','R','M','I','N','G',' ','R','O','B','O','T','S'])
d = input("Words ")
arr = np.delete(arr,int(d)-1)
print(arr)
'''
#3
'''
arr = [1,2,3,4,5,6,7,8,9]
d = input("Words ")
arr = np.delete(arr,int(d)-1)
print(arr)
'''
'''
a = np.full((2,3),True)
print(a)
'''
'''
a = np.zeros((2, 3))
print(a)
print( a.reshape(1,6), np.ndim(a) )
print( a.reshape(3,2))
'''
'''
a = np.array([1,2,3,4])
print (a, "dim:", a.ndim, "shape: ", a.shape)
'''
'''
x = [1,23,5,6,7,4,3,1,5,56,7,4,3,2,45,67,4,34,37,23456,234523,]
print(x)
s = slice(0,100000,5)
print(x[s])
'''
'''
structure = np.dtype([('oranges',np.int8)])
array = np.array([(11),(20),(45),(469)],dtype=structure)
#print(a)
print(a['oranges'])
'''
'''
x = [1,2,3,4,5,6,7,8,9]
y = x[2:8:2]
print(y)
'''
'''
array = np.zeros((7,9))
array[1:3,1:4] = np.full((2,3),1)
print(array)
'''
#4
'''
array = [[1,2,3],[4,5,6],[7,8,9]]
array = array[::-1]
print(array)
'''
#5
'''
arr = [[1,2,3],[4,5,6]]
a = np.reshape(arr,(3,2),order='F')
print(a)
'''
#7
'''
array = [1,2,3,4,5,6]
arr = np.reshape(array, (2,3))
print(arr)
'''
#8
'''
c = np.array([0,12,45,21,34,99.91])
f = []
c = (c-30)*(5/9)
print(c)
'''
#9
'''
arr = [[4,5,6,7],[8,9,10,11]]
array = [0,1,2,3]
k = []
for i in arr:
    k = np.append(k,i[0:5:1])
k = np.append(k,array)
print(k)
'''
#18
'''
a=[1,2]
b=[4,5]
if (a>b)==True:
    print("a is big")
elif (a>=b)==True:
    print("greater than or equals")
elif (a < b)==True:
    print("b is big")
else:
    print("b is big or equal")
'''
#14
'''
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = np.array([10, 30, 40, 50, 70])
print("Array2: ",array2)
print("Unique Values are: ")
print(np.setxor1d(array1,array2))
'''
#15
'''
a = [0,10,20,40,60,80]
b = [10,30,40,50,70]
print(np.union1d(a,b))
'''
#16
'''
a = [1,2,3,4]
print(np.repeat(a,2))
'''













