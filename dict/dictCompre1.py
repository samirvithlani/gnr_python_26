#{1:1,2:2,3:3,4:4,5:5}

# data ={}
# for i in range(1,6):
#     data[i]=i
   
# print(data)    

data ={i:i for i in range(1,6)}
print(data)
data ={i:i**2 for i in range(1,6)}
print(data)

number = [1,2,3,4,5]
data = {i:i**3 for i in number}
print(data)

users = ["amit","sumit","raj","parth","jay"]
userswithinit  ={i[0]:i for i in users}
print(userswithinit)

userwithlen = {i:len(i) for i in users}
print(userwithlen)

