
def zara():
    print("shopping from zara")

def Lv():
    print("shopping from Lv")    

def Gucci():
    print("shopping from Gucci")    
    

def shopping(func):
    print("shopping called...")
    func()

budget = 1000000
if budget>500000:
    shopping(Lv)    
elif budget>300000:
    shopping(Gucci)    
elif budget>200000:
    shopping(zara)    
else:
    print("tat....a...")    
    