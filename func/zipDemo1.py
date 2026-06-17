data1 = [10,20,30]
data2 = ["amit","sumit",'raj']


for i,j in zip(data1,data2):
    print(i,j)


x = {i:j for i,j in zip(data1,data2)}    
print(x)