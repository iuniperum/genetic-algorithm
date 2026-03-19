import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import random


print("Prease enter the maximum number of generations: ")
MAX_GEN = int(input())
MAX_WEIGHT = 0
MUTATION_PROBABILITY = 0.05


weights = [1, 2, 5, 4, 6, 3, 7, 8, 10, 4]
prices = [1, 6, 11, 4, 5, 1, 3, 7, 2, 3]


population = []
buffor = []


class chromosome:
   def __init__(self, fitness, code):
       self.fitness = fitness #niech sam się liczy
       self.code = code
       self.range_up = 0
       self.range_down = 0


def count_f(code):
   count = 0
   for i, bit in enumerate(code):
       if bit == "1":
           count +=  prices[i]
   return count


def count_weight(code):
   weight = 0
   for i, bit in enumerate(code):
       if bit == "1":
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
   for i, ch in enumerate(list):
       ch.range_up = wheel
       wheel += ch.fitness
       wheel -= 1
       ch.range_down = wheel
       wheel += 1
   parent_1 = random.randint(1, wheel - 1)
   parent_1 = (check_which(population, parent_1))
   parent_2 = random.randint(1, wheel - 1)
   parent_2 = (check_which(population, parent_2))
   return (parent_1, parent_2)


#GENETIC OPERATIONS
def crossing_over(parent_1, parent_2):
   CHR_LENGTH = len(population[0].code)
   point = random.randint(1, CHR_LENGTH - 1)


   print(parent_1[0:point] + " " + parent_2[point:])
   chr_1 = parent_1[0:point] + parent_2[point:]
   child_1 = chromosome(count_f(chr_1.strip()), chr_1.strip())
   buffor.append(child_1)


   print(parent_2[0:point] + " " + parent_1[point:])
   chr_2 = parent_2[0:point] + parent_1[point:]
   child_2 = chromosome(count_f(chr_2.strip()), chr_2)
   buffor.append(child_2)


def mutation (chr):
   prob = np.random.rand(len(chr))
   for i, bit in enumerate(chr):
       if prob[i] <= MUTATION_PROBABILITY:
           if bit == 1:
               bit = 0
           elif bit == 0:
               bit = 1
           print ("Mutation occured! ")


filename = sys.argv[1]
with open(filename) as file:
   for line in file:
       new = chromosome(count_f(line.strip()), line.strip())
       population.append(new)


for i in population:
   for j in population:
       if len(i.code) != len(j.code):
           print("Chromosome lengths are not equal!")
           sys.exit()


for i in range(MAX_GEN):
   print("GENERATION NO. " + str(i + 1))
   print("Parents: ")
   for i in population:
       print(i.code)
   print("\n")
   while len(buffor) != len(population):
       pair = roulette(population)
       print("Chosen parents: ")
       print(str(population[pair[0]].code) + ", fitness = " + str(population[pair[0]].fitness))
       print(population[pair[1]].code + ", fitness = " + str(population[pair[1]].fitness))
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

