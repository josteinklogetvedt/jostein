import numpy as np
import matplotlib.pyplot as plt

#data
vekt_1 = [83.8, 81.27, 78.76, 76.34, 73.93]
tid_1 = [0.3333333, 1.3333333, 2.3333333, 3.333333, 4.3333333]
vekt_2 = [66.469, 64.069, 62.149, 60.029, 57.909, 55.919, 53.879]
tid_2 = [5.58333333, 6.65, 7.58333333, 8.58333333, 9.58333333, 10.58333333, 11.58333333]

def linear_regresjon(x,y):
    N = len(x)
    S_x = np.sum(x)
    S_y = np.sum(y)
    S_xx = np.sum(x ** 2)
    S_xy = np.sum(x * y)
    Delta = N * S_xx - S_x ** 2
    a0 = (S_y * S_xx - S_x * S_xy) / Delta
    a1 = (N * S_xy - S_x * S_y) / Delta
    y_new = a0 + a1 * x

    Dy = y - y_new
    S = np.sum(Dy ** 2)
    Da0 = np.sqrt((S * S_xx) / ((N - 2) * Delta))
    Da1 = np.sqrt((N * S) / ((N - 2) * Delta))
    #print('Da0: ' + str(Da0) + ' Da1: ' + str(Da1))
    return a0,a1

#plotter serie 1
plt.figure()
plt.xlabel("t / min")
plt.ylabel("m / g")
b_1,a_1 = linear_regresjon(np.array(tid_1),np.array(vekt_1))
plt.plot(tid_1,vekt_1, label="Set 1",color="blue", marker="o", linestyle="")
x_1 = np.arange(0,12,0.1)
y_1 = b_1 + a_1*x_1
plt.plot(x_1,y_1, color="blue")
print(a_1)

#plotter serie 2
plt.plot(tid_2,vekt_2, label="Set 2", color="orange", marker="o", linestyle="")
b_2, a_2 = linear_regresjon(np.array(tid_2), np.array(vekt_2))
x_2 = np.arange(0,12,0.1)
y_2 = b_2 + a_2*x_2
plt.plot(x_2,y_2, color="orange")
print(a_2)

#finner Delta_m average
delta_m_1 = b_1 + a_1*tid_1[-1] - (b_2+a_2*tid_1[-1])
delta_m_2 = b_1 + a_1*tid_2[0] - (b_2+a_2*tid_2[0])
delta_m_ave = (delta_m_1+delta_m_2)/2
print(delta_m_ave, "delta m average")

#plotter delta_m1
y_a = np.arange(b_2+a_2*tid_1[-1],b_1+a_1*tid_1[-1], 0.1)
x_a = []
for i in range(len(y_a)):
    x_a.append(tid_1[-1])
plt.plot(np.array(x_a),y_a, label="$\Delta m_{1}$",color="red", linestyle="dotted")

#plotter delta_m2
y_b = np.arange(b_2+a_2*tid_2[0],b_1+a_1*tid_2[0], 0.1)
x_b = []
for i in range(len(y_b)):
    x_b.append(tid_2[0])
plt.plot(np.array(x_b),y_b, label="$\Delta m_{2}$", color="green", linestyle="dotted")

plt.xticks([1,3,round(tid_1[-1],1),round(tid_2[0],1),7,9,11],["1","3", "$t_{1}$","$t_{2}$","7","9","11"])

plt.legend(loc="upper right", prop={'size': 13})
plt.title("Data collections")
#plt.savefig("linear_regression_4.pdf")
plt.show()

from scipy.optimize import fsolve
#sensitivitetsanalyse
n = 0.2234
R = 8.314
L = 2*10**5
T_0 = 295.15
T_f = 77
def func(x, T=295.15, m=delta_m_ave):
    epsilon_1 = (x/T)/((np.e**(x/T))-1)
    epsilon_2 = (x/T_f)/((np.e**(x/T_f))-1)
    delta_Q = 3*n*R*((T*epsilon_1-T_f*epsilon_2))
    return delta_Q - L*m*10**(-3)
einsteintemp_orig = fsolve(func, 10)
print(einsteintemp_orig, "einsteintemp original")

d_T = 1
d_m = (delta_m_1-delta_m_2)/2
print(d_m, "d(delta_m)")
def func_1(x, T=296.15, m=delta_m_ave):
    epsilon_1 = (x/T)/((np.e**(x/T))-1)
    epsilon_2 = (x/T_f)/((np.e**(x/T_f))-1)
    delta_Q = 3*n*R*((T*epsilon_1-T_f*epsilon_2))
    return delta_Q - L*m*10**(-3)
einsteintemp_1 = fsolve(func_1, 10)
def func_2(x, T=294.15, m=delta_m_ave):
    epsilon_1 = (x/T)/((np.e**(x/T))-1)
    epsilon_2 = (x/T_f)/((np.e**(x/T_f))-1)
    delta_Q = 3*n*R*((T*epsilon_1-T_f*epsilon_2))
    return delta_Q - L*m*10**(-3)
einsteintemp_2 = fsolve(func_2, 10)
partiell_mhp_T = (einsteintemp_1-einsteintemp_2)/2*d_T
print(partiell_mhp_T, "partiell derivert mhp T")

def func_3(x, T=295.15, m=delta_m_ave+d_m):
    epsilon_1 = (x/T)/((np.e**(x/T))-1)
    epsilon_2 = (x/T_f)/((np.e**(x/T_f))-1)
    delta_Q = 3*n*R*((T*epsilon_1-T_f*epsilon_2))
    return delta_Q - L*m*10**(-3)
einsteintemp_3 = fsolve(func_3, 10)

def func_4(x, T=295.15, m=delta_m_ave-d_m):
    epsilon_1 = (x/T)/((np.e**(x/T))-1)
    epsilon_2 = (x/T_f)/((np.e**(x/T_f))-1)
    delta_Q = 3*n*R*((T*epsilon_1-T_f*epsilon_2))
    return delta_Q - L*m*10**(-3)
einsteintemp_4 = fsolve(func_4, 10)


partiell_mhp_dm = (einsteintemp_3-einsteintemp_4)/(2*d_m)
print(partiell_mhp_dm, "partiell derivert mhp delta_m")

#Usikkerhetsanalyse
usikkerhet_einsteintemp = np.sqrt((partiell_mhp_dm*d_m)**2+(partiell_mhp_T*d_T)**2)
print(usikkerhet_einsteintemp, "usikkerhet")

