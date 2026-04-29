score = [["Vaibhav",400],["Abhisekh",360],["Virat",3000]]
print(score)

max = score[0][1]
name = score[0][0]
for i in range(0,len(score)):
    if score[i][1]>max:
        max = score[i][1]
        name = score[i][0]

print(max)        
print(name)