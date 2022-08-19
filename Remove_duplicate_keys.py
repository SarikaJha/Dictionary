#Write a program to remove duplicate keys.
dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
}
my_dict={}
for i in dic:
    if i not in my_dict:
        my_dict[i]=dic[i]
print(my_dict)

