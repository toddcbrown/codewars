######## MY Function ####### GOT IT FIRST TRY!!!!!!!!!!!
def filter_list(l):
    new_lst = list()
    for item in l:
        if not type(item) is str:
            new_lst.append(item)
    return new_lst
    
    
############ BEST PRACTICES #######################
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
  
  
 # isistance()
