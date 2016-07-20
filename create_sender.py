import random

"""
    List of TODOs

    - Check this stuff the Architecture makes sense!!! max_Beliefs = 22 max_Intentions = 22  max_Desire = 20 Optimal_Score = 64
    - Consider >= 64 results in the Fitness f(x)
"""

def makeBeliefs(): #First part of binary string, Corresponds to the Beliefs of the Agent
    
    g = random.randint(1,10)  
    p = random.randint(1,10)
    a = random.randint(1,10)     
    
    gamma = '{0:04b}'.format(g)
    psi = '{0:04b}'.format(p)
    alfa = '{0:04b}'.format(a)
    
    beliefes = []
    beliefes = gamma + psi + alfa 
        
    return beliefes
    
def makeIntentions():   #Second part of binary string, Corresponds to the Intentions of the Agent
          
    g = random.randint(1,10)  
    p = random.randint(1,10)
    a = random.randint(1,10)     
    
    gamma = '{0:04b}'.format(g)
    psi = '{0:04b}'.format(p)
    alfa = '{0:04b}'.format(a)
    
    intentions = []
    intentions = gamma + psi + alfa
    
    return intentions
    
def makeDesire():   #Third part of the binary string, Corresponds to the Desirs of the Agent
   
    g = random.randint(1,10)  
    p = random.randint(1,10)
    a = random.randint(1,10)     
    
    gamma = '{0:04b}'.format(g)
    psi = '{0:04b}'.format(p)
    alfa = '{0:04b}'.format(a)
    
    desire = []
    desire = gamma + psi + alfa

    return desire

def createChromosome(): #Creates one single Chromosome of the population
                        #According to the BDI Architecture
    Chromosome = []
    
    beliefs = makeBeliefs() 
    intentions = makeIntentions()
    desire = makeDesire()
    
    Chromosome = beliefs + intentions + desire
    
    return Chromosome

def splitGenesAndScores(Chromosome):   #Every Agent is separated and individual feature scores are computed
                                       #Returns a Score for every member of the population 
    
    #print "This is one single Agent:", Chromosome

    B_gamma = Chromosome[:4]
    B_psi = Chromosome[4:8]
    B_alfa = Chromosome[8:12]
    
    Score_B_gamma = int(B_gamma,2)
    Score_B_psi = int(B_psi,2)
    Score_B_alfa = int(B_alfa,2)

    BeliefScore = Score_B_gamma + Score_B_psi + Score_B_alfa   
    
    #print "These are the Belief features:", B_gamma, B_psi, B_alfa
    
    I_gamma = Chromosome[12:16]
    I_psi = Chromosome[16:20]
    I_alfa = Chromosome[20:24]

    Score_I_gamma = int(I_gamma,2)
    Score_I_psi = int(I_psi,2)
    Score_I_alfa = int(I_alfa,2)

    IntentionScore = Score_I_gamma + Score_I_psi + Score_I_alfa    

    #print "These are the Intention features:", I_gamma, I_psi, I_alfa
    
    D_gamma = Chromosome[24:28]
    D_psi = Chromosome[28:32]
    D_alfa = Chromosome[32:36]

    Score_D_gamma = int(D_gamma,2)
    Score_D_psi = int(D_psi,2)
    Score_D_alfa = int(D_alfa,2)

    DesireScore = Score_D_gamma + Score_D_psi + Score_D_alfa   
    
    #print "These are the Desire features:", D_gamma, D_psi, D_alfa
    
    ChromosomeScore = BeliefScore + IntentionScore + DesireScore
    #print "----------------------------------------------------"

    return Chromosome, ChromosomeScore

def createPopulation(num_pop): #A population of Agents is created
                               #List of Chromosomes 
     
    population = []
    
    for i in xrange(0, num_pop):
        c = createChromosome()
        population.append(c)
     
    return population        
