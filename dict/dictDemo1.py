data ={} #empty dict
print(data)

print(type(data))

data = {"Guj":"Gandhinagar","Mah":"Mumbai","Punjab":"Chadigadh","Goa":"Panji","Guj":"Ahm","hariyana":"Chadigadh"}
print(data)

#access data 
print(data["Guj"])#if key is not present throw exception
print(data.get("Punjabi")) #if key is not present return None

k = data.keys() #object([])
print(k)
v = data.values()
print(v)

kv = data.items() #[(),(),()]
print(kv)

for i,j in data.items():
    print(f"{i} - {j}")