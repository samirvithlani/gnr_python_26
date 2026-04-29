#list comprehension...

names= ["amit","sumit","raj"]
uppernames= []

for i in names:
    uppernames.append(i.upper())
print(uppernames)    

#comprehension
#[i[append] for i in names]
uppernames1 = [i.upper() for i in names]
print(uppernames1)

sales = [100,200,300,400,500] #10% profit
salesprof =[]

for i in sales:
    salesprof.append(i+ i*0.1)

print(salesprof)    

salesprof1 = [i*1.1 for i in sales]
print(salesprof1)

#list [100,200,300,400,500,600,700,800,900,1000]
numbers = []
for i in range(100,1100,100):
    numbers.append(i)
print(numbers)    

numbers1 = [i for i in range(100,1100,100)]
print(numbers1)


