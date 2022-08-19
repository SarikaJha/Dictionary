# user=input("enter word:")
# a=[]
# a.append(user)
# for i in a:
#     print(i.capitalize())
# print()


# a=int(input("enter the number:"))
# i=0
# b=[]
# while i<a:
#     val=input("enter the string:")
#     b.append(val)
#     i=i+1
# print(b)
# for i in b:
#         print(i.capitalize(),end=" ")
# print()



a=int(input("enter the number:"))
i=0
s=""
l=[]
while i<a:
    val=input("enter the string:")
    l.append(val)
    i=i+1
i=0
while i<len(l):
    j=0
    while j<len(l[i]):
        if j==0:
            s+=l[i][0].upper()
        else:
            s+=l[i][j]
        j+=1
    i+=1
k=0
strng=""
while k<len(s):
    if s[k].isupper() and k!=0:
        strng+=" "+s[k]
    else:
        strng+=s[k]
    k+=1
print(strng)
