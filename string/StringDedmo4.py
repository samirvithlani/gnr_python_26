data = "python is programming Language python is python"

#ind = data.index("on")
#ind = data.index("p",3)
#ind = data.index("p",3,6) 
#exception 
#print(f"index = {ind}")

#without using index funciton
# "L"


ind1 = data.index("p")
print(ind1)
ind2 = data.index("p",ind1+1)
print(ind2)

cnt = data.count("z")
print(cnt)