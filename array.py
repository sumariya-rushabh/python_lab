"""#Q1. len()- no of elements
from array import array
arr=array('i',[1,2,3,4,5])
print(len(arr)) #5


#Q2. append(x)- add element at the end
from array import array
arr=array('i',[10,20,30,40,50])
arr.append(60)
print(arr) #array('i', [10, 20, 30, 40, 50, 60])


#Q3. insert(pos,x)- insert at position
from array import array
arr=array('i',[10,20,40,50])
arr.insert(2,30) #insert 30 at position 2
print(arr) #array('i', [10, 20, 30, 40, 50])


#Q4. remove(x)- remove first occurrence of x
from array import array
arr=array('i',[10,20,30,40,50,20])
arr.remove(20) #remove 20 from array
print(arr) #array('i', [10, 30, 40, 50, 20])


#Q5. pop()- remove and return last element
from array import array
arr=array('i',[10,20,30,40,50])
last_element=arr.pop()
print(last_element) #50
print(arr) #array('i', [10, 20, 30, 40])


#Q6. index(x)- Find the index of element x
from array import array
arr=array('i',[10,20,30,40,50])
index_of_30=arr.index(30)
print(index_of_30) #2


#Q7. count(x)- Count occurrences of x
from array import array
arr=array('i',[10,20,30,40,50,20])
count_of_20=arr.count(20)
print(count_of_20) #2


#Q8. reverse()- Reverse the array
from array import array
arr=array('i',[10,20,30,40,50])
arr.reverse()
print(arr) #array('i', [50, 40, 30, 20, 10])
"""