n_survive = 70

def one_point_crossover(parent_1, parent_2):

	cross_over_1_1 = parent_1[:4]
	cross_over_1_2 = parent_2[:4]
	
	child_1 = parent_1.replace(parent_1[:4], cross_over_1_2)
	child_2 = parent_2.replace(parent_2[:4], cross_over_1_1)

	return child_1, child_2

def create_next_gen(filtered_gen):	#Fittest pool ready to reproduce
									#One Point Cross-Over Method is used
	
	print "Generation for the Algorithm", len(filtered_gen)
	next_gen = []

	for i in xrange(0,len(filtered_gen)-1):
		c1, c2 = one_point_crossover(filtered_gen[i], filtered_gen[i+1])
		next_gen.append(c1)
		next_gen.append(c2)

	print "Next Generation:", len(next_gen)		

	return next_gen

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

	#print "merged_pool", merged_pool	
	#print "Sorted Pool", sorted_pool

	filtered_gen = prepare_pool(sorted_pool)
	new_gen = create_next_gen(filtered_gen)
	
	return new_gen
