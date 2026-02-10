# Data structure

# list

# list1 = [11,12,13,14,15,16,17,18,19]
# print(type(list1))
# print(list1)

# Update list
# list1[1]=100

# 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
# 11, 12, 13, 14, 15, 16, 17, 18, 19
# -9, -8, -7, -6, -5, -4, -3, -2, -1


# print(list1)
# print(list1[1])
# print(list1[-4])

# list1 = [11,12,13,14,15,16,17,18,19]
# list1[2]='A'
# list1[4]='Apple'
# print(list1)
# print(type(list1))

# delete list index 
list1 = [11,12,13,14,15,16,17,18,19]

# print(list1)  #[11, 12, 13, 14, 15, 16, 17, 18, 19]
# del list1[0]
# print(list1)  #[12, 13, 14, 15, 16, 17, 18, 19]
# del list1[4]
# print(list1)  #[12, 13, 14, 15, 17, 18, 19]  
# del list1[5]
# print(list1)  #[12, 13, 14, 15, 17, 19]  


# list1=['math','physics','chemistry','english']
# list2=[1,2,3,4,5]
# list3=['a','b','c','d','e','f']
# list4=['ram','raj','shyam','kevin','sam','dia']
# list5 = [11,12,13,14,15,16,17,18,19]

# print(len(list1))
# print(len(list2))
# print(len(list3))
# print(len(list4))
# print(len(list5))
# del list4[5]
# print(len(list4))

# print(list1+list4)
# print(list1)
# print(list4)
# print(list2+list5)
# newlist = list1*5
# print(len(newlist))
# print(newlist)

# 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
# 11, 12, 13, 14, 15, 16, 17, 18, 19
# -9, -8, -7, -6, -5, -4, -3, -2, -1

# list5 = [11,12,13,14,15,16,17,18,19]

# print(list5[2::3])

# print(list5[:2])
# print(list5[::2])

# print(list5[3:])
# print(list5[:8])
# print(list5[:-8])

# print(list5[-1:-8])
# print(list5[-8:-1])

# print(list5[-7:-4])
# print(list5[4:-4])
# print(list5[2:-2])

# print(list5[-6:7])
# print(list5[-8:8])
# print(list5[8:])
# print(list5[2:8])
# print(list5[3:6])

#-----------------------------------------

# list1 = [11,12,13,14,15] 
# list2 = [15,16,17,18,19]

# print(list1*10)  
# #can't multiply sequence by non-int of type 'list'
# print(list1*'a') 
# #can't multiply sequence by non-int of type 'str'

# ------------- list Methods ----------------
list1 = [11,12,13,14,15] 

# append(): Adds an element to the end of the list.

# print(list1)
# list1.append(20)
# list1.append(21)
# print(list1)

# copy(): Returns a shallow   copy of the list.

# print(list1)
# # list2 = list1.copy() # shallow copy
# list2 = list1 # deep copy
# list1.append(10)
# list2.append(100)
# print(list1)
# print(list2)


# clear(): Removes all elements from the list.

# print(list1)
# list1.clear()
# print(list1)

# count(): Returns the number of times a specified element appears in the list.

# print(list1)
# list1.append(11)
# print(list1.count(11))
# print(list1)

# extend(): Adds elements from another list to the end of the current list.

# list1 = [11,12,13,14,15] 
# list2 = [15,16,17,18,19]

# print(list1.extend(list2))
# print(list1.extend([15,16,17,18,19]))
# print(list1)
# print(list2)


# index(): Returns the index of the first occurrence of a specified element.

# print(list1)
# print(list1.index(14))

# insert(): Inserts an element at a specified position.

# list1 = [11,12,13,14,15] 
# print(list1)
# list1.insert(1,10)
# list1.insert(0,10)
# print(list1)

# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).

# list1 = [11,12,13,14,15] 
# print(list1)
# print(list1.pop())
# print(list1)


# remove(): Removes the first occurrence of a specified element.

# list1 = [11,12,13,14,15,13] 
# print(list1)
# list1.remove(13)
# print(list1)

# reverse(): Reverses the order of the elements in the list.

# list1 = [11,12,13,14,15] 
# print(list1)
# list1.reverse()
# print(list1)


# sort(): Sorts the list in ascending order (by default).

# my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]
# # my_numbers.sort()
# my_numbers.sort(reverse=True)
# print(my_numbers)


# ------------- list Methods ----------------

 
# tuple

# tup1 = (1234,'eng','math','phy',10,23,43,54,65,'a','b') 
# list1 = [1234,'eng','math','phy',10,23,43,54,65,'a','b'] 
# tup2 = 1,2,3,4,5,6,7 
# print(type(tup1))
# print(tup1)

# print(tup1)
# print(tup1[5])
# print(list1[1][1])  

# print(tup1[3])  
# print(tup1[3])  
# print(type(tup1))  #<class 'tuple'>

# tup1 = (11,12,13,14,15,16,17,18,19)
# # -->
# print(tup1[-1])
# print(tup1[2:-2])

# tup1 = (11,12,13,14,15,16,17,18,19)
# tup1[0]=100
# print(tup1)  # 'tuple' object does not support item assignment

