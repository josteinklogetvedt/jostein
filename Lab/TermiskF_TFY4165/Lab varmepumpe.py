import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit


#Data målt fra laben. Måler temperaturen på det varmeste og kaldeste stedet på en varmepumpe
T_c = [14.3,14.2,12.4,10.6,8.8,7.5,6.2,5.0,3.9,2.8,2.1,1.2]
x = np.arange(0,23,2)
T_h = [14.5,16.5,18.9,21.1,23.2,25.2,27.1,28.7,30.0,31.6,32.9,34.4]

plt.figure()
plt.plot(x,T_c, Marker="x", Color="blue",Label="Cold Temperature",Linestyle="")
plt.plot(x,T_h, Marker="+",Color="red",Label="Hot Temperature",Linestyle="")
plt.legend()
plt.xlabel("t/min")
plt.ylabel("T/Celsius")


delta_T = []
for i in range(1,len(T_h)):
    delta_T.append((T_h[i]-T_h[i-1])*1.6518)
y = x[:-1]
plt.plot(y,delta_T, Marker="x", Color="blue", Label = "n", Linestyle="")

delta_T_2 = []
for i in range(len(T_h)):
    delta_T_2.append((T_h[i]+273)/(T_h[i]-T_c[i]))
plt.plot(x[1:-1],delta_T_2[1:-1],Marker="+", Color="red", Label="n_e", Linestyle="")
plt.show()
