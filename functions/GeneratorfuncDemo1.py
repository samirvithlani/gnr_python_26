# def get_post():
#     yield "post 1"
#     yield "post 2"
#     yield "post 3"
#     yield "post 4"
#     yield "post 5"

# #x = get_post()    
# #print(x)
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))

# for p in get_post():
#     print(p)


def get_post():
    for i in range(1,10000):
        yield f"post {i}"

for i in get_post():
    print(i)        