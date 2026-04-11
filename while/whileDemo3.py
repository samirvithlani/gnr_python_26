'''

10 ,15 ->30
1 % 10 ==0 and 1 % 15 ==0
2   2
3
4
5
6
7
8
9
10
11,12,13,14,15,
16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
30 % 10 ==0 and 30 % 15  == 30

'''
no1 = 10
no2 = 15
#i=i
if (no1>no2):
    i = no1
else:
    i = no2
        
lcm =0
while True:
    
    if i % no1 ==0 and i % no2 ==0:
        lcm = i
        break
    i+=1

print("lcm = ",lcm)    