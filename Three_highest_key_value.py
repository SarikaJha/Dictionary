#Write a program to print the top 3 highest values of a given dictionary.
my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100, 'f':20}
max=0
sec=0
third=0
a=[]
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]
            b=j
        if my_dict[j]>sec and my_dict[j]<max:
            sec=my_dict[j]
            c=j
        if my_dict[j]>third and my_dict[j]<sec:
            third=my_dict[j]
            d=j
a.append(b)
a.append(c)
a.append(d)
print(a)
