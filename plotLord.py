from matplotlib import pyplot as plt
from numpy.random import normal
import random

def succes_plot(generations, standardscores):

	plt.figure('Figure 1')
	plt.xlabel('Number of Generations')
	plt.ylabel('Succes of the Agent')
	plt.title('Sender Model')
	plt.ylim([80,100])
	plt.plot(generations, standardscores)
	plt.show()

def split_for_plotting(gene):
	
	Beliefs = gene[:12]
	Intentions = gene[12:24] 
	Desires = gene[24:]

	gamma_B = int(Beliefs[:4],2)
	psi_B = int(Beliefs[4:8],2)
	alfa_B = int(Beliefs[8:12],2)

	gamma_I = int(Intentions[:4],2)
	psi_I = int(Intentions[4:8],2)
	alfa_I = int(Intentions[8:12],2)

	gamma_D = int(Desires[:4],2)
	psi_D = int(Desires[4:8],2)
	alfa_D = int(Desires[8:12],2)


def individual_stats(worst, best):
	
	print "==================================================="
	min_index = random.randrange(len(worst))
	Worst_gene_to_analyze = worst[min_index]
	print "Worst Gene", Worst_gene_to_analyze

	max_index = random.randrange(len(best))
	Best_gene_to_analyze = best[min_index]
	print "Best Gene", Best_gene_to_analyze
	
	split_for_plotting(Worst_gene_to_analyze)
	split_for_plotting(Best_gene_to_analyze)