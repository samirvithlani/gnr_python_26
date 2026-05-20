sent = "hi i am from india india is my country"

x  = set(sent.split(" "))
print(x)

votes = ["A", "B", "A", "C", "B", "D"]
#unique cand 
#duplicate cand

unquie = set(votes)
dupli = len(votes) - len(unquie)


#a = "developer"
#b = "envelope"

#find unique login days

# logins = [
#     ("sam", "monday"),
#     ("sam", "monday"),
#     ("sam", "tuesday")
# ]

names = ["sam", "raj", "rohit", "sneha"]
#{"s","r"} --> comprehensoin

x = {i[0] for i in names}
print(x)

words = ["apple", "banana", "kiwi", "apple"]
x = {len(i) for i in words}
print(x)

nums =[1,2,3,4,5,6]
target =7
#(1,6)
#(2,5)
#(3,4)


checked = set()
# 1 #2 #3 4
for i in nums: 
    #
    diff = target-i
    
    if diff in checked:
        print((diff,i))
    
    checked.add(i) #1,2,3
        

