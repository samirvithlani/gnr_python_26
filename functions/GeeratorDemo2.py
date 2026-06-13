def get_ticekts():
    ticket=1000
    while True:
        yield ticket
        ticket+=1


x = get_ticekts()
print(next(x))
print(next(x))
print(next(x))