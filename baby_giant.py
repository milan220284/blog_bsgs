from math import sqrt

def babyGiant(g, y, p, option = False):
    '''
    Returns x s.t. y = g^x mod p for a prime p.
    optional argument option for printing intermediate steps
    '''
    # calculating ceiling
    k = round(sqrt(p - 1))

    X = [None] * k 

    # Baby steps
    for i in range(k):
        X[i] = pow(g, i, p)
    
    #Calculating inverse using Fermat's little theorem
    inv = pow(g, k * (p - 2), p)
    
    if option:
        print("X: ")
        for i in range(k): print(i, ':', X[i])
        Y = [None] * k 

    # Giant step, search for match in the list
    for j in range(k):
        tmp = (y * pow(inv, j, p)) % p
        if option: Y[j] = tmp

        if tmp in X:
            if option: print("Y: ", Y[:j+1])
            return j * k + X.index(tmp)
    # Solution not found
    return None

print(babyGiant(17, 438, 509, True))
