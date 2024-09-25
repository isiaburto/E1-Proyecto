import sympy as sp
import numpy as np

sp.init_printing(use_unicode=True)

def EnsamblarBf(XYZ, IEN):
    N = XYZ.rows
    M = IEN.rows
    Bf = sp.zeros(2*N, M)
    
    '''for i in range (Bf.rows):
        nodo = i + 1
        for j in range (IEN.rows):
            if IEN[j,0]==nodo:
                Coord_x = XYZ[IEN[j,1]-1,0] - XYZ[IEN[]]'''
                    
            
    
    return Bf

def EnsamblarLr(XYZ, Ap):
    return

def EnsamblarF(XYZ, Fext):
    return

def Solver(XYZ, IEN, Ap, Fext):
    return



XYZ = sp.Matrix([[-3,0],[0,4],[3,4],[3,0]])
IEN = sp.Matrix([[1,2],[2,3],[3,4],[4,1],[4,2]])
Fext = sp.Matrix([[2,0,-400],[4,600,0]])
Ap = sp.Matrix([[1,0,1,0],[3,90,1,1]])
sp.pprint(XYZ)
sp.pprint(IEN)
sp.pprint(Fext)
sp.pprint(Ap)

res = EnsamblarBf(XYZ,IEN)
print(sp.pprint(res))