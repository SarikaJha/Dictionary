#Write a program to sort a dictionary in ascending or descending according to its values .
name={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=sorted(name.values())
dict={}
dic={}
for i in a:
    for j in name.keys():
        if name[j]==i:
            dict[j]=name[j]
# for i in reversed(a):
#     for j in reversed(name.keys()):
#         if name[j]==i:
#             dic[j]=name[j]
print(dict)
# print(dic)

# name={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in name:
#     for k in name:
#         if name[k]>name[i]:
#             name[k],name[i]=name[i],name[k]
#         elif name[i]>name[k]:
#             name[k],name[i]=name[i],name[k]
# print(name)
