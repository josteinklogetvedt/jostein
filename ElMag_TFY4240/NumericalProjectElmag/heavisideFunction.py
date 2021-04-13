from solvingLaplace import *


def V_0_Heaviside(x):
    V_0 = np.copy(x)*0
    V_0[x[:]<3/4] = 1
    V_0[x[:]<1/2] = 0
    return V_0
 

M = 500  
x = np.linspace(0,1,M+1)
y = np.linspace(0,1,M+1)
x_1, y_1 = np.meshgrid(x,y)

V = Fourier_expansion(x_1,y_1,V_0_Heaviside, 100) #order = 100


# --- Plot E-field ---
skip = 15
Ex, Ey = calc_field(x,y,V)

M = np.hypot(Ex,Ey)
fig, ax = plt.subplots()
q = ax.quiver(x_1[::skip],y_1[::skip],Ex[::skip],Ey[::skip],M[::skip],scale=150,width=0.0015)
ax.set_xlim(-0.05,1.05)
ax.set_ylim(0.3,1.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
#plt.savefig("Efield_Heaviside.pdf")
plt.show()


# --- Plot potential ---
plt.contourf(x_1,y_1,V)
plt.colorbar()
plt.title('V(x,y)')
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('V_Heaviside_contourf.pdf')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_1, y_1, V)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
#plt.savefig('V_Heaviside3D.pdf')
plt.show()


# --- Plot V_0(x) and V(x,1) for different orders ---
orders = [10,30,50]
plt.plot(x,V_0_Heaviside(x), label='$V_0$',color='blue',linestyle='dotted',linewidth=3)
for i in range(len(orders)):
    V = Fourier_expansion(x_1,y_1,V_0_Heaviside,orders[i])
    plt.plot(x, V[-1,:], label='n='+str(orders[i]))
    plt.xlabel('x')
plt.legend()
#plt.savefig('V(x,1)_Heavisidepot.pdf')
plt.show()


# --- Convergence analysis ---
orders = [i**2 for i in range(1,20)]
error = np.zeros(len(orders))
analytic = V_0_Heaviside(x) 
for i in range(len(orders)):
    V = Fourier_expansion(x_1,y_1,V_0_Heaviside,orders[i])
    error[i] = la.norm(V[-1,:]-analytic)/la.norm(analytic)
    
plt.plot(orders, error, label='$e_r$', marker='o',linestyle='--',color='red',linewidth=1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('order')
plt.grid()
plt.legend()
#plt.savefig('error_Heavisidepot.pdf')
plt.show()


# --- Plot potential at boundaries ---
plt.plot(x,V[0,:],label='V(x,0)',linestyle='dotted',linewidth=3)
plt.plot(y,V[:,0],label='V(0,y)')
plt.plot(y,V[:,-1],label='V(1,y)')
plt.legend()
#plt.savefig('boundaries_Heaviside.pdf')
plt.show()
