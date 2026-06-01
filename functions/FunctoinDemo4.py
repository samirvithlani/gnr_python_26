def getStudents(**kwargs):
    print(kwargs)


getStudents(name="amit",age=23,status=True)    


def getData(*args,**kwargs):
    print(args)
    print(kwargs)

getData(1,2,2,3,4,55,a=10,b=20,c=90)    

#create f --> which will accept kwrgs and returen all key as list and print it
def shoppingcart(**kwargs):
    total =0
    for i,j in kwargs.items():
        if type(j)==int or type(j)==float:
            total  =total+j
    return total

print(shoppingcart(laptop=20000,phonoe=10000,mobile="realme"))  


#vlidateform
#param kwrgs --> name,age,email,password,contact
#required fileds -->name email,password

def validateForm(*args,**kwargs):
    #reequiredFileds =["name","email","password"]
    msg=""
    for rf in args:
        print(rf)
        if rf not in kwargs:
            msg= "form validation faild."
        else:
            msg= "reg successfull !!"
    return msg        

print(validateForm("name","email","password",name="amit",age=23,email="sam@gmail.com",password="sam"))        

#dynamic sql query
#select * from emaployee where"
#city = "ahmedbad",name="sumit"
        
def sqlq(**kwargs):
    query= "SELECT * from Employee where "
    cond =[]
    for i,j in kwargs.items():
        cond.append(f"{i}='{j}'")
    query = query+ " AND ".join(cond)    
    return query

print(sqlq(name="amit",age=23))
        
        
        