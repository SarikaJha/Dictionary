#Write a program to print the top 3 highest values of a given dictionary.
my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
a=[]
for i in my_dict:
  a.append(my_dict[i])
print(a)
f_max=0
s_max=0
t_max=0
i=0
b=[]
while i<len(a):
  if a[i]>f_max:
    t_max=s_max
    s_max=f_max
    f_max=a[i]
  elif a[i]>s_max:
    t_max=s_max
    s_max=f_max
    s_max=a[i]
  elif a[i]>t_max:
    t_max=a[i]
  i=i+1
print([f_max,s_max,t_max])


# dict={"name":"Priya","city":"New York","country":"USA"}
# print(dict.items())

