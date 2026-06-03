def calling():
    print("calling !!!")

def test(a):
    print(a)
    a() #calling

# test(10)    
# test("a")
# test([])
test(calling)