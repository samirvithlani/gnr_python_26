#file read...

# file = open("th.txt","r")
# #x =file.read()
# x =file.read(3)
# print(x)

# file = open("th.txt","r")
# x = file.readline()
# print(x)

# linecount =0
# file = open("th.txt","r")
# while True:
#     x = file.readline()
#     print(x,end="")
    
#     if not x:
#         break
#     linecount+=1

# file.close()    

# print("line count = ",linecount)



linecount =0
file = open("th.txt","r")

# x  = file.readlines() #list
# print(x)
for x in file.readlines():
    print(x,end="")
file.close()    

print("line count = ",linecount)