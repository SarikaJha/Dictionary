dict={'a':[3,4,8],'b':[9,2,3]}
for i in dict:
    x=dict[i]
    j=0
    b=[]
    while j<len(x):
        if x[j]%2==0:
            b.append(x[j])
        j+=1
    dict[i]=b
print(dict)     