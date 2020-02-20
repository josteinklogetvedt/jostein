import numpy as np
import matplotlib.pyplot as plt


T = [222.4, 262.4, 283.7, 306.4, 331.3, 358.5, 413.0, 479.2, 520.0, 879.7, 1079.7, 1258.0]
c = [0.762, 1.146, 1.354, 1.582, 1.838, 2.118, 2.661, 3.28, 3.631, 5.29, 5.387, 5.507]

plt.figure()
plt.xlabel("T/(K)")
#plt.ylabel("c/(cal/mol K)")
#plt.plot(T,c, Marker="o", Color="black", Label = "Eksperiment", Linestyle="")

#R = 1.987
theta = 1324    #tipper Einsteinstemperaturen til diamant

T_new = np.arange(222.4,1258,1)
#c_t = np.array((3*R*(theta/T_new)**2)*((np.e**(theta/T_new))/(np.e**(theta/T_new)-1)**2))
#plt.plot(T_new,c_t, Color="red", Label = "Teori")



#TIL SI-ENHETER:
c_SI = []
for i in range(len(c)):
    c_SI.append(c[i]*4.184)  #Til SI-enheter

R = 8.314

plt.ylabel("c/(J/mol K)")
plt.plot(T,c_SI, Marker="o", Color="black", Label = "Eksp. (SI)", Linestyle="")

c_t = np.array((3*R*(theta/T_new)**2)*((np.e**(theta/T_new))/(np.e**(theta/T_new)-1)**2))
plt.plot(T_new,c_t, Color="red", Label = "Teori (SI)")

plt.legend()
plt.show()