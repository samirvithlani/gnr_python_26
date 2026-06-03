#Lambda function

x = lambda:print("test function called")
x() #calling

add = lambda a,b: print(a+b)
add(10,20)


avg = lambda a,b,c:(a+b+c)/3
a = avg(10,20,30)
print(a)

#if else..
findMax = lambda a,b : a if a>b else b
print("max",findMax(10,100))

#lambda name true or false
isPalindrome = lambda name :True if name ==name[::-1] else False
print(isPalindrome("naman"))

#hw
checkData = lambda x : True if "aeiou" in x else False
print(checkData("Amit"))
    
checkno = lambda no : "Pos" if no>0 else("zero" if no==0 else "Neg")    
print(checkno(0))

lower = lambda name : True if name.islower() else False
print(lower("sam"))







