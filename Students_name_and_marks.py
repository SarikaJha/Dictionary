#Take input of name and marks of 10 students and store to a dictionary.
# my_dict={
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# }
i=0
a=[]
b=[]
while i<10:
    name=input("enter the name:")
    marks=int(input("enter marks:"))
    a.append(name)
    b.append(marks)
    dict={}
    for j in range(len(a)):
        dict[a[j]]=b[j]
    i+=1
print(dict)
# print(my_dict)