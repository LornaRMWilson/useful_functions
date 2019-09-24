def mean(list):
    '''
    Takes a list of numbers and returns the mean
    '''
    
        total=0
        for item in list:
                total += item
        return total/len(list)