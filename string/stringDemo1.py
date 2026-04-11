#'' ""  --> str

name = "royal technosoft"
print("name = ",name)
print(f"name = {name}")

print(name[0]) #supscri...

#len find

l = len(name)
print("length = ",l)

#range:
# for i in range(0,5):
#     print(name[i],end=" ")


# for i in range(0,l):
#     print(name[i],end=" ")

# for i in range(0,len(name)):
#     print(name[i],end=" ")

# for i in range(len(name)):
#     print(i,"-",name[i],end=" ")


#for each loop
for i in name:
    print(i,end=" ")
    
#immutable:no modification
#name[0] ="R"     #modification TypeError: 'str' object does not support item assignment