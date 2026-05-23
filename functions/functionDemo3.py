#args
# def getUsers(user):
#     print(user)



def getUsers(*args):
    print(args)

#getUsers("ram","raj")    
getUsers()    

#error
# def getStudents(*students,x):
#     print(students,x)

#soln (jugad)
# def getStudents(x,*students):
#     print(students,x)    

#soln 2
def getStudents(*students,x):
    print(students,x)    

getStudents("rudra","vedant",x="jaya")    


#cg which will a args as arg --> check all dta should be number time or else return false