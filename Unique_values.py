#Take a list having dictionary elements as shown below (Sample Data) and then store all 
#the unique values into a list and print.
num=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
j=0
a=[]
while i<len(num):
    for j in num[i]:
        if num[i][j] not in a:
            a.append(num[i][j])
        i=i+1
print(a)