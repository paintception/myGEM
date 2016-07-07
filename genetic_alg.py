"""
	List of TODOs:

	- The Genetic Algorithm implements only single cross_over. Multiple ways of breeding should be added!
	- Selection of top Agents is given by Truncation method. Roulette Wheel and Tournament Selection should be tried
	- The set of Agents makes children in an exponential way, this should change ---> possible reason of the success shown in the graph
	- Randomness should be added by changing some Chromosomes randomly in order to avoid overfitting
	- Optimal Result is still not reached, might be given by the Algorithm itself
	- Reformat the code sooner or later
	
"""
import random

n_survive = 70
mutation_rate = 10

def one_point_crossover(parent_1, parent_2):

	cross_over_1_1 = parent_1[:4]
	cross_over_1_2 = parent_2[:4]
	
	child_1 = parent_1.replace(parent_1[:4], cross_over_1_2)
	child_2 = parent_2.replace(parent_2[:4], cross_over_1_1)

	return child_1, child_2

def three_parent_crossover(parent_1, parent_2, parent_3):

	child = []

	for i,j,k in zip(parent_1,parent_2,parent_3):
	    if i == j:
	   		child.append(i)
	    else:
	        child.append(k)

	return child


"""
def random_mutation(pool):	#FIXME Still doesn't work

	chromosomes_to_mutate = random.choice(pool)
	
	position_to_mutate = random.randint(0, len(chromosomes_to_mutate)-1)
	
	if chromosomes_to_mutate[position_to_mutate] == "1":
		chromosomes_to_mutate=chromosomes_to_mutate[:position_to_mutate] + "0" + chromosomes_to_mutate[1+position_to_mutate:]
	elif chromosomes_to_mutate[position_to_mutate] == "0":
		chromosomes_to_mutate=chromosomes_to_mutate[:position_to_mutate] + "1" + chromosomes_to_mutate[1+position_to_mutate:]
	else:
		raise Exception("Chromosome Error!")

	pool.append(chromosomes_to_mutate)

	return pool
"""

def create_next_gen(filtered_gen):	#Fittest pool ready to reproduce
									#One Point Cross-Over Method is used
	
	#print "Generation for the Algorithm", len(filtered_gen)
	next_gen_singleCrossover = []
	next_gen_threeParentCrossover = []

	for i in xrange(0,len(filtered_gen)-1):
		c1, c2 = one_point_crossover(filtered_gen[i], filtered_gen[i+1])
		#c = three_parent_crossover(filtered_gen[i], filtered_gen[i+1], filtered_gen[i+2])
		
		next_gen_singleCrossover.append(c1)
		next_gen_singleCrossover.append(c2)
	
		#next_gen_threeParentCrossover.append(c)

	size = (len(next_gen_singleCrossover)*mutation_rate)/100
	pool_to_mutate = []

	for i in xrange(0,size):
		tmp = random.choice(next_gen_singleCrossover)
		pool_to_mutate.append(tmp)

	#mutation = random_mutation(pool_to_mutate)

	return next_gen_singleCrossover

def prepare_pool(sorted_pool):
	
	elements_to_keep = (len(sorted_pool)*n_survive)/100	#Percentage of elements to keep in a generation is computed
	
	tmp = [x[0] for x in sorted_pool]
	genes_to_reproduce = []

	for i, j in enumerate(tmp):
		if i <= elements_to_keep:
			genes_to_reproduce.append(j)

	#print "Genes to Reproduce:", genes_to_reproduce
	return genes_to_reproduce	#Genetic pool is filtered out from weakest Agents

def run_alg(pool, scores):
	
	merged_pool = zip(pool, scores)	#Chromosomes and relative scores are merged together
	sorted_pool = sorted(merged_pool, key=lambda x: x[1], reverse=True) #Descending sorting, higher scores are at the top of the list

	filtered_gen = prepare_pool(sorted_pool)
	new_gen = create_next_gen(filtered_gen)
		
	return new_gen
