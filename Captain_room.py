d=list(map(int,input().split()))
print(d)
a={}
for i in d:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
for j in a:
    if a[j]==1:
        print("captain room:",j)
        break
