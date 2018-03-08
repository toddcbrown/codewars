##### My function
def xo(s):
    countx = 0
    counto = 0
    for dig in s:
        if dig is 'x' or dig is 'X':
            countx = countx + 1
        elif dig is 'o' or dig is 'O':
            counto = counto + 1
        else: continue
    if countx == counto:
        return True
    else:
        return False
        
#### Best practice
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')   #way easier
