a=input("enter string:")
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for j in range(len(a)):
    if dict[a[j]]==1:
        print(j)
        break