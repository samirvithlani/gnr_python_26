#key word argument function
def getUserData(name,age,salary):
    print(f"Name = {name} Age = {age} salary = {salary}")

#getUserData("raj",23,34500)    
#getUserData(23,34500,"ram")    

#getUserData(age=23,name="ram",salary=34567)
#getUserData(age=23,name="ram",34000) #error
#getUserData("raj",age=23,name="ram") #error
getUserData("raj",age=23,salary=4500) #error