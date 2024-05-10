import heapq

# Função para verificar se o estado atual é o objetivo
def is_goal(state):
    return state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Função para gerar os estados vizinhos
def generate_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = idx // 3, idx % 3

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

# Função de heurística (distância de Manhattan)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# Algoritmo de busca A*
def solve_puzzle(start_state):
    visited = set()
    heap = [(heuristic(start_state), 0, start_state)]
    heapq.heapify(heap)

    while heap:
        _, moves, state = heapq.heappop(heap)

        if is_goal(state):
            return moves, state

        visited.add(state)
        for neighbor in generate_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(heap, (moves + heuristic(neighbor), moves + 1, neighbor))

    return None, None

# Estado inicial do quebra-cabeça (0 representa o espaço vazio)
initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
initial_state = (1, 3, 5, 4, 2, 6, 7, 8, 0)

# Resolvendo o quebra-cabeça
num_moves, solution = solve_puzzle(initial_state)

# Exibindo a solução
if solution:
    print("Solução encontrada em", num_moves, "movimentos:")
    for i in range(0, 9, 3):
        print(solution[i:i+3])
else:
    print("Não há solução.")
