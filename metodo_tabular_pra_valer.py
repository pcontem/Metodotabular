# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:16:31 2024

@author: pluca
"""

import numpy as np

#configura o codigo quanto aos valores verdade e ao numero de bits maximo

number_bits = int(input("escolha o numero de bits\n"))

print("insira os valores decimais que resultam em 1, quando quiser parar digite -1")

n = 0
number_true = 0
true_vector= [0,1,2,3,5,7,9,11,13,15]

while number_true != -1:
    number_true = int(input("insira o numero\n"))
    
    if number_true != -1 and number_true <= 2**number_bits - 1:
        true_vector.append(number_true)
        n = n+1
    if number_true > 2**number_bits -1:
        print("numero fora do alcance")
lenght = len(true_vector)      
print(true_vector)

#cria matriz binaria e a preenche com os valores verdade

binary_matrix = np.zeros((lenght, number_bits))
n=0
for x in range(lenght):
    converting = true_vector[x]
    while converting > 0:
        binary_matrix[x,n] = converting % 2
        converting = converting // 2
        n = n+1
    n = 0
    
binary_matrix = np.flip(binary_matrix, 1)
            

#checa por outras entradas com um bit de diferenca e marca pra que casos eles sao solucao
solution_sets = [{true_vector[x]} for x in range(lenght)]
print(solution_sets)
difference_count = 0 
for w in range(number_bits-1):
    for x in range(lenght-1):
        for y in range(x, lenght):
            for z in range(number_bits):
                if binary_matrix[x,z] != binary_matrix[y,z]:
                    difference_count = difference_count + 1
                
            if difference_count == 1:
                for z in range(number_bits):
                    if binary_matrix[x,z] != binary_matrix[y,z]:
                        binary_matrix[x,z] = -1
                        solution_sets[x].add(true_vector[y])
                                  
            difference_count = 0
            
#junta sets que sao dados por outros mais simples
            
difference_count = 0
for x in range(lenght):
    for y in range(x, lenght):
        for z in range(number_bits):
            if binary_matrix[x,z] != -1:
                if binary_matrix[x,z] != binary_matrix[y,z]:
                    difference_count = difference_count +1
        if difference_count == 0:
            solution_sets[x].update(solution_sets[y])
        difference_count = 0

print(binary_matrix)
print(solution_sets)  
solution = []
solved_for = set(())
solution_board = []

#simplifica a solucao booleana removendo duplicados

null_counter = 0
for x in range(number_bits):
    for y in range(lenght):
        for z in range(number_bits):
            if binary_matrix[y,z] == -1:
                null_counter = null_counter + 1
            if null_counter == (number_bits-x-1) and not solution_sets[y].issubset(solved_for):
                solution_temp = tuple((binary_matrix[y]))
                solution_board.append(solution_sets[y])
                solution.append(solution_temp)
                solved_for.update(solution_sets[y])
        null_counter = 0
print(solution_board)
        
redundancy = set(())
redundant = []

#remove soluções duplicadas

for x in range(len(solution)):
    for y in range(len(solution)):
        if x != y:
            redundancy.update(solution_board[y])
    if solved_for == redundancy:
        redundant.append(x)
    redundancy.clear()
print(redundant)

final_solution = solution

for x in range(len(redundant)):
    final_solution.remove(solution[redundant[x]])
    
    
    
print(final_solution)