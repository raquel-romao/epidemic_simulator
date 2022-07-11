def ind(n,e): 
    return [n,e]

def num(i):
    return i[0]

def est(i):
    return i[1]

def alt_est(i,e): 
    i[1]=e
    return i

def mostra_ind(i):
    print("número=",i[0], "estado=",i[1])