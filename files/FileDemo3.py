#import ...
import os
import shutil

#file exist..
print(os.path.exists("task.txt"))

#check it is file or folder
print(os.path.isfile("task.txt"))
print(os.path.isdir("func"))
#info..

print(os.path.getsize("task.txt"))
# print(os.path.getmtime("task.txt"))

#delete
#if exists..
#os.remove("aa.txt")

#file rename..
#os.rename("demo1.txt","demo11.txt")

#copy..
folderName ="files"
#shutil.copy("demo11.txt",f"./{folderName}/demo12.txt")
#shutil.copy2("demo11.txt",f"./{folderName}/demo12.txt") #meta data

#move
#shutil.move("demo11.txt","./files/demomove.txt")

#folder create
#os.mkdir("new_folder")
#os.mkdir("./files2/new_folder")
#os.makedirs("./file2/new_folder")

#os.rmdir("file2")
#shutil.rmtree("a")

#rename folder
#os.rename()

#copy full tree 

shutil.copytree("basics","../basics_copy")

