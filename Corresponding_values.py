#Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements 
#of the 2nd list are the corresponding values.
list1=['one','two','three','four','five']
list2=['1','2','3','4','5']
l=len(list1)
new_list={}
for i in range(l):
    new_list[list1[i]]=list2[i]
print(new_list)
