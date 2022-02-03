#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input())
num2 = int(input())

print("The LCM is", lcm(num1, num2))


# In[4]:


#2

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input())
num2 = int(input())

print("The HCF is", hcf(num1, num2))


# In[8]:


#3

decimal = int(input())

print("The decimal value of", decimal, "is:")
print(bin(decimal), "in binary")
print(oct(decimal), "in octal")
print(hex(decimal), "in hexadecimal")


# In[15]:


#4

c = str(input())
print("The ASCII value of '" + c + "' is", ord(c))

#for whole word

a=str(input())
[ord(i) for i in a]


# In[16]:


#5

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    
    else:
        print("Invalid Input")


# In[ ]:




