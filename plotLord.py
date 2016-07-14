from matplotlib import pyplot as plt
import random

def succes_plot(generations, standardscores):

	plt.figure('Figure 1')
	plt.xlabel('Number of Generations')
	plt.ylabel('Succes of the Agent')
	plt.title('Sender Model')
	plt.ylim([80,100])
	plt.plot(generations, standardscores)
	plt.show()

def split_for_plotting(w_gene, b_gene):
	pass

def individual_stats(worst, best):
	print "==================================================="
	min_index = random.randrange(len(worst))
	Worst_gene_to_analyze = worst[min_index]
	print "Worst Gene", Worst_gene_to_analyze

	max_index = random.randrange(len(best))
	Best_gene_to_analyze = best[min_index]
	print "Best Gene", Best_gene_to_analyze
	
	split_for_plotting(Worst_gene_to_analyze, Best_gene_to_analyze)