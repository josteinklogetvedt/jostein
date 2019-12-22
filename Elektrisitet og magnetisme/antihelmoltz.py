import numpy as np
from matplotlib import pyplot as plt


N = 330
I0 = 1
mu_0 = 4*np.pi*10**(-7)
R = 0.07
a_liste = [2*R, R, R/2]

def B_felt_antihelmholtz(x,a):
    prefaktor = N*mu_0*I0/(2*R)
    return 10000*prefaktor*((1 +(x-a/2)**2/R**2)**(-1.5) - (1 +(x+a/2)**2/R**2)**(-1.5))

def brgn_avvik(B, B_brgn):
    return (B_brgn-B)

def unpacking_to_array(file):
    f = open(file, "r")
    B = []
    x = []
    for line in f:
        liste = line.split()
        B.append(liste[0])
        x.append(liste[1])
    f.close()
    del B[0]
    del x[0]
    x = np.asarray(x, dtype=np.float64)
    B = np.asarray(B, dtype=np.float64)
    return x,B

def lag_error_punkter(x,B):
    error_x_verdier = np.array([x[0]])
    error_B_verdier = np.array([B[0]])
    for i in range(len(x)):
        if x[i] - error_x_verdier[-1] >= 0.01:
            error_x_verdier = np.append(error_x_verdier,[x[i]])
            error_B_verdier = np.append(error_B_verdier,[B[i]])
        if x[i] - error_x_verdier[-1] <= -0.01:
            error_x_verdier = np.append(error_x_verdier,[x[i]])
            error_B_verdier = np.append(error_B_verdier,[B[i]])

    return error_x_verdier, error_B_verdier

def brgn_og_maalte_graf(maaltefil1, maaltefil2, maaltefil3):
    x1, B_2R = unpacking_to_array(maaltefil1)
    x2, B_R = unpacking_to_array(maaltefil2)
    x3, B_R_2 = unpacking_to_array(maaltefil3)
    x1 -= 0.2565
    x2 -= 0.2545
    x3 -= 0.257

    x_new1 = np.linspace(x1[10], x1[-1], 100)
    x_new2 = np.linspace(x2[10], x2[-1], 100)
    x_new3 = np.linspace(x3[10], x3[-1], 100)


    error_x_verdier1, error_B_verdier1 = lag_error_punkter(x1, B_2R)
    error_x_verdier2, error_B_verdier2 = lag_error_punkter(x2, B_R)
    error_x_verdier3, error_B_verdier3 = lag_error_punkter(x3, B_R_2)

    plt.plot(x1, B_2R, label="Måledata a=2R", linestyle='dashed', color='r')
    plt.plot(x2, B_R, label="Måledata a=R", linestyle='dashed', color='b')
    plt.plot(x3, B_R_2, label="Måledata a=R/2", linestyle='dashed', color='g')

    plt.plot(x_new1, B_felt_antihelmholtz(x_new1, 2*R), label="Beregnet a=2R", color='r')
    plt.plot(x_new2, B_felt_antihelmholtz(x_new2, R), label="Beregnet a=R", color='b')
    plt.plot(x_new3, B_felt_antihelmholtz(x_new3, R/2), label="Beregnet a=R/2", color='g')

    plt.margins(0.03)
    plt.errorbar(error_x_verdier1, error_B_verdier1, yerr=0.0486, fmt="m|", label="Standardavvik")
    plt.errorbar(error_x_verdier2, error_B_verdier2, yerr=0.0486, fmt="m|")
    plt.errorbar(error_x_verdier3, error_B_verdier3, yerr=0.0486, fmt="m|")

    plt.xlabel("x [m]")
    plt.ylabel("B [Gauss]")

    plt.legend(loc=2, prop={'size': 10})
    #plt.savefig('antihelmot3.pdf')
    plt.show()
brgn_og_maalte_graf("antihelmot2_2R.txt", "antihelmot2_R.txt", "antihelmot2_R_2.txt")

def avvik_graf(maaltefil_2R, maaltefil_R, maaltefil_R_2):
    x1, B_2R = unpacking_to_array(maaltefil_2R)
    x2, B_R = unpacking_to_array(maaltefil_R)
    x3, B_R_2 = unpacking_to_array(maaltefil_R_2)
    x1 -= 0.2545
    x2 -= 0.2545
    x3 -= 0.2545

    brgn_2R = B_felt_antihelmholtz(x1, 2*R)
    brgn_R = B_felt_antihelmholtz(x2, R)
    brgn_R_2 = B_felt_antihelmholtz(x3, R/2)

    avvik_2R = brgn_avvik(B_2R, brgn_2R)
    avvik_R = brgn_avvik(B_R, brgn_R)
    avvik_R_2 = brgn_avvik(B_R_2, brgn_R_2)

    gj_2R = np.mean(avvik_2R)
    gj_R = np.mean(avvik_R)
    gj_R_2 = np.mean(avvik_R_2)

    plt.plot(x1, avvik_2R, label="Avvik, a=2R", color='r')
    plt.axhline(y=gj_2R, color='r', linestyle='dashed', label='Gjennomsnittlig avvik a=2R')
    plt.plot(x2, avvik_R, label="Avvik, a=R", color='b')
    plt.axhline(y=gj_R, color='b', linestyle='dashed', label='Gjennomsnittlig avvik a=R')
    plt.plot(x3, avvik_R_2, label="Avvik, a=R/2", color='g')
    plt.axhline(y=gj_R_2, color='g', linestyle='dashed', label='Gjennomsnittlig avvik a=R/2')

    plt.xlabel("x [m]")
    plt.ylabel("Avvik i B [Gauss]")
    plt.title('Absolutte avvik Anti-Helmholtz')
    plt.legend()

    plt.show()

