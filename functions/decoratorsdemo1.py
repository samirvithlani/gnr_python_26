

def check_persons(func): #3 #func == throwParty()
    
    def inner(): #6
        pers = 10
        print("inner called..") #7
        #func() #8
        if pers>50:
            func()
        else:
            print("no party !")    
    
    return inner    #4


@check_persons #2 #5
def throwParty(): #9
    print("throwing party...") #10


throwParty() #1