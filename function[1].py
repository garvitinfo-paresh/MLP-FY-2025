# function

# 1. in built 
# len , max, min
# 2. UDF - User Defined Function

# def func_name(parameter):
#     ..
#     ...
#     ..
#     return val

# parameter/argument     return
#    w                      w 
#    w                      n  
#    n                      w
#    n                      n     

# NPNR
# def toPrint():  #Function Defination
#     # function body
#     print("Hello world")
# toPrint() #function calling 

# WPNR
# def toPrint(name):
#     print("Hello,",name)

# toPrint("Raj")
# toPrint("Rajesh")
# toPrint()

# NPNR
# def doSum():
#     n = int(input("Enter n : "))
#     m = int(input("Enter m : "))
#     print(n+m) 

# doSum()

# WPNR
# def doSum(a,b):
#     print(a+b) 

# n = int(input("Enter n : "))
# m = int(input("Enter m : "))
# doSum(n,m)


# NPWR
# def doSum():
#     n = int(input("Enter n : "))
#     m = int(input("Enter m : "))
#     # print(n+m)
#     return n+m

# print(doSum())
# sum = doSum()
# print(sum)

# WPWR
# def doSum(a,b):
#     return a+b 

# n = int(input("Enter n : "))
# m = int(input("Enter m : "))

# print(doSum(n,m))



# n=10
# def showNo():
#     a=n+1
#     print(a)
# showNo()

# def arith(a,b):
#     sum = a+b   
#     sub = a-b
#     return sum,sub
# sumRes,subRes = arith(30,20)
# print("sum :",sumRes)
# print("sub :",subRes)

# def arith(a,b):
#     sum = a+b   
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return sum,sub,mul,div

# arithRes = arith(30,20)    
# print(arithRes)
# print(type(arithRes))
# sumRes,subRes,mulRes,divRes = arith(30,20)
# print("sum :",sumRes)
# print("sub :",subRes)
# print("mul :",mulRes)
# print("div :",divRes)

# def func(a,b)
#     ...
#     ...
#     ..
#     return val

# func(10,20)

# a,b : formal argument
# 10,20 : actual argument

# 1. positional arguments

# 2. keyword arguments
# def myFucn(name,age):
#     print("Hello my name is ",name)
#     print("My age is ",age)
# myFucn(age = 32,name="Rajesh")

# 3. default arguments

# def toPrint(name = "guest",age ="NA" ):
#     print("Hello, i am  ", name)
#     print("my age is ", age )
# toPrint("raj")
# toPrint()
# toPrint("rajesh")

# 4. Variable length arguments

# def doSum(fname,lname,*arg):
#     print("fname : ",fname)
#     print("lname : ",lname)
#     print(arg)
#     print(type(arg))
    # sumOfInt = 0
    # for i in arg:
    #     print(i)
    #     # sumOfInt+=i
    # print(" Sum of Int :  ",sumOfInt)


# doSum(10)
# doSum(10,20)
# doSum(10,20,30,40,50,60)
# doSum("raj","ram",20)

# def toPrint(desig="new joinee",**kvagrs):
#     print(desig)
#     for k,v in kvagrs.items():
#         print(k," - ",v)
# toPrint(name="Raj",contact=43343434)
    
# Recursive Function 

# function exit, return , pc  
# def recur(n): 
#     print("Before ",n)
#     if(n>0): 
#         recur(n-1)
#     return n
#     # print("After ",n)

# recur(3)


# user
# recur(3) -> before 3      3>0         2
# recur(2) -> before 2      2>0         1
# recur(2) -> before 1      1>0         0
# recur(2) -> before 0      0>0   F     
# After 0  <- before 
# After 1  <- before 1
# After 2  <- before 2
# After 3  <- before 3 user

# def recur(n): 
#     print("before ",n)
#     if(n<3):  
#         recur(n+1)
#     return n
#     # print("after ",n)
# print(recur(1))

# factorial 
# 5 -> 5*4*3*2*1  -> 
# 5 -> 5*fact(n-1)
# 4 -> 4*fact(n-1)


# def fact(n):
#     if n == 1 :
#         return n
#     else:
#         return fact(n-1)*n
# print(fact(5))

#             n==1      else
# fact(5)     F         fact(4)*5
# fact(4)     F         fact(3)*4
# fact(3)     F         fact(2)*3
# fact(2)     F         fact(1)*2
# fact(1)     T         1
