school = {"class11":["amit","sumit","raj"],"class12":["parth","rajvi","sumita"]}
print(school)

for i,j in school.items():
    print(i,end=" ") #j-->[]
    for stu in j:
        print(stu,end=" ")
    print()    


fruits = {"Names":["apple","banana","kiwi"],"price":[100,40,120]}    
#apple 100
fruits = {"Names":["apple","banana","kiwi"],"price":[100,40,120],"qty":[100,1000,300]} 
#op:apple = 100*100 = 10,000   