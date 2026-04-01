import matplotlib.pyplot as plt
import numpy as np
import sys
import random

"""
LISTA DO STRINGU
"""

weights = []
prices = []

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

population = []
buffor = []

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
       if num >= ch.range_up and num <= ch.range_down:
           return i


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


   print(parent_1[0:point] + " " + parent_2[point:])
   chr_1 = np.concatenate((parent_1[0:point], parent_2[point:]))
   child_1 = chromosome(chr_1)
   buffor.append(child_1)


   print(parent_2[0:point] + " " + parent_1[point:])
   chr_2 = np.concatenate((parent_2[0:point], parent_1[point:]))
   child_2 = chromosome(chr_2)
   buffor.append(child_2)


def mutation (chr):
   prob = np.random.rand(len(chr))
   for i, bit in enumerate(chr):
       if prob[i] <= MUTATION_PROBABILITY:
           if bit == 1:
               chr[i] = 0
           elif bit == 0:
               chr[i] = 1
           print ("Mutation occured! ")

#FIRST POPULATION - RANDOM SOLUTIONS
print("Please enter size of the population: ")
x = int(input())
for i in range(x):
    code = np.random.randint(2, size=EL_NUM)
    while(count_weight(code) > MAX_WEIGHT):
        code = np.random.randint(2, size=EL_NUM)
    #code = ''.join(str(x) for x in code)
    new = chromosome(code)
    population.append(new)

for i in range(MAX_GEN):
   print("GENERATION NO. " + str(i + 1))
   print("Parents: ")
   for i in population:
       print(i.code)
   print("\n")
   while len(buffor) != len(population):
       pair = roulette(population)
       print("Chosen parents: ")
       print(population[pair[0]].code)
       print ("fitness = " + str(population[pair[0]].fitness))
       print(population[pair[1]].code)
       print ("fitness = " + str(population[pair[1]].fitness))
       parents = [population[pair[0]].code, population[pair[1]].code]
       crossing_over(parents[0], parents[1])
       print("\n")
   population.clear()
   for i in buffor:
       population.append(i)
   buffor.clear()
   for i in population:
       mutation(i.code)
   print("Children: ")
   for i in population:
       print(i.code)
   print("\n")


for i in population:
   print(i.code + ", fitness = " + str(i.fitness))