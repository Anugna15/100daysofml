my_list=[1,2,3,4,5]
my_list.append(6)
print(my_list)
my_list.insert(0,0)
print(my_list)
my_list.remove(3)
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list.extend([7,8,9])
print(my_list)
my_list2=[6,7,8,9,10]
print(my_list2)
my_list3=my_list+my_list2
print(my_list3)
my_list4=my_list*2
print(my_list4)
my_list5=[x for x in my_list if x%2==0]
print(my_list5)
my_list6=[x**2 for x in my_list]
print(my_list6)
my_list7=[x for x in my_list if x>2]
print(my_list7)
my_list8=[x for x in my_list if x<3]
print(my_list8)
my_list9=[x for x in my_list if x==3]
print(my_list9)
my_list10=[x for x in my_list if x!=3]
print(my_list10)
my_list11=[x for x in my_list if x>=3]
print(my_list11)
my_list12=[x for x in my_list if x<=3]
print(my_list12)