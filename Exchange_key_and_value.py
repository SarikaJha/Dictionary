dict={1:10,2:60,3:30,5:50,4:60,5:3}
a={}
for key,value in dict.items():
    if value not in a:
        a[value]=[key]
    else:
        a[value].append(key)
print(a)


# dict2 = {}
# for i in dict:
#     dict2.setdefault(dict[i], []).append(i)
# print(dict2)