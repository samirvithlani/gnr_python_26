
def zara(name):
    print(f"shopping from zara {name}")
    return name.upper()

def Lv(name):
    print(f"shopping from Lv {name}")    
    return name.upper()

def Gucci(name):
    print(f"shopping from Gucci {name}")    
    return name.upper()
    

def shopping(func):
    print("shopping called...")
    item  =func("purse")
    #print("item = ",item)
    return item

item =None

budget = 400000
if budget>500000:
    item =shopping(Lv)    
elif budget>300000:
    item = shopping(Gucci)    
elif budget>200000:
    item =shopping(zara)    
else:
    print("tat....a...")    


print("item = ",item)    
    