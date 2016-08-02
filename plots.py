import seaborn as sns
import pylab
import numpy as np
from matplotlib import pyplot as plt
import random
import os

Beliefes_Set = []
Desires_Set = []
Intentions_Set = []

def makeplots(number_generations, sc):		#Plot that shows the increase of performance during one single Simulation
    
    plt.xlabel('Number of Generations')
    plt.ylabel('Succes of the Agent')
    plt.title('Criminal Model')
    plt.ylim([65, 100])
    plt.plot(number_generations, sc)
    plt.savefig('res/GenAl/genAl.png')
    plt.show()

def Final_StatPlots(b, d, i):		#Final Stats of the BDI Architecture

    belief_counter = ([[x,b.count(x)] for x in set(b)]) 
    desire_counter = ([[x,d.count(x)] for x in set(d)]) 
    intention_counter = ([[x,i.count(x)] for x in set(i)]) 

    b_values = []
    b_occurences = []
    d_values = []
    d_occurences = []
    i_values = []
    i_occurences = []

    for i in belief_counter:
         b_values.append(i[0])
         b_occurences.append(i[1])
    
    for j in desire_counter:
         d_values.append(j[0])
         d_occurences.append(j[1])
    
    for k in intention_counter:
         i_values.append(k[0])
         i_occurences.append(k[1])
    
    b_values = np.array(b_values)
    d_values = np.array(d_values)
    i_values = np.array(i_values)

    plt.xlabel('Feature Values')
    plt.ylabel('Feature Occurance')
    plt.title('Criminal Scores')
    plt.ylim([0,40]) 
    
    ax = plt.subplot(111)
    ax.bar(b_values-0.25, b_occurences,width=0.2,color='gold',align='center')
    ax.bar(d_values, d_occurences,width=0.2,color='blue',align='center')
    ax.bar(i_values+0.25, i_occurences,width=0.2,color='red',align='center')

    b_values = b_values.tolist()
    d_values = d_values.tolist()
    i_values = i_values.tolist()

    plt.savefig('res/BDI/BDI_features.png')
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
    
    
