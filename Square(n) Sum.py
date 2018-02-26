####### MY FUNCTION
def square_sum(numbers):
    new_list = list()    ########## Do I need a new list or can I change the value in the old list?
    for num in numbers:
        one = num ** 2
        new_list.append(one)
    return sum(new_list)
    
########### Best practice ############
    
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)   ##Mapping, right? I need to learn this ##UPDATE: I don't think this is mapping
    
    ####################################################
    #                 QUESTIONS                        #
    ####################################################
    #
    #  HOW TO MAP:   map(function_to_apply, list_of_inputs)
    # ---------------
    # https://stackoverflow.com/questions/1540049/replace-values-in-list-using-python
    # According to this ↑ ... It doesn't appear to be any faster to modify old list, they recommend making a new list. 
    #
