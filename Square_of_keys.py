#Write a program to create a dictionary with all numbers from 1 to 15 as the keys and their squares 
#as the corresponding values.
i=1
a={}
for i in range(1,16):
    b=i*i
    a[i]=b
print(a)