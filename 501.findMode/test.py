dic = {'user1':'01', 'user2':'02'} 
a = list(dic.keys())[list(dic.values()).index('01')]
print(a)