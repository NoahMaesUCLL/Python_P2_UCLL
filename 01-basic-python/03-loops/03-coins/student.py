# Write your code here
def coins(one, two, five, goal): # Slow Solution
    for i in range(0, one + 1):
        if (i * 1 + 0 * 2 + 0 * 5) == goal:
            return True
        for k in range(0, two + 1):
            if(i * 1 + k * 2 + 0 * 5) == goal:
                return True
            for j in range(0, five + 1):
                if(i * 1 + k * 2 + j * 5) == goal:
                    return True
                
    return False 

def coins(one, two, five, goal): # Fast Solution
    for x in range(0, one+1):
        for y in range(0, two+1):
            for z in range(0, five+1):
                if x + 2 * y + 5 * z == goal:
                    return True

    return False