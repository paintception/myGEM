def create_new_gen(sorted_pool):
	pass
	#print "Sorted Pool", sorted_pool
	
	#return new_gen

def run_alg(pool, scores):
	
	merged_pool = zip(pool, scores)
	sorted_pool = sorted(merged_pool, key=lambda x: x[1], reverse=True)

	print "merged_pool", merged_pool	
	print "Sorted Pool", sorted_pool

	create_new_gen(sorted_pool)

	#return new_gen
#pool = run_alg()