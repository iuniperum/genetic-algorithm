# Genetic Algorithm

### Overview
This project implements a genetic algorithm for the Knapsack problem. 
- Genetic algorithm is a metaheuristic inspired by biological mechanisms of natural selection
- The Knapsack problem is a problem in combinatorial optimisation: Given a set of items, each with a weight and a value, determine which items to choose so that the total weight is less than or equal to a given limit and the total value is maximized.

### How to run 
python genetic.py

### Technologies
Python, libraries: matplotlib, numpy, sys, random

### Pipeline
- Generating a set of random solutions
- Determining the quality value of the solutions
- Selecting parents: probability of selection proportionate to the quality value
- Crossing-over: combining parts of the parental solutions to create children 
- Creating a new set of parents with the children 
- Applying random mutations
- Start of the new generation - children are now parents
- Creating a graph of best solution by each generation