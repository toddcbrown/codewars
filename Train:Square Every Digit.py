######## MY Code (12 lines)

def square_digits(num):
    new_num = list()
    num = str(num)
    num = list(num)
    for dig in num:
        dig = int(dig)
        dig = dig ** 2
        dig = str(dig)
        new_num.append(dig)
    new_num = ''.join(new_num)
    new_num = int(new_num)
    return(new_num)

### improve  (9 lines)

def square_digits(num):
    new_num = list()
    num = str(num)
    for dig in num:
        dig = int(dig)
        dig = str(dig ** 2)
        new_num.append(dig)
    new_num = ''.join(new_num)
    return int(new_num)
    
##### Best Practice (5 lines)

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)   #what does += mean?? add to variable?
    return int(ret)
