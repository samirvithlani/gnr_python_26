tokens = iter([10,20,30,40,50])
#print(tokens)
print(next(tokens))
print(next(tokens))
print(next(tokens))
print(next(tokens))
print(next(tokens))


cuts = {101:"raj",102:"rajvi",103:"amit",104:"parth"}

q = iter(cuts.items())

while True:
    cust = next(q,None)
    if cust is None:
        print("no cust is ther")
        break
    print(cust)
    input("press enter for next cust:")
    print("next cust is",cust)