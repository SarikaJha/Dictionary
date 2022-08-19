dict={"a":20,"b":42,"c":34}
val=dict.values()
l=list(val)
i=0
min=l[0]
while i <len(l):
    if l[i]<min:
        min=l[i]
    i+=1
print(min)