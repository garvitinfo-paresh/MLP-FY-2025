
# How to run Python Programm
# 1) Shortcut
# 3) Ext terminal
# 2) terminal_size
# 4) REPL
    #  Read Eval Print Loop

# print("Hello")

# Identifier
# variable

# a=10
# b=20
# print(" a : ",a)
# print(" b : ",b)
# print(" a+b : ",a+b)
# print(" a-b : ",a-b)
# print(" a*b : ",a*b)
# print(" a/b : ",a/b)

# c=6
# print(" a**c : ",a**c) #Power
# print(" a/c : ",a/c) # division
# print(" a//c : ",a//c) #floor division

# % - modulus

# print(45%4)
# print(45%3)
# print(78%7)
# print(79%8)

# print(90%9)
# print(92%9)
# print(95%9)
# print(98%9)
# print(98%9)
# print(99%9)
# print(103%9)

# x % 9 = max (8)
# x % 15 = max (14)
# x % n = max (n-1)

# print(10%3)

# 24%4 = 0
# 56%6 = 0
# 57%6 = 1
# 77%8 = 5

# 78%9 = 6
# 80%9 = 8
# 83%9 = 2

# a,b=10,20
# a,b=b,a
# print(" a : ",a)
# print(" b : ",b)

# BODMAS
# 10+20/5*4-1
# 9
# 25
# 22
# print(10+20/5*4-1)
# ---------------



# val1 = input("Enter something :  ")
# print(val1)
# # # print(10+ +val1)
# print(type(val1))

# a=10
# b='20'
# print(a+b)

# num1 = int(input(" Enter no1 : "))
# num2 = input(" Enter no2 : ")
# print("Total  = ",num1+num2)

# val1 = int(input("Enter your value1 ")) #Read a string from standard input. 
# val2 = int(input("Enter your value2 "))
# print(type(val1))
# print(val1+val2)

# print("0 Hello")
# print("2 Hello",end="\n")
# print("3 Hello","4 Hello",end="",sep="-")
# print("5 Hello")
# a=10
# b=20
# print("a : ",a,"b : ",b)
# ----------
# price=10
# qty= 5
# print("\nprice\tqty\t\trate\tamt ")
# print("\n",price,"\t",qty)

# 1) Arithmatic  +,-,*,/,%
# 2) Relational  >,<,<=,>=,==,!=
# 3) Logical    and, or, not
# 4) Bitwise    


# Relational operator

# >     greater than    a>b  a is greater than b
# <     less than       a<b  a is less than b
# >=    greater than or equal to    a>=b    a is greater than or equal to b     
# <=    less than or equal to    a<=b    a is less than or equal to b
# !=    not equal   a!=b    a is not equal to b 
# ==    equal to is equal   a==b    a is equal to is equal to b       


# print("Hello","5")
# print(5 + +"5")
# print("Hello"+"5")

# print("hello"*3)

# print(10+True)
# print(True+True)
# print(True+False)
# print(True*False)

# True = 1    False = 0

# print(10>20)
# print(10<20)
# print(100>=20)    
# print(10>=10)
# print(10>10) 

# print(100<=20)    
# print(10<=10)
# print(10<10) 

# print(10<20)
# print(10<20<30)

# print(10>20>30) #0
# print(30>20>10) #1
# print(10>20<30) #1  0
# print(30<20<10) #0  0

# print(1<2<3)    #1
# print(1>2>3)    #0
# print(3>2>1)    #1
# print(3<2<1)    #0

# print(12>15<5)

# print(int(3>=2>=1))
# print(4>=3>=2>=1)

# print(3>2)
# print(2>1)

# print(1>2>1)
# print(4>1)
# print(1<2<1)
# print(0>1)


# print(10!=10)
# print(10!=11)
# print(10==10)
# print(10==11)


# conditional statement
# if expression

# val = 1
# print("Before if")
# if val:
#     print("\tTrue part")
# print("After if")
    
# val = True
# print("Before if")
# if val:
#     print("\tTrue part")
# else:
#     print("\tFalse part")
# print("After if")

# print(" Greater ")
# a,b,c = 10,30,20
# if c<a>b:
#     print("a is greater ")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# if a>b:
#     if a>c: 
#         print("a is greater ")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")
# if a>b:
#     if a>c:
#         print(" a is greater ")
#     else:
#         print(" c is greater ")

# else:  
#     if b>c:
#         print(" b is greater ") 
#     else:
#         print(" c is greater ")



# if a>b and a>c:
#     print(a)
# elif b>c:
#     b
# else :
#     c 
# ---------------------------------------

# range(start,stop,step)

# start (1)
# stop (10) n i exclusive 

# n=10
# for i in range(1,n+1):
#     print(i,end=" ")

# for i in range(1,11,2):
#     print(i,end=" ")

# for i in range(10,0,-1):
#     print(i,end=" ")

# range()
# for i in range(1.5,10): not valid
#     print(i,end=" ")

# for i in range(65,90+1):
#     print(chr(i+32),end=" ")
# print()
# for i in range(1,26+1):
#     print(chr(i+64),end=" ")

# for i in range(1,5+1): # row    i = 5 
#     for j in range(1,i+1): # col    i
#         print("*",end=" ")
#     print()

# for i in range(1,3+1):
#     for j in range(1,5+1):
#         print("* ",end="")
#     print()

# i=1 * * * * *
# i=2 * * * * *
# i=3 * * * * * 


# i=1 j=1,2,3,4,5                  
# i=2 j=1,2,3,4,5                  
# i=2 j=1,2,3,4,5     
# 
# 
# for i in range(1,3+1):
    # for j in range(1,5+1):
    #     print("* ",end="")
    # print()

# i=1 * * * * *
# i=2 * * * * *
# i=3 * * * * * 



# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# i=1 * 
# i=2 * * 
# i=3 * * *  
# i=4 * * * *  
# i=5 * * * * * 


# i=1 j=1                
# i=2 j=1,2                  
# i=2 j=1,2,3                  
# i=2 j=1,2,3,4                  
# i=2 j=1,2,3,4,5            

# -------------------
# sp=10
# for i in range(1,5+1):
#     for k in range(1,sp):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# i=1      * 
# i=2      * * 
# i=3      * * *  
# i=4      * * * *  
# i=5      * * * * * 

# i=1 k=1..10 j=1                
# i=2 k=1..10 j=1,2                  
# i=2 k=1..10 j=1,2,3                  
# i=2 k=1..10 j=1,2,3,4                  
# i=2 k=1..10 j=1,2,3,4,5       

# sp=10
# for i in range(1,5+1):
#     for k in range(1,sp):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(" *",end="")
#     sp-=1
#     print()

#          -*   
#         -*-*
#        -*-*-*
#       -*-*-*-*
#      -*-*-*-*-*



# i=10
# while i>=1:
#     print(i,end=' ')
#     i-=1
# print(" i : ",i)

# i=1
# sp=10
# while i<=5:
#     k=1
#     while k<=sp:
#         print(" ",end="")
#         k+=1
#     j=1
#     while j<=i:
#         print(" *",end='')
#         j+=1
#     sp-=1 
#     print()
#     i+=1

# print(" i : ",i)
# sp=10
# for i in range(5,0,-1):
#     for k in range(1,sp):
#         print(end=" ")
#     for j in range(1,i+1): 
#         print(" *",end="")
#     sp+=1
#     print()


