def outer():
    print("outer called..")
    def inner(x):
        print("inner called..",x)
    
    
    return inner

ans = outer() #ans == inner address
print(ans)
ans(10)

        