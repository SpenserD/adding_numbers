def add(x, y):
    if x == "" or  y == "":
        return "Invalid Operation" 
        
    result = int(x) + int(y)
    result = str(result)
    return result
