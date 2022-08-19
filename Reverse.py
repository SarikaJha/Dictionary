dict={'a':[3,4,8],'b':[9,2,3]}
for i in dict:
    x=dict[i]
    j=-1
    b=[]
    while j>=-len(x):
        b.append(x[j])
        j-=1
    dict[i]=b
print(dict)
