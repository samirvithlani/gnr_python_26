data =[100,"amit","jay",200,"sumit"]
print(data)

#data=[]
#remove..
removedElm = data.pop() #IndexError: pop from empty list
print(f"removing... {removedElm}")
print(data)


removedElm = data.pop(2)
print(f"removing... {removedElm}")
print(data)

data.remove("amit") #if 100 is presne tit will remove
                  #if not present ValueError: list.remove(x): x not in list
print(data)