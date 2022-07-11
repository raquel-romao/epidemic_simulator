from evento import *

def novaA():  
    return []

def adcE(a,e): 
    antes=[ev for ev in a if tempo(ev)<tempo(e)]
    depois=[ev for ev in a if tempo(ev)>tempo(e)]
    return antes+[e]+depois

def retE(a): 
    if len(a)>0:
        return a[1:]
    else:
        print("Erro de retE! A CAP está vazia.")
               
def proxE(a):
    if len(a)>0:
        return a[0]
    else:
        print("Erro de proxE! A CAP está vazia.")

def mostraE(a):
    for e in a:
        print(ind(e),tipo(e),tempo(e))