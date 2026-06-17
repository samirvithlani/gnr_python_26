#open
#("uri",mode)
#r,w,a,r+,w+
# w mode -> file if it exist it will replace all data and write it
# w mode -> file if it is not exist it will create file at location and write it
#file -->it is not keyword , variable only

# file = open("./demo1.txt","a")
# file.write("Hello this is first line from python !!!\n")
# file.close()

# file = open("student.txt","a")
# file.writelines(["amit\n","sumit\n","jay\n","raj\n"])
# file.close()


# print("Hello")
# stufile = open("student1.txt","a")
# print("Hi i am student file",file=stufile)
# stufile.close()


#vairblae fmd data write..
empid =101
empname = "amit"
file = open("../employee.txt","a")
file.write(f"id = {empid} - name = {empname}")
file.close()


