# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# a=10
# print(type(a))
# b = 10.3
# print(type(b))
# c = True
# print(type(c))
# d = 4j
# print(type(d))
# e=(1,2)
# f = [3,2]
# g = {5,6}
# i = {'a':'apple','p':"put"}
# j='word'
# print(type(e),type(f),type(g),type(i),type(j))
#-----------------------------------
# a = int(input("Enter the value of A:"))
# b = int(input("enter ht evalue of B:"))

# def add(a,b):
#     res1 = a+b
#     print(res1)
#     print("\n")

# print("\n choices are 1 addition only")
# while(1):
#     cho = int(input("enter your choice:"))
#     if cho == 1:   
#         add(a,b)
#     elif True: print("marja sahu")
#     else:
#         print("invalid choic\]\n")
#         break
#------------------------------------------------------
# s1 = input("enter a string:")
# s2 = input("enter a string:")

# con_str = s1+s2
# print("string is ",con_str)

# s3 = con_str[2:]
# s4 = con_str[3:6]
# s5 = con_str[::-1]#reverses a string
# s6 = con_str[1:6:2]#prints with stepcount of 2 inside a scope
# print("substring:")
# print(s3,s4,s5)
#-----------------------------------
# import numpy as np
# a = np.array([[1,2,3],[4,2,5]])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(type(a))

#-----------------------------------

# a= [1,2,3,4,5,"hello"]
# print(a)
# a.insert(3,20)
# print(a)
# a.remove(3)#number is removied not index
# print(a)
# a.append("hi")
# print(a)
# print(len(a))
# a.pop()
# print(a)
# a.pop(2)
# print(a)
# a.clear()
# print(a)


#---------------------------------------
# def checklist(list1,list2):
#     return list1==list2
    
# li = [12,34]
# lm = [12,34]
# lj = [32,54]

# print(checklist(li,lm))
# print(checklist(li,lj))


#---------------------------------------
# a=(10,20,30)
# print(a)
# b = a + (40,50,60)
# print(b)
# print("len si",len(a))
# n = int(input("enter element"))
# print(b.index(n))
# print("elemts from 2 to 5 are")
# print(b[2:5])
#--------------------------------------

# dict = {1:"python",2:"java",3:"C",4:"c++"}
# print(dict)
# print("accessing 1 ele:",dict[1])
# print("accessing 3 ele:",dict.get(1))
# dict[4] = "sql"
# print("after chaing val of 4ht ele:",dict)
# print(len(dict))
#-----------------------------------------
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("hello, my name is",self.name,"and i am",self.age,"yearsodl.")
# person1 = Person("Dj",69)
# person1.greet()

#-----------------------------------------

# stu = ['megha','ram','ravi','ruth']
# mar = []
# for i in stu:
#     print(i,"makr is:",end='')
#     marks = int(input())
#     if marks > 100:
#         raise Exception('marks shiould not be less than 100')
#     else:
#         mar.append(marks)


# try:
#     i = int(input("index:"))
#     print(mar[i])
#     avg = int(input("ente not of subjet to cal avg"))
#     print(mar[i]/avg)
# except IndexError as error:
#         print("you are asccesing anot asdfghal;sfh",error)
# except ZeroDivisionError as e:
#     print("no of subjects cannot be zero",e)



#dict - get,len
#tuple - index->element to pos,len