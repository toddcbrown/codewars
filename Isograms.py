##### Mine
def is_isogram(string):
    string = string.lower()
    string = list(string)
    newstring =[]
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in string:
        if i not in alphabet:
            return(False)
        if i not in newstring:
            newstring.append(i)
            continue
        if i in newstring:
            return(False)
        else:
            return(True)
    return True
    
###### BEST
def is_isogram(string):
    return len(string) == len(set(string.lower()))
