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

users = ["amit","sumit","raj","parth","jay"]

#{"amit":"tima"}
numbers = [100,20,34,55,21,33,0,78,90,98,97,121,23]

numberwithl = {i:"even" if i % 2==0 else "odd" for i in numbers}
print(numberwithl)


users = ["amit","madam","sumit","bob","raj","parth","jay"]

#{"amit":" not paindrom...",mada,....}


numbers = [100,20,34,55,21,33,0,78,90,98,97,121,23]

#{100:100}
evennos = {i:i for i in numbers if i %2==0}
print(evennos)


students = {101:"ram",102:"shyam",103:"amit",104:"sumit",105:"raj"}
#op: {1001:"RAM",.....}
#students = {"ram":23,"shyam":24,"amit":18,"sumit":16,"snajay":20}
#{"ram":23,"shyam":24}


students1 = {k+1000: v.upper() for k,v in students.items()}
print(students1)
students = {"ram":23,"shyam":24,"amit":18,"sumit":16,"snajay":20}
qulifieds = {k:v for k,v in students.items() if v>20}
print(qulifieds)

sales = {"Mon":[10,20,30],"Tue":[10,30,50]}

salessum = {k:sum(v) for k,v in sales.items()}
print(salessum)