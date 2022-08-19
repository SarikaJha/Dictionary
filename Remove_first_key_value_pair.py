#Write a program remove the first key value pair from a nested dictionary.
dict= {
    1: 'NAVGURUKUL',
    2: 'IN',  
    3:{
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
}
}
del dict[3]["A"]
print(dict)