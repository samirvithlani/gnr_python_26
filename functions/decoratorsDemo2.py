
def smartdiv(func): #func == div
    
    def inner(x,y):
        print("innner called..",x,y)
        if(y==0):
            print("can not divide by zero :")
        else:
            func(x,y)    
    
    return inner        
    

@smartdiv
def div(no1,no2):
    print("div called ",no1/no2)


div(10,20)    
    