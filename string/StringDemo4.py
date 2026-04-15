email = "   samir@gmail.com  " #15
print(email)
print(len(email))

#email = email.strip()
#email = email.lstrip()
#email = email.rstrip()
#print(email)
#print(len(email))

email = "   samir@ gmail .c om  " #15

email = email.strip()
email1 =""
for i in email:
    if " " not in i:
        email1 = email1+i

print("email...",email1)        
