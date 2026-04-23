text = "HelloWorld"
#text[start:end]
x =text[0:5]
print(x)
print(text[5:10])
print(text[:5])
print(text[5:])
print(text[:])

#negative index..
#0  1  2  3
#J  A  V  A
#-4 -3 -2 -1
print(text[-1])

#helloworld
print(text[-5:])
print(text[:-5])

print("----------------------------")

#skip char
print(text[0:10:2])
print(text[::]) # 0 to end
print(text[::1])
print(text[::2])
print(text[1::])
print(text[1::2])
print(text[::-1])
print(text[8:2:-1]) #lrowl

