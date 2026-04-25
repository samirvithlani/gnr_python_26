#empty list

data = []
print(data)
print(type(data))

data = ["ram","shyam","amit","krishna","arjun"]
print(data)

#single elm
print(data[0])

#len
print(len(data))

#mutable:
data[1]="lakshman"
print(data)

#list iterable:

# for i in range(0,len(data)):
#     print(data[i])

for i in data:
    print(i)