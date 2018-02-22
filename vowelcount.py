def getCount(inputStr):
    num_vowels = 0
    new_str = list(inputStr) #seperate string
    #print(new_str)
    for ch in new_str:
        if any (c in ch for c in ('a', 'e', 'i', 'o', 'u')): #I learned this instead of if ch is 'a' or 'e', etc... (this results in an error)
            num_vowels = num_vowels + 1
    
    
    return num_vowels
    
    #------Best practices---->
    
    def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
