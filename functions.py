def mean(this_list):
    '''
    Takes a list of numbers and returns the mean
    '''
    
    if len(this_list) <= 0:
        return "You passed an empty list"
        
        
        
    total=0
    for item in this_list:
        total += item
    return total/len(this_list)