###### My function
def find_short(s):
    s = s.split()
    length = None
    for word in s:
        if length is None or len(word) < length: 
            length = len(word)
        else: continue
    return(length)
    
##### Best practice
def find_short(s):
    return min(len(x) for x in s.split())    ###Min function
