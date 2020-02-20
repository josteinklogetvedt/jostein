import numpy as np
import matplotlib.pyplot as plt

###TABELL 2.2 m/SI-ENHETER
#Eksperimentelle verdier
T = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 298, 300]
c = [0.022, 0.054, 0.112, 0.203, 0.332, 0.5, 0.698, 0.912, 1.375, 1.846, 2.298, 2.714, 3.094, 3.422, 3.704, 3.943, 4.165, 4.361, 4.536, 4.69, 4.823, 4.938, 5.039, 5.122, 5.198, 5.268, 5.329, 5.383, 5.436, 5.483, 5.523, 5.562, 5.592, 5.599]

plt.figure()

theta = 285
R = 8.314

c_SI = []
for i in range(len(c)):
    c_SI.append(c[i]*4.184)  #Til SI-enheter

#plotter eksp.
plt.plot(T,c_SI, Marker="o", Color="black", Label = "Eksp. (SI)", Linestyle="")

#plotter teroretisk
T_new = np.arange(15,300,1)
c_t = np.array((3*R*(theta/T_new)**2)*((np.e**(theta/T_new))/(np.e**(theta/T_new)-1)**2))
plt.plot(T_new,c_t, Color="red", Label = "Teori (SI)")
plt.title("Tabell 2.2")

###TABELL 2.3 m/SI-ENHETER
#Ekspermienetelle verdier
T_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 273.15, 298.15, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
c_2 = [3.269*10**-4, 1.992*10**-3, 7.608*10**-3, 1.848*10**-2, 3.371*10**-2, 5.097*10**-2, 6.851*10**-2, 8.536*10**-2, 0.101, 0.1152, 0.1655, 0.1922, 0.207, 0.2116, 0.2156, 0.2159, 0.2222, 0.2273, 0.2321, 0.237, 0.2421, 0.2478, 0.2539, 0.2606, 0.2679, 0.2758, 0.2844, 0.2935]

#plt.figure()
plt.xlabel("T/(K)")
plt.ylabel("c/(J/mol K)")

#c_SI_2 = []
#for i in range(len(c_2)):
#    c_SI_2.append(c_2[i]*4.184*26.9815)

#plotter eksp.
#plt.plot(T_2,c_SI_2, Marker="o", Color="black", Label = "Eksp. (SI)", Linestyle="")

#theta_2 = 285
#plotter teoretiske
#T_new_2 = np.arange(10,900,5)
#c_t_2 = np.array((3*R*(theta_2/T_new_2)**2)*((np.e**(theta_2/T_new_2))/(np.e**(theta_2/T_new_2)-1)**2))
#plt.plot(T_new_2,c_t_2, Color="red", Label = "Teori (SI)")
#plt.title("Tabell 2.3")

plt.legend()
plt.show()
