from solvingLaplace import *

V_0_quad = lambda x : 1-16*(x-(1/2))**4

M = 200
x = np.linspace(0,1,M+1)
y = np.linspace(0,1,M+1)
x_1, y_1 = np.meshgrid(x,y)

V = Fourier_expansion(x_1,y_1,V_0_quad,10) #order = 10


# --- Plot E-field --- 
skip = 6
Ex, Ey = calc_field(x,y,V)

E_abs = (Ex**2 + Ey**2)**(1/2)
plt.contourf(x_1,y_1,E_abs)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('Efield_contour_quad.pdf')
plt.show()

M = np.hypot(Ex,Ey)
fig, ax = plt.subplots()
q = ax.quiver(x_1[::skip],y_1[::skip],Ex[::skip],Ey[::skip],M[::skip],scale=50,width=0.0015)
ax.set_xlim(-0.05,1.05)
ax.set_ylim(0.2,1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
#plt.savefig('Efield_quadpot.pdf')
plt.show()


# --- Plot potential ---
plt.contourf(x_1,y_1,V)
plt.colorbar()
plt.title('V(x,y)')
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('V_quadpot_contourf.pdf')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_1, y_1, V)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
#plt.savefig('V_sinepot3D.pdf')
plt.show()


# --- Plot V_0(x) and V(x,1) for different orders ---
orders = [1,3,5,7]
plt.plot(x,V_0_quad(x), label='$V_0$',color='blue',linestyle='dotted',linewidth=3)
for i in range(len(orders)):
    V = Fourier_expansion(x_1,y_1,V_0_quad,orders[i])
    plt.plot(x, V[-1,:], label='n='+str(orders[i]))
    plt.xlabel('x')
plt.legend()
#plt.savefig('V(x,1)_quadpot.pdf')
plt.show()


# --- Convergence analysis ---
orders = [1+i for i in range(60)]
error = np.zeros(len(orders))
analytic = V_0_quad(x) 
for i in range(len(orders)):
    V = Fourier_expansion(x_1,y_1,V_0_quad,orders[i])
    error[i] = la.norm(V[-1,:]-analytic)/la.norm(analytic)
    
plt.plot(orders, error, label='$e_r$', marker='o',linestyle='--',color='red',linewidth=1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('order')
plt.grid()
plt.legend()
#plt.savefig('error_quadpot.pdf')
plt.show()


# --- Plot potential at boundaries ---
plt.plot(x,V[0,:],label='V(x,0)',linestyle='dotted',linewidth=3)
plt.plot(x,V[:,0],label='V(0,y)')
plt.plot(x,V[:,-1],label='V(1,y)')
plt.legend()
#plt.savefig('boundaries_quadpot.pdf')
plt.show()
