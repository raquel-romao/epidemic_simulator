from individuo import *

def nova_grelha(N,obs): 
    d={}
    for p in obs:
        d[p]="O"
    return [N,d]

def mostra_grelha(g): 
    print(g)
    
def pos_livQ(g,x,y):
    assert abs(x)<=g[0] and abs(y)<=g[0]  
    d=g[1]
    if d.get((x,y),"v")=="v":
        return True
    else:
        return False
    
def posI(g,n):
    d=g[1]
    d=list(d.items())
    found=False
    for x in d:
        if num(x[1])==n:
            found=True
            return x[0]
    if not found:
        print("Erro de posI! O indivíduo não se encontra na grelha.")
        

def adcI(g,i,x,y):  
    assert abs(x)<=g[0] and abs(y)<=g[0]  
    d=g[1]
    if not pos_livQ(g,x,y):   
        print("Erro de adcI! Posição indisponível.")
    else:                                             
        d[(x,y)]=i
        return [g[0],d]

def remI(g,n):   
    g[1].pop(posI(g,n))
    return g   

def l_ind(g):
    d=g[1]
    i=[]
    for x in d.keys():
        if d.get(x)!="O":
            i=i+[d.get(x)]
    return i
           
def n_estado(g,e):    
    i=l_ind(g)
    x=0
    n=0
    while x<len(i):
        if i[x][1]==e:
            n=n+1
        x=x+1
    return n
    
def aux_viz1(tri):
    N=tri[0][0]
    a=tri[1]
    b=tri[2]
    l=[a,b]
    for i in range(len(l)):
        
        if l[i]==N+1:
            l[i]=-N
        elif l[i]==-N-1:
            l[i]=N
        
    return (l[0],l[1])

            
def viz_1(g,n):
    d=g[1]
    x="nd"
    y="nd"
    for p in d.keys():
        if posI(g,n)==p:
            x=posI(g,n)[0]
            y=posI(g,n)[1]  
                 
    return list(map(aux_viz1,[(g,x-1,y+1),(g,x-1,y),(g,x-1,y-1),(g,x,y+1),(g,x,y-1),(g,x+1,y+1),(g,x+1,y),(g,x+1,y-1)]))


def aux_viz2(tri):
    N=tri[0][0]
    a=tri[1]
    b=tri[2]
    l=[a,b]
    for i in range(len(l)):
        
        if l[i]==N+1:
            l[i]=-N
        elif l[i]==-N-1:
            l[i]=N
        elif l[i]==N+2:
            l[i]=-N+1
        elif l[i]==-N-2:
            l[i]=N-1
            
    return (l[0],l[1])

     
def viz_2(g,n): 
    d=g[1]
    x="nd"
    y="nd"
    for p in d.keys():
        if posI(g,n)==p:
            x=posI(g,n)[0]
            y=posI(g,n)[1]   
    
    return list(map(aux_viz2,[(g,x-2,y+2),(g,x-2,y+1),(g,x-2,y),(g,x-2,y-1),(g,x-2,y-2),(g,x-1,y+2),(g,x-1,y-2),(g,x,y+2),(g,x,y-2),(g,x+1,y+2),(g,x+1,y-2),(g,x+2,y+2),(g,x+2,y+1),(g,x+2,y),(g,x+2,y-1),(g,x+2,y-2)]))


def d_ind(g):
    d=g[1]
    I={}
    for a in d.keys():
        if d.get(a)!= "O" and d.get(a,"v")!="v":
            I[a]=d.get(a)
    return I


def l_coord(g,e):
    d=g[1]
    I=d_ind(g)
    l=[]
    for y in d.keys():
        for x in I.keys():
            if y==x and est(I.get(x))==e:
                l=l+[x]
    return l


def contactoQ(g,n1,n2):
    d=g[1]
    v11=viz_1(g,n1)
    v12=viz_1(g,n2)
    r=[]
    for a in v11:
        if a in v12:
            r=r+[a]
    z=[x for x in r if d.get((x[0],x[1]))!="O"] 
    return len(z)>0


def n1(g,n):
    d=g[1]
    v1=viz_1(g,n)
    
    a=[x for x in v1 if d.get(x)!="O" and d.get(x,"v")!="v" and est(d.get(x))=="I"]
    
    return len(a)


def n2(g,n):
    d=g[1]
    v2=viz_2(g,n)

    a=[x for x in v2 if d.get(x)!="O" and d.get(x,"v")!="v" and est(d.get(x))=="I" and contactoQ(g,n,num(d.get(x)))]
    
    return len(a)