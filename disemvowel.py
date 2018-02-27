#### My function ######
def disemvowel(string):
    new_lst = list()
    vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    for word in string:
        for letter in word:
            if letter in vowels: continue
            new_lst.append(letter)
    
    return ''.join(new_lst)
    
#### Best practice #### I Tried this code and got a Traceback?????
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
