from matplotlib import pyplot as plt
import random

def makeplots(number_generations, sc):

    plt.xlabel('Number of Generations')
    plt.ylabel('Succes of the Agent')
    plt.title('Sender Model')
    plt.ylim([80,100])
    plt.plot(number_generations, sc)
    plt.show()


def analyze_Chromo(chromo):

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

    print "D_alfa", D_alfa
    print "D_psi", D_psi
    print "D_gamma", D_gamma
    print "================================"

    print "I_alfa", I_alfa
    print "I_psi", I_psi
    print "I_gamma", I_gamma
    print "================================"
    