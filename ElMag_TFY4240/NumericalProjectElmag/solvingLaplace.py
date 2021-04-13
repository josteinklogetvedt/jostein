
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from mpl_toolkits.mplot3d import Axes3D
import numpy.linalg as la
 
def sinh(x):
    return (np.exp(x)-np.exp(-x))/2

def Fourier_expansion(x_1, y_1, V_0, order):
    '''
    x_1, y_1 : all x- and y-coordinates on the grid. The output of np.meshgrid(x,y).
    V_0 : Func to give boundary condition at V(x,1)=V_0(x), returns an array
    order : number of terms in the Fourier expansion
    '''
    V = x_1*0  #initialize V
    x = x_1[0,:]
    
    for n in range(1,order+1):
        integrand = V_0(x)*np.sin(n*np.pi*x)
        D_n = (2/sinh(n*np.pi))*integrate.simps(integrand,x)
        V += D_n*np.sin(n*np.pi*x_1)*sinh(n*np.pi*y_1)
        
    return V

def calc_field(x,y,V):
    Ex,Ey = np.gradient(V,x,y,edge_order=2)
    Ex = -Ex
    Ey = -Ey
    return Ex, Ey



