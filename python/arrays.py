'''
my_list=[1,2,3,4,5]
print(my_list)

#append-end of the list
my_list.append(3)
print(my_list)

#insert-insert into perticular index
my_list.insert(2,1)
print(my_list)

#remove-used to remove specific index
my_list.remove(1)
print(my_list)
print(my_list.__len__())

my_list[2]=10
print(my_list)

my_list[1:3]
print(my_list)

#Create a program that reads two vectors of integers of the same size and displays a new vector with the sum of the corresponding elements of the two vectors.
n=int(input("enter length of the vector :"))
vector1=[]
vector2=[]
print("elements of 1st vector")
for i in range(n):
    element=int(input("elements {} ".format(i+1)))
    vector1.append(element)
print("elements of 2nd vector")
for i in range(n):
    element=int(input("elements {} ".format(i+1)))
    vector2.append(element)
resultant=[]
for i in range(n):
    resultant.append(vector1[i]+vector2[i])
print(resultant)

#is ascending
n=int(input("no of elements"))
array=[]
for i in range(n):
    ele=int(input("element {} ".format(i+1)))
    array.append(ele)
is_ascending=True
for i in range(1,n):
    if array[i]<array[i-1]:
        is_ascending=False
        break
if is_ascending==True:
    print("the list is in ascending order")
else:
    print("not...!")


#reverse
n=int(input("no of elements "))
array=[]
for i in range(n):
    ele=int(input("element {} ".format(i+1)))
    array.append(ele)
start=0
end=n-1
while start<end:
    array[start],array[end]=array[end],array[start]
    start+=1
    end-=1
print("elemets in reverse order")
for ele in array:
    print(ele)

#Create a program that reads an array of integers and displays the sum of all the elements..
n=int(input("enter size of array : "))
array=[]
for i in range(n):
    ele=int(input('element {} '.format(i+1)))
    array.append(ele)

sum=0
for i in array:
    sum+=i
print(sum)

#finding largest number in the array
n=int(input("enter size of array : "))
array=[]
for i in range(n):
    ele=int(input('element {} '.format(i+1)))
    array.append(ele)
largest=array[0]
for i in range(1,n):
    if array[i]>largest:
        largest=array[i]
print("largest element is : ",largest)

#finding average of the array
n=int(input("enter size of array : "))
array=[]
for i in range(n):
    ele=int(input('element {} '.format(i+1)))
    array.append(ele)
sum=0
for i in array:
    sum+=i
average=sum/n
print("average of n elements in the array is : ",average)


#Write a program that reads an array of integers and displays how many times a specific number appears in the array
n=int(input("enter size of array : "))
array=[]
for i in range(n):
    ele=int(input('element {} '.format(i+1)))
    array.append(ele)
target=int(input("enter target element "))
count=0
for i in array:
    if target==i:
        count+=1
print("the target element ",target,"apperead",count,"times")
'''
