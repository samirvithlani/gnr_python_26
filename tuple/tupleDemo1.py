data = ("ram","laxman","krishna","arjun")
print(data)
print(type(data))

#immutable
# data[0] = "RAM"
# print(data)

x =data.count("arjun")
print(x)

ind = data.index("krishna")
print(ind)

a = (1,2,3)
b = (4,5,6)

c = a + b
print(c)