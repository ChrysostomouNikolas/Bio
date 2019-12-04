#Nikolas Chrysostomou
#Computer Science Year3
#Biocomputaion

import random #we will be using random numbers in our code so we call the radom library/module 

_N=60#Gene length
_P=100#Population Size
_MR=1#mutation rate
_lengthOfRule=6#a constant for the length of the dataset

data=open("data1.txt", "r")
text=data.readlines()# We reference the Data1.txt that we were given 

class Rule:
    def __init__(self, condition, action):
        self.condition=list(condition)
        self.action=action# we create need the Rule class in order to get the data from the data1.txt and  we search for 
                        #similar pattern to  the aim is to find patterns similar to the one from the txt file and if we do we get their 
global_rulebase=[]      #valua(1) and we add  them to our list
for i in range(1, 33):
    line = text[i].split(" ")
    condition = list(map(int, list(line[0])))
    output = int(line[1][0])
    global_rulebase.append(Rule(condition, output))
    print()

class Individual:
    def __init__(self, genes = None):# we create the calss for our individuals  and give them an original fitness of 0
        self.genes=genes
        self.fitness = 0
        if genes == None:   # if the genes re empty we'll loop by giving them values of 0 and 1  based on our length for them
            self.genes = []
            for i in range(_N):# for each gene in their length
                if (i+1) % _lengthOfRule == 0:
                    self.genes.append(random.randint(0, 1))
                else:
                    self.genes.append(random.randint(0, 2))

    def fitness_function(self): #the next thing we need is to change their fitness  and seperate them by slicing them. 
        self.fitness=0
        local_rulebase=[]
        for i in range(0, _N, _lengthOfRule):# we seperate the genes to rules the first one beeing our condition while the rest (1)is our action
            line=self.genes[slice(i, i+_lengthOfRule, 1)]
            condition=line[slice(0, _lengthOfRule-1)]   # we also slice the individual into 10 rules
            action=line[_lengthOfRule-1]
            local_rulebase.append(Rule(condition, action))
        
        for i in range(32):     # we check each bit  to see if it matches with the file
            for j in range(10):
                matches=0
                for l in range(_lengthOfRule-1):
                    if local_rulebase[j].condition[l] == global_rulebase[i].condition[l] or local_rulebase[j].condition[l] == 2:
                        matches += 1
                if matches == _lengthOfRule - 1:
                    if local_rulebase[j].action == global_rulebase[i].action:
                        self.fitness += 1
                    break

class Generation:
    def __init__(self, individuals = None): # the class of generation includes many individuals 
        self.individuals = individuals      # we create as many individuals to fill the size of the generations
        if individuals == None:
            self.individuals = []
            for i in range(_P):
                self.individuals.append(Individual())

    def fitness_function(self):
        for individual in self.individuals:# we once again call the function for the fitness for each of the individuals
            individual.fitness_function()

        self.best_fitness = 0  
        total = 0
        for i in range(_P):         # we know also want to find the best fitness so we initialise best as 0 and we start looping in all of them 
            if self.individuals[i].fitness > self.best_fitness:#each time comparing their fitness with best and if an individual fitness is greater
                self.best_fitness = self.individuals[i].fitness# than the best,we saved our newly found fitness as the best.
            total = total + self.individuals[i].fitness#total is a variable used to get all of the individuals fitness and add them together

        self.mean_fitness=total/_P # we get our total of fitness and we devide them with the size of the population to get  the average 


def tournament_selection(generation): 
    offspring = []#is a list used to save the individuals with the best fitness.
    
    for i in range(_P):                 #we loop in the population 
        candidate1 = random.randint(0, _P-1)# we pick to random canditate solutions for  both canditates 
        candidate2 = random.randint(0, _P-1)
        while candidate1 == candidate2:     # we dont want the candidates to be the same with each other  so in case they re we change them
            candidate1 = random.randint(0, _P-1)#P-1 is because in our P=10 so when we loop inside it python counts 0 as a number so we have
            candidate2 = random.randint(0, _P-1)#a total of 11 numbers so it returns error due to size.. so We subtract 1
        if generation.individuals[candidate1].fitness >= generation.individuals[candidate2].fitness:#we compare their fitness values 
            offspring.append(generation.individuals[candidate1])
        else:               #The ones whose fitness is greater than the others re being added in our offspring list
            offspring.append(generation.individuals[candidate2])
    return offspring

def crossover(offspring):   # crossover picks 2 individuals from the offspring  
    for i in range(0, _P, 2):
        crossover_point = random.randint(0, _P-1) #picks  a random point and changes the tails of the 2 individuals
        for j in range(crossover_point, _N-1):
            offspring[i].genes[j], offspring[i+1].genes[j] = offspring[i+1].genes[j], offspring[i].genes[j]
    return offspring

def mutation(offspring):      #the mutation function  is once again using the offspring list
    for i in range(_P):       # the main idea is to  take each gen from each individual from all population
        for j in range(_N):
            if random.randint(0, 100) <= _MR:  # we create a random number  between 0 & 100 and we compare it with our const for MutationRate(MR)
                if (j+1) % _lengthOfRule == 0: # if that number is 0 Or 1 we mutate our number/gene by 1 which is our mutation rate 
                    if offspring[i].genes[j]==0:
                        offspring[i].genes[j]=1
                    else:
                        offspring[i].genes[j]=0
                else:
                    if offspring[i].genes[j]==0:
                        offspring[i].genes[j]=random.randint(1, 2)
                    elif offspring[i].genes[j]==1:
                        offspring[i].genes[j]=random.choice([0, 2])
                    else:
                        offspring[i].genes[j]=random.randint(0, 1)

    return offspring


list_of_generations = []
list_of_generations.append(Generation())#init pop
list_of_generations[0].fitness_function()#evaluate each candidate

for i in range(500):            #this is basically the GA's loop
    offspring=tournament_selection(list_of_generations[0])
    offspring=crossover(offspring)
    offspring=mutation(offspring)
    list_of_generations.append(Generation(offspring))
    list_of_generations[i+1].fitness_function()
    if list_of_generations[i+1].best_fitness==17:
        break

print()




