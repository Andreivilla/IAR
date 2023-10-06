import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Função para avaliar a qualidade de uma atribuição (minimizar o número de cláusulas insatisfeitas)
def evaluate_assignment(assignment, clauses):
    unsatisfied = 0
    for clause in clauses:
        is_clause_satisfied = False
        for literal in clause:
            variable, is_negated = abs(literal), literal < 0
            if (assignment[variable - 1] and not is_negated) or (not assignment[variable - 1] and is_negated):
                is_clause_satisfied = True
                break
        if not is_clause_satisfied:
            unsatisfied += 1
    return unsatisfied

# Função para gerar uma solução vizinha
def generate_neighbor(assignment):
    neighbor = assignment[:]
    variable_to_flip = random.randint(0, len(neighbor) - 1)
    neighbor[variable_to_flip] = not neighbor[variable_to_flip]
    return neighbor

# Algoritmo Simulated Annealing
def simulated_annealing(clauses, max_iterations, initial_temperature, cooling_rate, max_evaluations):
    num_variables = max(abs(literal) for clause in clauses for literal in clause)
    current_assignment = [random.choice([True, False]) for _ in range(num_variables)]
    current_unsatisfaction = evaluate_assignment(current_assignment, clauses)
    best_assignment = current_assignment[:]
    best_unsatisfaction = current_unsatisfaction

    temperature = initial_temperature
    evaluations = 0

    convergence_data = []  # Para armazenar dados de convergência

    while evaluations < max_evaluations:
        neighbor_assignment = generate_neighbor(current_assignment)
        neighbor_unsatisfaction = evaluate_assignment(neighbor_assignment, clauses)

        delta_unsatisfaction = neighbor_unsatisfaction - current_unsatisfaction

        if delta_unsatisfaction < 0 or random.random() < math.exp(-delta_unsatisfaction / temperature):
            current_assignment = neighbor_assignment
            current_unsatisfaction = neighbor_unsatisfaction

        if current_unsatisfaction < best_unsatisfaction:
            best_assignment = current_assignment[:]
            best_unsatisfaction = current_unsatisfaction

        temperature *= cooling_rate
        evaluations += 1

        # Coleta dados de convergência
        convergence_data.append(best_unsatisfaction)
        print('append')

    return best_assignment, best_unsatisfaction, convergence_data

# Leitura da instância do problema a partir do arquivo "uf20-01.cnf"
with open("uf20-01.cnf", "r") as file:
    lines = file.readlines()

clauses = []
for line in lines:
    if line.startswith("c") or line.startswith("p"):
        continue
    clause = [int(x) for x in line.strip().split()[:-1]]
    clauses.append(clause)

# Configuração do Simulated Annealing
max_iterations = 10000
initial_temperature = 1.0
cooling_rate = 0.99
max_evaluations = 250000  # Limite de avaliações de função

# Execução do Simulated Annealing 10 vezes para coletar dados de convergência
num_runs = 10
results = []

for _ in range(num_runs):
    best_assignment, best_unsatisfaction, convergence_data = simulated_annealing(clauses, max_iterations, initial_temperature, cooling_rate, max_evaluations)
    results.append(best_unsatisfaction)

# Calcular média e desvio-padrão dos resultados
mean_result = np.mean(results)
std_deviation = np.std(results)

# Exibir os resultados
print("Resultados das 10 execuções:", results)
print("Média dos resultados:", mean_result)
print("Desvio-padrão dos resultados:", std_deviation)

# Gerar e exibir gráfico de convergência
plt.plot(convergence_data)
plt.xlabel("Número de Iterações")
plt.ylabel("Melhor Valor de Função Objetivo")
plt.title("Convergência do Simulated Annealing")
plt.show()
