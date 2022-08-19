dict={'a':[3,4,8],"b":[9,2,3]}
for i in dict:
    x=dict[i]
    j=0
    sum=0
    while j<len(x):
        sum+=x[j]
        j+=1
    dict[i]=sum
print(dict)
