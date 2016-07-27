import random

n_survive = 70	

def three_parent_crossover(parent_1, parent_2, parent_3):

	child = []

	for i,j,k in zip(parent_1,parent_2,parent_3):
	    if i == j:
	   		child.append(i)
	    else:
	        child.append(k)

	child = ''.join(child)

	return child

def single_crossover(parent_1, parent_2):
		
		parent_1 = ''.join(str(e) for e in parent_1)
		parent_2 = ''.join(str(e) for e in parent_2)

		cross_over_1_1 = parent_1[:3]
		cross_over_1_2 = parent_2[:3]

		child1 = parent_1.replace(parent_1[:3], cross_over_1_2)
		child2 = parent_2.replace(parent_2[:3], cross_over_1_1)

		return child1, child2

def random_mutation(generation):
	
	index = random.randrange(len(generation))
	gene_to_mutate = generation[index]

	#print "Gene to mutate:", gene_to_mutate

	list_gene_to_mutate = list(gene_to_mutate)

	index = random.randint(0,len(list_gene_to_mutate)-1)
		
	for i, j in enumerate(list_gene_to_mutate):
		if i == index:
			if j == "0":
				list_gene_to_mutate[i] = 1
			elif j == "1":
				list_gene_to_mutate[i] = 0
			else:
				raise Exception("Chromosome is not supported!")
		
	mutated_gen = ''.join(str(e) for e in list_gene_to_mutate)
	generation[index] = mutated_gen
	
	return generation

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
	
	new_gen = []

	for i in xrange(0,len(filtered_gen)-1):
		c1, c2 = single_crossover(filtered_gen[i], filtered_gen[i+1])
		new_gen.append(c1)
		new_gen.append(c2)

	mutated_gen = random_mutation(new_gen)
	#print "Length of the newest generation:", len(mutated_gen)
	
	return mutated_gen