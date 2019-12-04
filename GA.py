#Nikolas Chrysostomou
#Computer Science Year3
#Biocomputaion

import random       # since we ll be using random in our code we need to call in the random library 

_N=10   #Gene length
_P=10   #Population Size
_MR=1   #mutation rate

class Individual:
    def __init__(self, genes = None):# we create the calss for our individuals  and give them an original fitness of 0
        self.genes=genes
        self.fitness = 0
        if genes == None:  # if the genes re empty we'll loop by giving them values of 0 and 1  based on our length for them
            self.genes = []
            for i in range(_N):                        # for each gene in their length
                self.genes.append(random.randint(0, 1))# get a random value of 0 or 1

    def fitness_function(self):     #once we created a rndom individual we give them 
        self.fitness=sum(self.genes)# their fitness value based on their gens with number 1 using the sum() method

class Generation:
    def __init__(self, individuals = None):  # the class of generation is created with the help of individuals
        self.individuals = individuals       # we create as many individuals as the size of the population
        if individuals == None:
            self.individuals = []
            for i in range(_P):
                self.individuals.append(Individual())

    def fitness_function(self):             # we also get the fitness of the newly created individuals by calling our
        for individual in self.individuals: # fitness.function
            individual.fitness_function()

        self.best_fitness = 0   # a variable created for best fitness
        total = 0               # a variable for total of fitness
        for i in range(_P):                                    #we loop in the entire population
            if self.individuals[i].fitness > self.best_fitness:#each time comparing their fitness with best and if an individual fitness is 
                self.best_fitness = self.individuals[i].fitness#greater the best,we saved our newly found fitness as the best.
            total = total + self.individuals[i].fitness        #we re using our total to get all of the  fitness into one variable

        self.mean_fitness=total/_P # we get our and we devide them with the size of the population to get the average  


def tournament_selection(generation):
    offspring = [] #is a list used to save the individuals with the best fitness.
    
    for i in range(_P):
        candidate1 = random.randint(0, _P-1)    # we pick 2 random canditate solutions for  both canditate variables 
        candidate2 = random.randint(0, _P-1)  
        while candidate1 == candidate2:         # we dont want the candidates to be the same with each other  so in case they re we change them
            candidate1 = random.randint(0, _P-1)#P-1 is because in our P=10 so when we loop inside it python counts 0 as a number so we have
            candidate2 = random.randint(0, _P-1)#a total of 11 numbers so it returns error due to size.. so We subtract 1
        if generation.individuals[candidate1].fitness >= generation.individuals[candidate2].fitness: #we compare their fitness values
            offspring.append(generation.individuals[candidate1])
        else:   #The ones whose fitness is greater than the others re being added in our offspring list
            offspring.append(generation.individuals[candidate2])
    return offspring   #return offspring

def crossover(offspring):  # crossover picks 2 individuals from the offspring 
    for i in range(0, _P, 2):
        crossover_point = random.randint(0, _P-1) #picks  a random point and changes the tails of the 2 individuals
        for j in range(crossover_point, _P-1):
            offspring[i].genes[j], offspring[i+1].genes[j] = offspring[i+1].genes[j], offspring[i].genes[j]
    return offspring

def mutation(offspring):   #the mutation function  is once again using the offspring list
    for i in range(_P):     # the main idea is to  take each gen from each individual from all population
        for j in range(_N):
            if random.randint(0, 100) <= _MR:# we create a random number  between 0 & 100 and we compare it with our const for MutationRate(MR)
                if offspring[i].genes[j] == 0: # if that number is 0 Or 1 we mutate our number/gene by 1 which is our mutation rate
                    offspring[i].genes[j] == 1
                else:
                    offspring[i].genes[j] == 0
    return offspring


list_of_generations = []
list_of_generations.append(Generation())#init pop
list_of_generations[0].fitness_function()#evaluate each candidate

for i in range(100):
    offspring=tournament_selection(list_of_generations[0])
    offspring=crossover(offspring)
    offspring=mutation(offspring)
    list_of_generations.append(Generation(offspring))
    list_of_generations[i+1].fitness_function()
    if list_of_generations[i+1].best_fitness==10:
        break

print()




