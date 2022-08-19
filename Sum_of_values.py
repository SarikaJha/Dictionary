#Write a program to print the sum of values.
my_dict = {
    'data1':100,
    'data2': -54,
    'data3': 247
}
val=my_dict.values()
sum=0
for i in val:
    sum=sum+i
print(sum)