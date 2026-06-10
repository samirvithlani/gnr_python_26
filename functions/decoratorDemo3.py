
histroy=[] #50,80,95

def undoable(func):
    def inner(*args,**kwargs):
        result = func(*args,**kwargs)
        histroy.append(result)
        return result
    return inner
        
def undo():
    if len(histroy)>1:
        #histroy.pop() #remove current value.
        return histroy.pop()
    elif len(histroy)==1:
        return histroy[0]
    
    else:
        return "no history avaialble.."

@undoable
def update_score(score):
    return score

print(update_score(50))
print(update_score(80))
print(update_score(95))
print(update_score(195))
print(update_score(85))
print("undo",undo())
print("undo",undo())
print("undo",undo())
print("undo",undo())
print("undo",undo())
