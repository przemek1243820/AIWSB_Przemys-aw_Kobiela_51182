import pygad
import numpy
import time
import matplotlib.pyplot as plt

S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]
S2 = [25, 46, 12, 32, 22, 1, 23, 54, 12, 46, 11, 21, 90, 6, 56, 12, 74, 64, 19, 20, 51, 58, 23, 46, 12]
S3 = [6, 23, 27, 13, 12, 1, 54, 12, 65, 100, 12, 65, 13, 15, 16,
      5, 20, 67, 18, 22, 6, 2, 65, 64, 27, 85, 62, 80, 21, 13, 22, 32, 13, 54, 16]
S4 = [100, 63, 2, 65, 22, 23, 2, 41, 1, 93, 56, 13, 26, 13, 95,
      23, 12, 14, 63, 82, 17, 30, 64, 27, 22, 16, 2, 37, 42, 17, 21, 6, 7, 8, 2, 12, 89, 93, 12, 7, 23, 4, 1, 9, 13]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = -numpy.abs(sum1-sum2)
    #lub: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
    return fitness

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 15
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 5
wielkosci = [len(S), len(S2), len(S3), len(S4)]
print("wielkosci: ", wielkosci)
sum_time = 0

for i in range(0,10,1):
    start = time.time()
    #inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=["reach_0", "saturate_15"])

    #uruchomienie algorytmu
    ga_instance.run()
    end = time.time()
    sum_time = sum_time + (end - start)
    print("czas: ", end - start)
print("średni czas: ", sum_time/10)
print("liczba generacji: ", ga_instance.generations_completed)

plt.plot([wielkosci],[sum_time/10])
plt.ylabel('some numbers')
plt.show()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = numpy.sum(S*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()