import seaborn as sns
from matplotlib import pyplot as plt
import random

Beliefes_Set = []
Desires_Set = []
Intentions_Set = []


def makeplots(number_generations, sc):

    plt.xlabel('Number of Generations')
    plt.ylabel('Succes of the Agent')
    plt.title('Sender Model')
    plt.ylim([80,100])
    plt.plot(number_generations, sc)
    plt.show()

def GenerationPlot(bel, des, inten):

    scatter_bel = [0] * len(bel)
    scatter_des = [1] * len(des)
    scatter_inten = [2] * len(inten)

    plt.xlabel('BDI Features')
    plt.ylabel('Scores')
    plt.scatter(scatter_bel, bel, s=40, lw=0, color='gold', marker='o', label=r'B')
    plt.scatter(scatter_des, des, s=40, lw=0, color='blue', marker='^', label=r'D')
    plt.scatter(scatter_inten, inten, s=40, lw=0, color='red', marker='*', label=r'I')
    plt.legend(loc='lower right')

    plt.show()

def analyze_Generation(chromo):

    Beliefes = chromo[0:12]
    Desires = chromo[12:24]
    Intentions = chromo[24:36]
    
    B_alfa = int(Beliefes[0:4],2)
    B_psi = int(Beliefes[4:8],2)
    B_gamma = int(Beliefes[8:12],2)

    D_alfa = int(Desires[0:4],2)
    D_psi = int(Desires[4:8],2)
    D_gamma = int(Desires[8:12],2)

    I_alfa = int(Intentions[0:4],2)
    I_psi = int(Intentions[4:8],2)
    I_gamma = int(Intentions[8:12],2)

    print "================================"
    print "B_alfa", B_alfa
    print "B_psi", B_psi
    print "B_gamma", B_gamma
    print "================================"
    
    Beliefes_Set.extend((B_alfa, B_psi, B_gamma))
    
    print "D_alfa", D_alfa
    print "D_psi", D_psi
    print "D_gamma", D_gamma
    print "================================"

    Desires_Set.extend((D_alfa, D_psi, D_gamma))

    print "I_alfa", I_alfa
    print "I_psi", I_psi
    print "I_gamma", I_gamma
    print "================================"

    Intentions_Set.extend((I_alfa, I_psi, I_gamma))

    return Beliefes_Set, Desires_Set, Intentions_Set
    
    