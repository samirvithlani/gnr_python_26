def outer(o1,o2):
    x =100
    print("outer function called..")
    print("o1 = ",o1)
    print("o2 = ",o2)
    
    #print("y = ",y)
    def inner(no):
        print("inner function ")
        print("o1 inner = ",o1)
        print("o2 inner = ",o2)
        y =200
        return no **2

    #print("y = ",y)
    sqr = inner(9)
    print(sqr)
    #print("y = ",y)

outer(100,200)
        