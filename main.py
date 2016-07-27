import random
from genetic_alg import run_alg
from create_sender import *
from create_criminal import *

def standardization(generation_scores):
    
    standardized_scores = []
    
    for score in generation_scores:
        standardized_scores.append(((score*100)/60))

    return standardized_scores

if __name__ == "__main__":

    from plots import *

    number_simulations = 20

    for i in xrange(0, number_simulations):

        print "Simulation", i, "running"
        
        number_generations = 20       
        scores = []
        generation_scores = []
        Agent_set = []
        
        #TODO add option which agent to simulate!

        #genetic_pool = create_Sender_Population(100) #Creation of random set of Agents
        genetic_pool = create_Criminal_Population(100)

        #print "This is the genetic_algnetic pool:", genetic_pool
        for j in xrange(0,number_generations):
            
            print "Generation:", j

            tot = 0.000
            
            for i in genetic_pool:
                c, s = splitGenesAndScores(i)
                #print "This is the Chromosome", c
                #print "This is his Score", s
                tot += s
                scores.append(s)    #Individual Scores of chromosomes are saved
            tot_score = tot/len(genetic_pool)   #Total Fitness score of the generation
            
            Agent_set.append(genetic_pool)

            if tot_score < 65:
                generation_scores.append(tot_score) #Single Scores are saved in a global list for plotting

            #print "This is the score of the population:", scores

                n = run_alg(genetic_pool, scores)   #Genetic Algorithm is called, with the current genetic pool and the relative scores of the Agents

                genetic_pool = n

        print "Generation Scores:", generation_scores
       
        sc = standardization(generation_scores)
        print "Standardized Scores:", sc

        number_generations = []
        for i in range(len(generation_scores)):
            number_generations.append(i)

        makeplots(number_generations, sc)

        best_set = max(Agent_set)
        best_scores = []

        for i in best_set:
            c, s = splitGenesAndScores(i)
            best_scores.append(s)

        b_i = best_scores.index(max(best_scores))
        b_c = best_set[b_i]

        b, d, i = analyze_Generation(b_c)

    Final_StatPlots(b, d, i)