import matplotlib.pyplot as plt
import numpy as np
import sys
import random

weights = []
prices = []
best_fits = []

population = []
buffer = []

class chromosome:
   def __init__(self, code):
       self.code = code
       self.fitness = count_f(self.code)
       self.range_up = 0
       self.range_down = 0


def count_f(code):
   count = 0
   for i, bit in enumerate(code):
       if bit == 1:
           count +=  prices[i]
   return count


def count_weight(code):
   weight = 0
   for i, bit in enumerate(code):
       if bit == 1:
           weight +=  weights[i]
   return weight


def check_which(list, num):
    for i, ch in enumerate(list):
       if num <= ch.range_up and num >= ch.range_down:
           return i
    return 0

def find_best(list):
    fits = []
    for i in list:
        fits.append(i.fitness)
    return max(fits)


#SELECTION: Parents are chosen randomly
#Probability of choosing a chromosome is proportionate to its fitness value
def roulette(list):
   wheel = 1
   for ch in list:
       ch.range_down = wheel
       wheel += ch.fitness
       wheel -= 1
       ch.range_up = wheel
       wheel += 1
   parent_1 = random.randint(1, wheel)
   parent_1 = (check_which(population, parent_1))
   parent_2 = random.randint(1, wheel)
   parent_2 = (check_which(population, parent_2))
   return (parent_1, parent_2)


#GENETIC OPERATIONS
def crossing_over(parent_1, parent_2):
   CHR_LENGTH = len(population[0].code)
   point = random.randint(1, CHR_LENGTH - 1)

   print(str(parent_1[0:point]) + " " + str(parent_2[point:]))
   chr_1 = np.concatenate((parent_1[0:point], parent_2[point:]))
   child_1 = chromosome(chr_1)
   buffer.append(child_1)

   print(str(parent_2[0:point]) + " " + str(parent_1[point:]))
   chr_2 = np.concatenate((parent_2[0:point], parent_1[point:]))
   child_2 = chromosome(chr_2)
   buffer.append(child_2)


def mutation (chr):
   prob = np.random.rand(len(chr.code))
   for i, bit in enumerate(chr.code):
       if prob[i] <= MUTATION_PROBABILITY:
            if bit == 1:
                chr.code[i] = 0
                if(count_weight(chr.code) > MAX_WEIGHT):
                    chr.code[i] = 1
                else:
                    chr.fitness = count_f(chr.code)
            elif bit == 0:
                chr.code[i] = 1
                if(count_weight(chr.code) > MAX_WEIGHT):
                    chr.code[i] = 0
                else:
                    chr.fitness = count_f(chr.code)

#DETERMINING PARAMETERS
print("Press 1 to input values, 2 to use default")
x = int(input())
if x == 1:
    print("Prease enter number of the elements in the knapsack: ")
    EL_NUM = int(input())

    print("Prease enter weights: ")
    for i in range(EL_NUM):
        x  = int(input())
        weights.append(x)

    print("Prease enter prices: ")
    for i in range(EL_NUM):
        x  = int(input())
        prices.append(x)

    print("Prease enter the maximum weight: ")
    MAX_WEIGHT = int(input())

    print("Prease enter the maximum number of generations: ")
    MAX_GEN = int(input())
    print("Prease enter mutation probability: ")
    MUTATION_PROBABILITY = float(input())
    print("Please enter size of the population: ")
    SIZE = int(input())
elif x == 2:
    EL_NUM = 11
    weights = [2, 5, 2, 3, 7, 4, 4, 5, 9, 2, 3]
    prices = [1, 2, 5, 3, 8, 3, 5, 4, 7, 5, 3]
    MAX_WEIGHT = 20
    MAX_GEN = 50
    MUTATION_PROBABILITY = 0.05
    SIZE = 8
else: 
    print("Wrong imput!")
    sys.exit()

#FIRST POPULATION - RANDOM SOLUTIONS
for i in range(SIZE):
    code = np.random.randint(2, size=EL_NUM)
    while(count_weight(code) > MAX_WEIGHT):
        code = np.random.randint(2, size=EL_NUM)
    new = chromosome(code)
    population.append(new)

#MAIN
for i in range(MAX_GEN):
    print("GENERATION NO. " + str(i + 1))
    print("Parents: ")
    for i in population:
        print(i.code)
    best_fits.append(find_best(population))
    print(best_fits)
    print("\n")
    while len(buffer) != len(population):
        pair = roulette(population)
        print("Chosen parents: ")
        print(str(population[pair[0]].code) + ", fitness = " + str(population[pair[0]].fitness))
        print(str(population[pair[1]].code) + ", fitness = " + str(population[pair[1]].fitness))
        parents = [population[pair[0]].code, population[pair[1]].code]
        crossing_over(parents[0], parents[1])
        print("\n")
    
    population.clear()
    for i in buffer:
        population.append(i)
    buffer.clear()
    for i in population:
        mutation(i)
    print("Children: ")
    for i in population:
        print(str(i.code))
    print("\n")


for i in population:
   print(str(i.code) + ", fitness = " + str(i.fitness))

gens = []
for i in range(1, MAX_GEN + 1):
    gens.append(i)

plt.plot(gens, best_fits)
plt.xlabel('Generation')
plt.ylabel('Best fitness value')
plt.title('Best fitness value per generation')
plt.savefig("plot.png")
plt.show()