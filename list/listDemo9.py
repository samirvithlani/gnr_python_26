data = [10,20,23,34,56,78,90,27,34]

#odd no list
oddlist =[i for i in data if i % 2==1]

# for i in data:
#     if i %2==1:
#         oddlist.append(i)

print(oddlist)   


users =["amit","sumit","raj","parth","kunal","priya","supriya"]     
users4= [i for i in users if len(i)>4]
print(users4)

users =["amit","sumit","raj","parth","madam","kunal","bob","priya","supriya","naman"]   

palidromelist = [i for i in users if i == i[::-1]]
print(palidromelist)


data = [10,20,23,34,56,78,90,27,34]

datalabel = ["odd" if i %2==1 else "even" for i in data]
print(datalabel)

numbers = [100,-20,23,89,0,-90,-87,0,-66,50]

#numberlab = ["pos" if i>0 else "neg" for i in numbers]
numberlab = ["pos" if i>0 else("zero" if i==0 else "neg")  for i in numbers]
print(numberlab)

#palindrome



