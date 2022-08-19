#Write a program to print 'exists' if entered key already exists in the dictionary and print 
#'not exists' if the entered key does not exist.
check_key=input("enter key:")
dict1={'name':'Raju','marks':56,'rank':'firstdiv'}
if check_key in dict1:
    print("exists")
else:
    print("not exixts")
