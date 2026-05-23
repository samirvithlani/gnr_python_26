def test():
    print("Test called..")

test()   

def add(a,b):
    return a + b 

#add() --.error
x = add(10,20)
print("ans = ",x)
print("ans1 ===",add(100,20))

#cf which will take 2 args as string if not string then return msg arg must be stirng
#if string then return full name

def getFullName(fname,lname):
    if type(fname)!=str or type(lname)!=str:
        return  "invalid type"
    return fname+" "+lname

print(getFullName("amit",12))

#cf take 1 param as list and retuen all param in upper case bonus:use compr.... only

def upperconv(data):
    return [i.upper() for i in data]

print(upperconv(["ram","shyam"]))
        