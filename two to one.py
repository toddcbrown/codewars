######## My solution

def longest(s1, s2):
    s4 = []
    s3 = s1 + s2
    s3 = list(s3)
    for i in s3:
        if i not in s4:
            s4.append(i)
        else: continue
    return(''.join(sorted(s4)))
    
best practice
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
