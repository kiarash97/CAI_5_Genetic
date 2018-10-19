import random

class genome:
    def __init__(self,lst):
        self.gens = []
        for i in lst:
            self.gens.append(i)

        #random gens
        if len(lst) == 0 :
            self.randomGens()

    def randomGens(self):
        while (len(self.gens) < 8):
            x = random.randint(0,7)
            if x not in self.gens:
                self.gens.append(x)

    def isCorrect(self):
        for i in self.gens:
            if self.gens.count(i) != 1 :
                return False
        return True
    def __str__(self):
        return str(self.gens)

def initialize_population(num = 100):
    population = []
    for i in range(num):
        population.append(genome(lst = []))
    return population

def one_point_cross_over(gen1 , gen2):
    cross_point = random.randint(0,6)
    result = []
    result.append(gen1.gens[0:cross_point])
    result = result[0]
    i = cross_point

    while len(result)<8:
        if gen2.gens[i] not in result :
            result.append(gen2.gens[i])
        i+=1
        if i>7:
            i=0

    result = genome(lst = result)

    if result.isCorrect():
        return result
    else :
        return False

def mutation(gen ,p = 0.001):
    for i in range(len(gen.gens)):
        if random.random() < p :
            x = random.randint(0,7)
            s = gen.gens.index(x)
            gen.gens[i] , gen.gens[s] = gen.gens[s] , gen.gens[i]

def fitness(gen):
    threat_count = 0
    max_threat = 28
    for i in range(len(gen.gens)):
        for j in range(i,len(gen.gens)):
            if i != j :
                if i-gen.gens[i] == j-gen.gens[j] or i+gen.gens[i] == j+gen.gens[j]:
                    threat_count +=1
    return max_threat-threat_count

def sort_by_fitness(population):
    result = []
    for i in range(len(population)):
        for j in range(len(population)):
            if fitness(population[i]) > fitness(population[j]):
                population[i] , population[j] = population[j] , population[i]

def genetic(initPopulationSize = 100 , pairsNumber = 100, populationSize = 30 , mutationProbability = 0.001):

    generation = 1
    population = initialize_population(num= initPopulationSize)
    sort_by_fitness(population)
    while True:
        print ("genaration = ",generation , "population number = ", len(population))
        if fitness(population[0]) == 28:
            print("Urekaaa !! ")
            return population[0]

        #each epoch
        for i in range(pairsNumber):
            x= random.randint(0,len(population)-1)
            y= random.randint(0,len(population)-1)
            if x!=y :
                child = one_point_cross_over(population[x],population[y])
                if child:
                    mutation(child , p=mutationProbability)
                    population.append(child)

        sort_by_fitness(population)
        population = population[0:populationSize]
        generation += 1



result = genetic(initPopulationSize = 100 , pairsNumber = 100, populationSize = 30 , mutationProbability = 0.001)
print ("answer = " , result)

