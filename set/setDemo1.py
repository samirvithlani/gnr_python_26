#empty
# data = set()
# print(data)
# print(type(data))


data = {"ram","krishna","arjun","bhim"}
print(data)

# for i in data:
#     print(i)

data.add("draupadi")    
print(data)

#data.update({"lakshman","balram"})
data.update(["lakshman","balram"])
print(data)

removedELm = data.pop()
print("removing..",removedELm)
print(data)

#data.remove("krishna")
#data.discard("krishnaaa")
print(data)