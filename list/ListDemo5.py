data =["amit","sumit","amit","raj","raj","neha","ajay","parth"]
##unique element list

uniqueList = [] #
for i in data:
    #i = amit,sumit,amit
    if i not in uniqueList:
        uniqueList.append(i) #amit

print(uniqueList)        