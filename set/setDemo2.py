users1 = {"dasrath","vibhishan","hanuman","jamvan","kk","ram","krishna"}
users2 = {"shakuni","yudhisthir","draupadi","bhim","arjun","krishna","ram"}



#x = users1.union(users2)
#x = users1 | users2
#x = users1.intersection(users2)
#x = users1 & users2
#x = users1.difference(users2)
#x = users2 - users1
#x = users1.symmetric_difference(users2)
#print(x)

#users1.difference_update(users2)
#users1.intersection_update(users2)
#users1.symmetric_difference_update(users2)
#print(users1)

users1 = {"ram","krishna"}
users2 = {"shakuni","yudhisthir","draupadi","bhim","arjun","krishna","ram"}


#x= users1.issubset(users2)
x = users2.issuperset(users1)
print(x)