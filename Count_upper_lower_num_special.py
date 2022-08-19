dict="123@KiramN*"
upper=0
lower=0
num=0
ch=0
a=[]
for i in dict:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i in ("1","2","3","4","5","6","7","8","9","0"):
        num+=1
    else:
        ch+=1
a.append(upper)
a.append(lower)
a.append(num)
a.append(ch)
print(a)