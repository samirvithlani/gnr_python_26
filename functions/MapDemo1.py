marks =[10,20,30,40,50,60]
updatedmarks =[]

for i in marks:
    updatedmarks.append(i+10)

print(updatedmarks)    

#compr
updatedmarks2 = [i+1 for i in marks]    
print(updatedmarks2)

#map
updatedmarks3 = map(lambda x:x+10,marks)
print(list(updatedmarks3))

data = ("amit","sumit","raj","parth")
upperData = map(lambda x:x.upper(),data)
print(tuple(upperData))

upperData2 = map(lambda x:x.startswith("s"),data)
print(list(upperData2))



sales = [11,22,123,45,66,78,90,98,97,13]
salesLb = map(lambda x:"even" if x % 2==0 else "odd",sales)
print(list(salesLb))


data = ("amit","sumit","raj","parth")
datalen = list(map(lambda x:len(x),data))
print(datalen)

data = ("amit","sumit","naman","raj","bob","parth")
palindromenames = list(map(lambda x:"palindrome" if x == x[::-1] else "not",data))
print(palindromenames)

data = [121,23,33,678,99,100,111]

palindromenums = list(map(lambda x:"palindrome" if str(x) ==str(x)[::-1] else "not",data))
print(palindromenums)



prices = {'apple': 1.00, 'banana': 0.50, 'orange': 0.75}

#[(apple,1.00),(),()]
#x = (apple,1.00)
price1 = dict(map(lambda x:[x[0],x[1]*1.1],prices.items()))
print(price1)

prices = {'apple': 1.00, 'banana': 0.50, 'orange': 0.75}


