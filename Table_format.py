# dict ={}
# dict1 = {1: ["Samuel", 21, 'Data Structures'],
#      2: ["Richie", 20, 'Machine Learning'],
#      3: ["Lauren", 21, 'OOPS with java'],
#      }
 
# # Print the names of the columns.
# print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
# for key, value in dict1.items():
#     name, age, course = value
#     print ("{:<10} {:<10} {:<10}".format(name, age, course))


dict={'c1':[1,2,3],'c2':[5,6,7],'c3':[9,10,11]}
a,b,c=dict.keys()
print(a,b,c)
x,y,z=dict.values()
d=x,y,z
i=0
while i<len(d):
     print(x[i],y[i],x[i])
     i+=1