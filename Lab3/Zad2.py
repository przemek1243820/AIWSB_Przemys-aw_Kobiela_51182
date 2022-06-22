import pygad
import numpy

ilosc = numpy.arange(1,12)
wartosc = [100, 300, 200, 40,500,70,100,250,300,280,300]
waga = [7,7,6,2,5,6,1,3,10,3,15]
nazwy = ["zegar","obraz-pejzaz", "ograz-portret","radio","laptop","lampka_nocna",
         "srebrne_szt","porcelana","figura_z_brazu","skorzana_torebka", "odkurzacz"]
n = 25
suma_wart = 0
suma_wag = 0
tab =[]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    global suma_wart
    global suma_wag
    global tab
    sum1 = numpy.sum(solution * wartosc)
    sum2 = numpy.sum(solution * waga)
    if(sum1 > suma_wart and sum2<=n):
        tab = []
        suma_wart = sum1
        suma_wag = sum2
        for i in range(0, 10, 1):
            if (solution[i] == 1):
                tab.append(nazwy[i])
    else:
        sum2=0
        sum1=0
    fitness = sum2
    fitness2 = suma_wart
    print("waga: ", suma_wag, " oraz kwota: ", suma_wart)
    print(tab)

    return fitness2

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(ilosc)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 100
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

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
                       mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()