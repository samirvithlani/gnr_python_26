import datetime
import time

print("Hello")
time.sleep(1) #seconds
print("hi")

# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)



# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)


#print(time.time())
start = time.time()
for i in range(10000000):
    pass
end = time.time()
print(end-start)

    