# tup1 = (11,12,13,14,15,16,17,18,19)

# print(tup1[::-2])
# print(tup1[1:5])
# tup2 = (100,200,300)
# print(tup1+tup2)
# print(tup1)
# print(tup1*tup2)

# key           value
# -------------------------------------------

# name          Paresh
# email         rajputpareshk@gmail.com
# city          surat
# a={
#     "name":"Paresh",
#     "city" : "surat",
#     "email":"rajputpareshk@gmail.com"
# }

# print(a[1])
# # print(type(a))
# a1 = {'name': 'Raghav', 'email': 'raghav@gmail.com', 'city': 'Hydrabad'}
# print(a1)
# a[1]=2000
# a['state']='Gujarat'
# a['country']='India'
# a['contact']=9586765994

# a['city']='Vapi'
# print(a)
# print(a[1])

# list1 = [1,2,3,4,5,6,7,8,9]

# print(len(list1))
# list1[100]=100
# list1[10]=100
# print(list1)
# print()

# a ={
#     "name":"Paresh",
#     "email":"rajputpareshk@gmail.com",
#     "city" : "surat",
#     "state":"gujarat",
#     "country":"india"
# }


# print(a) 
# print(a1)
# print(len(a)) 
# print(len(a1))
# print(a[0])    #KeyError: 0
# print(a['name'])  
# print(a['contact']) 

# pop popitem del

# print(a)
# print(a['name'])
# print(a.popitem()) #remove last pair
# a.popitem() #remove last pair
# a.pop("city") #remove inserted pair
# del a["email"]
# print(a)

# del a #delete dictionary completly
# print(len(a)) 
# print(a)

# contact ={
#     "name":"Paresh",
#     "email":"rajputpareshk@gmail.com",
#     "city" : "surat",
#     "state":"gujarat",
#     "country":"india"
# }
# print(contact)

# data = contact     #aliasing - deepcopy
# print(data)
# data['mob_no']=9586765994
# contact['bgroup']='O+'
# print(data)
# print(contact)

# data = contact.copy() # shallow copy
# data['mob_no']=9586765994
# contact['bgroup']='O+'
# print(data)
# print(contact)

# ---------------------------------------------------

# contact ={
#    "Person1": {
#     "name":"Paresh",
#     "email":"rajputpareshk@gmail.com",
#     "city" : "surat",
#     "state":"gujarat",
#     "country":"india"
# },
#    "Person2": {
#     "name":"Rajesh",
#     "email":"rajesh@gmail.com",
#     "city" : "Ahemdabad",
#     "state":"gujarat",
#     "country":"india"
# },
#    "Person3": {
#     "name":"Viral",
#     "email":"vira44@gmail.com",
#     "city" : "Baroda",
#     "state":"gujarat",
#     "country":"india"
# },
#    "Person4": {
#     "name":"Jignesh",
#     "email":"jignesh@gmail.com",
#     "city" : "Mumbai",
#     "state":"maharastra",
#     "country":"india"
# },
# }
# print(type(contact))
# print(contact)
# 

# print(contact["Person1"])

# print(contact["Person3"])
# Person5 ={
#     "name":"Altamas",
#     "email":"Altamas@gmail.com",
#     "city" : "Mumbai",
#     "state":"maharastra",
#     "country":"india"
# }
# contact["Person5"]=Person5
# print(contact["Person5"])

# print(contact)
# print(contact["Person5"]["name"])
# print(contact["Person5"][0]) #KeyError: 0

# contact["Person3"]["qualification"]="MCA"
# print(contact["Person3"])

# print(contact)
# contact.pop("Person2")
# print(contact)
# del contact["Person3"]
# print(contact)

# Set collection of unordered and unindexed

# set_A = {'apple','banana','cherry','orange','mango','grapes'}
# # print(type(set_A))
# print(set_A)

# print('banana' in  set_A)
# set_A.add('kiwi') 
# print(set_A)
# set_A.add('apple') 
# print(set_A)
# set_A.add('APPLE') 
# set_A.add('kiwi','avocado')  #ERROR : set.add() takes exactly one argument
# print(set_A) 

# print(len(set_A))
# set_A.update(['avocado','coconut','apple','jackfruit'])
# print(set_A)
# print(len(set_A))


# set_A = {'apple','banana','cherry','orange','mango','grapes'}
# set_A.remove('banmamaana')
# print(set_A)
# if item is does not exist, remove will raised an error.
# set_A.remove('kiwi')  # KeyError: 'kiwi'
# if item is does not exist, discard will not raised an error.
# set_A.discard('kiwi')  
# print(set_A)

# print(set_A)

# pop remove an item randomely
# poped1 = set_A.pop()
# print(poped1)
# poped1 = set_A.pop()
# print(poped1)
# poped1 = set_A.pop()
# print(poped1)
# poped1 = set_A.pop()
# print(poped1)
# poped1 = set_A.pop()
# print(poped1)
# print(set_A)
# poped2 = set_A.pop()
# print(poped2)

# print(set_A)

#del will delete set completely
# del set_A
# print(set_A)