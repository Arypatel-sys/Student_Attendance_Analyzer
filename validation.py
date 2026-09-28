def valid_classes(totalclasses,attendedclasses):
    if totalclasses <=0:
        return False
    if attendedclasses<0:
        return False
    if attendedclasses>totalclasses:
       return False

    return True
    
