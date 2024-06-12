def take_while(xs, condition):
    for i in range(len(xs)):
        if not condition(xs[i]):
            return(xs[:i], xs[i:])
        
    return(xs, [])
    
