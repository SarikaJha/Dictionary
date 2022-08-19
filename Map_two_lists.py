# a=['mango','pear','apple','papaya']
# b=[90,80,70,60]
# x=dict(zip(a,b))
# print(x)


a=['mango','pear','apple','papaya']
b=[90,80,70,60]
l=len(b)
dict={}
for i in range(l):
    dict[a[i]]=b[i]
print(dict)