#Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary,
#were the letters are the keys and their frequencies are the values.
# word="MISSISSIPPI"
# count={"M":0,"I":0,"S":0,"P":0}
# for i in word:
#     if i=="M":
#         count["M"]+=1
#     elif i=="I":
#         count["I"]+=1
#     elif i=="S":
#         count["S"]+=1
#     elif i=="P":
#         count["P"]+=1
# print(count)

dict="MISSISSIPPI"
# dict="frequencies"
a={}
for i in dict:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
