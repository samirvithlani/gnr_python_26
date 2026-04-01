ticket = False
corner_seat = True
price = 50
floor =  True

if ticket:
    print("ticket is avaialble..")
    if corner_seat:
        print("corner seat is available..")
        if price<500:
            print("give ticket..")
        else:
            print("will come in morning show..")    
    else:
        print("corner seart is not avaialbel..")    
else:
    print("ticket is not avaialble..")        
    if floor:
        print("yes you are welcome..")
    else:
        print("thanks come again !!")    