from solvingLaplace import *

V_0_sine = lambda x : np.sin(4*np.pi*x)


M = 200 
x = np.linspace(0,1,M+1)
y = np.linspace(0,1,M+1)
x_1, y_1 = np.meshgrid(x,y)

V = Fourier_expansion(x_1,y_1,V_0_sine,4)  #order = 4 


# -- Plot E-field ---
skip = 8
Ex, Ey = calc_field(x,y,V)

M = np.hypot(Ex,Ey)
fig, ax = plt.subplots()
q = ax.quiver(x_1[::skip],y_1[::skip],Ex[::skip],Ey[::skip],M[::skip],scale=150,width=0.0015)
ax.set_xlim(-0.05,1.05)
ax.set_ylim(0.0,1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
#plt.savefig('Efield_sine.pdf')
plt.show()


# -- Plot potential ---
plt.contourf(x_1,y_1,V)
plt.colorbar()
plt.title('V(x,y)')
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('V_sinepot_contourf.pdf')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_1, y_1, V)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
#plt.savefig('V_sinepot3D.pdf')
plt.show()


# --- Plot potential at boundaries ---
plt.plot(x,V_0_sine(x), label='$V_0$',color='red',linestyle='dotted',linewidth=3)
plt.plot(x,V[-1,:], label='$V(x,1)$')
plt.xlabel('x')
plt.legend()
#plt.savefig('V(x,1)_sinepot.pdf')
plt.show()

plt.plot(x,V[0,:],label='V(x,0)',linestyle='dotted',linewidth=3)
plt.plot(x,V[:,0],label='V(0,y)')
plt.plot(x,V[:,-1],label='V(1,y)')
plt.legend()
#plt.savefig('boundaries_sinepot.pdf')
plt.show()
