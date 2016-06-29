import numpy as np
import random
import pyevolve
from matplotlib import pyplot as plt

def makeBeliefs(): #First part of binary string
        
    g = random.randint(1,10)  
    p = random.randint(1,10)
    a = random.randint(1,10)     
    
    gamma = '{0:04b}'.format(g)
    psi = '{0:04b}'.format(p)
    alfa = '{0:04b}'.format(a)
    
    beliefes = []
    beliefes = gamma + psi + alfa 
        
    return beliefes
    
def makeIntentions():   #Second part of binary string
          
    g = random.randint(1,10)  
    p = random.randint(1,10)
    a = random.randint(1,10)     
    
    gamma = '{0:04b}'.format(g)
    psi = '{0:04b}'.format(p)
    alfa = '{0:04b}'.format(a)
    
    intentions = []
    intentions = gamma + psi + alfa
    
    return intentions
    
def makeDesire():   #Third part of the binary string
   
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
   
    Chromosome = []
    
    beliefs = makeBeliefs() 
    intentions = makeIntentions()
    desire = makeDesire()
    
    Chromosome = beliefs + intentions + desire
    
    return Chromosome
   
def genAlgorithm(genetic_pool): 
    pass

def calculateBelief(gamma, psi, alfa):

    gamma = int(gamma,2)
    psi = int(psi,2)
    alfa = int(alfa,2)

    #return BeliefVal

def calculateIntention(gamma, psi, alfa):
    
    gamma = int(gamma,2)
    psi = int(psi,2)
    alfa = int(alfa,2)
    #return IntentionVal

def calculateDesire(gamma, psi, alfa):
    
    gamma = int(gamma,2)
    psi = int(psi,2)
    alfa = int(alfa,2)
    #return DesireVal

def splitGenes(Chromosome):

    #print Chromosome

    B_gamma = Chromosome[:4]
    B_psi = Chromosome[4:8]
    B_alfa = Chromosome[8:12]
    
    calculateBelief(B_gamma, B_psi, B_alfa)

    I_gamma = Chromosome[12:16]
    I_psi = Chromosome[16:20]
    I_alfa = Chromosome[20:24]

    calculateIntention(I_gamma, I_psi, I_alfa)

    D_gamma = Chromosome[24:28]
    D_psi = Chromosome[28:32]
    D_alfa = Chromosome[32:36]

    calculateDesire(D_gamma, D_psi, D_alfa)
    

def splitPool(genetic_pool):    #How good the Sender Chromosomes are
    
    #print genetic_pool
    
    for i in genetic_pool:
        splitGenes(i)
    
    
def createPopulation(num_pop): #List of chromosomes 
     
    population = []
    
    for i in xrange(0, num_pop):
        c = createChromosome()
        population.append(c)
     
    return population        
        
if __name__ == "__main__":
            
    genetic_pool = createPopulation(3)
    splitPool(genetic_pool)
    