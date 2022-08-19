a=int(input("enter number:"))
x={}
for i in range(a):
    b=input("enter key:")
    x[b]={}
    c=input("enter name:")
    x[b]["name"]=c
    d=input("enter age:")
    x[b]["age"]=d
print(x)
