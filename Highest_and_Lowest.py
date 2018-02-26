######### MY Function #############
def high_and_low(numbers):
    high = None
    low = None
    lst = list()
    numbers = numbers.split()
    for numb in numbers:
        numb = int(numb)
        if low is None or numb < low:   #### This was a b%$#, I forgot to put numb before low....dumb
            low = numb
        if high is None or numb > high:
            high = numb
    high = str(high)
    low = str(low)
    return(high + ' ' + low)
    
######### Best practice ###############
    
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
