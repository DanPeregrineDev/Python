def MoreOrLess(n1, n2, n3):
    #Negative
    if n1 > 0 and n2 > 0 and n3 > 0:
        if n1 < n2 and n1 < n3:
            return n1
        if n2 < n1 and n2 < n3:
            return n2
        if n3 < n1 and n3 < n2:
            return n3
    #Positive
    if n1 < 0 and n2 < 0 and n3 < 0:
        if n1 > n2 and n1 > n3:
            return n1
        if n2 > n1 and n2 > n3:
            return n2
        if n3 > n1 and n3 > n2:
            return n3
    else:
        return None