mode = input("please enter game mode :")

match mode:
    case "easy" | "EASY" | "e" | "E":
        print("you have selected easy mode ...")
    case "med":
        print("you have seleccted med mode ...")    
    case "hard":
        print("you have selected hard mode....")
    case _:
        print("invalid mode...")    

        
        
