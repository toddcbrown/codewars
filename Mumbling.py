######### My function ##########
def accum(s):
    count = 0
    lst = list()
    for let in s:
        count = count + 1
        let = let * (count)
        let = let.capitalize() ##########This got me...I forgot to make this an equal to variable. 
        lst.append(let)
    return('-'.join(lst))
    
####### Best practice ######## (I am getting sick of these one liners)
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
    
#################
#    Learn      #
#################

