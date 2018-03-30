def nb_year(p0, percent, aug, p):
    count = 0
    newpop = p0
    while True:
        if newpop < p:
            newpop = newpop + int((newpop * (percent/100)) + aug)
            count += 1
        else:
            return(count)
            
####Best Practice
def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year
