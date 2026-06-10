sales = [11,22,123,45,66,78,90,98,97,13]

print(list(filter(lambda x:x%2==0,sales)))


data = ("amit","sumit","raj","parth")
print(tuple(filter(lambda x:len(x)>4,data)))

#upper
print(list(map(lambda x:x.upper(),filter(lambda x:len(x)>4,data))))

