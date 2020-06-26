#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. function that returns first and last digit of a number
def firstDigit(n):
    while n>=10:
        n=n/10;
    return int(n)
def lastDigit(n):
    return(n%10)
n=98562;
print(firstDigit(n),end=" ")
print(lastDigit (n))


# In[2]:


# 2.generating first n number of fibonacci numbers , n value from user
def printFibonacciNumbers(n):
    f1=0
    f2=1
    if(n<1):
        return
    for x in range(0,n):
        print(f2,end=" ")
        next=f1+f2
        f1=f2
        f2=next
printFibonacciNumbers(7)


# In[ ]:


# 4. Display multiplication table of k,k value from user
num=7
for i in range(1,11):
    print(num,'x',i,'=',num*i)


# In[3]:


# 3. Marks of students
n= int(input("Enter number ofstudents"))
if(n>=0):
    student=["member"]
    for i in range(0,n):
        name=input("Enter the name of student")
        print(name)
        mark=int(input('enter the marks out of 100'))
        print(mark)
        if(mark<40):
            student.append(name)
            print("this student has failed")
        else:
            print("you have passed")
    for i in range(1,len(student)):
        print(student[i])
else:
    print("invalid input")


# In[4]:


# 5. Taking number
sum=0
c=0
num=int(input("Enter the number"))
while num!=-1:
    c+=1
    sum+=num
    num=int(input())
print(sum/c)


# In[ ]:




