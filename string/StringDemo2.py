#assic value A - >65 a ->97

x = "A" #-->as..
print("ord",ord(x))
print("chr",chr(97))


#amit --> AMIT name ="amit" upperName ="AMIT"

name  ="amIt"
upperName = ""

for i in range(0,len(name)):
    #a -->97
    if ord(name[i])>=97:
        #"" = "" + chr(ord(a)-32) - chr(97-32) --chr(65) --A
        upperName = upperName+chr(ord(name[i])-32)
    else:
        upperName=upperName+name[i]    

print(upperName)        
        
