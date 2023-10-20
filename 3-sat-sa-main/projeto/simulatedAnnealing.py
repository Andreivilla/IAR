import random
import matplotlib.pyplot as plt

class SimulatedAannealing:
    def __init__(self, file, num_it):
        self.matrix = []
        self.max_range = 100
        #parametros
        self.file = file
        self.num_it = num_it
        #calculos
        self.matrix, self.num_var, self.num_rows = self.read_cnf()
        self.initial_solution = self.initial_random_solution()
        self.var_dict = self.map_solution()
        #resultados

            
    def run(self):
        results_sa = []
        results_rs = []

        for i in range(2):
            #result_sa = self.simulated_annealing(
            #    self.initial_solution, self.var_dict, self.matrix, self.num_it, 4, self.num_var, self.num_rows, self.max_range)
            result_sa = self.simulated_annealing()
            results_sa.append(result_sa)

            result_rs = self.random_search(initial_solution, num_it,
                                    self.var_dict, self.matrix, self.num_rows, self.max_range)
            results_rs.append(result_rs)

            log_filename = f"results/result_{file_name}.txt"

            # Abre o arquivo de log e escreve os resultados
            with open(log_filename, "w") as f:
                f.write("Simulated Annealing: \n")
                for result in results_sa:
                    f.write(f"{result}\n")

                f.write("Random Search: \n")
                for result in results_rs:
                    f.write(f"{result}\n")
        
        
    def read_cnf(self):
        with open(self.file, "r") as f:
            for i, line in enumerate(f):
                if i == 7:
                    num_var = int(line.split()[2])
                    num_rows = int(line.split()[3])
                    matrix = [[] for _ in range(num_rows)]
                elif i >= 8:
                    variables = line.split()
                    if len(variables) == 4:
                        matrix[i-8] = [int(v) for v in variables]
        return matrix, num_var, num_rows

    def initial_random_solution(self):
        initial_solution = []
        for i in range(self.num_var):
            initial_solution.append(random.choice([0, 1]))
        return initial_solution

    def map_solution(self):
        map = {}
        for i in range(self.num_var):
            var_name = 'v{}'.format(i+1)
            map[var_name] = self.initial_solution[i]
        return map

    def evaluate_solution(solution, var_dict, matrix):
        # Inicializa o número de cláusulas não satisfeitas
        num_clausulas_nao_satisfeitas = 0

        # Percorre todas as cláusulas da matriz
        for clausula in matrix:
            # Verifica se pelo menos uma das três variáveis da cláusula é satisfeita
            if (solution[var_dict[f"v{abs(clausula[0])}"]] == 1 and clausula[0] > 0) or (solution[var_dict[f"v{abs(clausula[0])}"]] == 0 and clausula[0] < 0):
                continue
            elif (solution[var_dict[f"v{abs(clausula[1])}"]] == 1 and clausula[1] > 0) or (solution[var_dict[f"v{abs(clausula[1])}"]] == 0 and clausula[1] < 0):
                continue
            elif (solution[var_dict[f"v{abs(clausula[2])}"]] == 1 and clausula[2] > 0) or (solution[var_dict[f"v{abs(clausula[2])}"]] == 0 and clausula[2] < 0):
                continue
            # Se nenhuma variável satisfaz a cláusula, incrementa o contador de cláusulas não satisfeitas
            num_clausulas_nao_satisfeitas += 1

        # Retorna o número de cláusulas não satisfeitas
        return num_clausulas_nao_satisfeitas

    def generate_neighbor(solution, num_var):
        # Calcula o número de variáveis a serem invertidas
        num_var_invertidas = max(1, int(num_var / 4))

        # Seleciona aleatoriamente um subconjunto de variáveis a serem invertidas
        indices_var_invertidas = random.sample(range(num_var), num_var_invertidas)

        # Cria uma cópia da solução inicial para ser modificada
        neighbor = solution.copy()

        # Inverte os valores das variáveis selecionadas
        for indice in indices_var_invertidas:
            neighbor[indice] = 1 - neighbor[indice]

        return neighbor

    def random_search(initial_solution, max_iter, var_dict, matrix, num_rows, max_range):
        current_solution = initial_solution
        current_score = self.evaluate_solution(current_solution, var_dict, matrix)
        best_solution = current_solution.copy()
        best_score = num_rows - current_score
        scores = [best_score]
        iter = []
        rangeScore = 0

        for it in range(max_iter):
            # Gerar uma nova solução aleatória
            new_solution = self.initial_random_solution(len(current_solution))
            new_score = self.evaluate_solution(new_solution, var_dict, matrix)

            # Atualizar a solução atual caso a nova solução seja melhor
            if new_score > current_score:
                current_solution = new_solution
                current_score = new_score

            # Atualizar a melhor solução encontrada
            if current_score > best_score:
                best_solution = current_solution.copy()
                best_score = current_score

            # Define um range de plot para melhorar a visualização do gráfico
            rangeScore = rangeScore + 1
            if (rangeScore == max_range):
                rangeScore = 0
                scores.append(num_rows - new_score)
                iter.append(it)

        # Plotar o gráfico
        plt.ylim(0, num_rows)
        plt.plot(range(0, len(iter)+1), scores)
        plt.xlabel('Número de Iterações (Núm. Iterações/Range)')
        plt.ylabel('Número de Cláusulas Satisfeitas')
        # plt.show()
        plt.savefig('rs.png')
        plt.close()

        map_b_solution = self.map_solution(len(current_solution), best_solution)
        return map_b_solution, best_score

    def simulated_annealing(self):#initial_solution, var_dict, matrix, max_iter, t, num_var, num_rows, max_range):
        current_solution = self.initial_solution
        current_score = self.evaluate_solution(current_solution, var_dict, matrix)
        best_solution = current_solution.copy()
        best_score = self.num_rows - self.current_score

        rangeScore = 0
        scores = [best_score]  # lista para armazenar os scores a cada iteração
        temp = []
        iter = []

        for it in range(max_iter):
            temperature = (1 - (it/max_iter)) ** t

            # Gerar vizinho aleatório
            neighbor = self.generate_neighbor(current_solution, num_var)
            n_dict = self.map_solution(num_var, neighbor)

            # Avaliar o vizinho
            neighbor_score = self.num_rows - self.evaluate_solution(neighbor, n_dict, matrix)

            # Aceitar o vizinho com uma determinada probabilidade
            delta_score = neighbor_score - current_score

            if delta_score > 0 or random.uniform(0, 1) < temperature:
                current_solution = neighbor
                current_score = neighbor_score

            # Atualizar a melhor solução encontrada
            if current_score > best_score:
                best_solution = current_solution.copy()
                best_score = current_score

            map_b_solution = self.map_solution(num_var, best_solution)

            # Define um range de plot para melhorar a visualização do gráfico
            rangeScore = rangeScore + 1
            if (rangeScore == max_range):
                rangeScore = 0
                scores.append(current_score)
                temp.append(temperature)
                iter.append(it)

                print(temperature)

        # Plotar o gráfico
        # plt.ylim(0, num_rows)
        plt.plot(range(0, len(iter)+1), scores)
        plt.xlabel('Número de Iterações (Núm. Iterações/Range)')
        plt.ylabel('Número de Cláusulas Satisfeitas')
        plt.savefig('convergencia.png')
        plt.close()

        plt.plot(iter, temp)
        plt.xlabel('Número de Iterações')
        plt.ylabel('Temperatura')
        plt.savefig('temperatura.png')
        plt.close()

        return map_b_solution