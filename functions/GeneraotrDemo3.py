# def send_mail():
#     users =1000
#     for i in range(1,users,100):
#         yield f"mail send to users {i} to {i+99}"


def send_mail():
    start =1
    while start<=1000:
        yield range(start,start+100)
        start+=100        


for i in send_mail():
    print(i)

        