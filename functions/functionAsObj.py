def test():
    print("test called..")
    return 100

# x  = test()    
# print(x)

x = test
print(x)
x() #test()

def add(a,b):
    return a+b

x = add
ans = x(10,20)
print(ans)