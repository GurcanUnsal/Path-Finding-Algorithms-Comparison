from collections import deque

def get_city_name(city_id, graph):
    return next(node['name'] for node in graph if node['id'] == city_id)

def bfs(graph, start_city, target_city):
    name_to_id = {node['name']: node['id'] for node in graph}
    start_id = name_to_id.get(start_city)
    target_id = name_to_id.get(target_city)

    if start_id is None or target_id is None:
        print("Geçersiz şehir ismi")
        return []

    visited = set()
    queue = deque([(start_id, [start_city])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == target_id:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node - 1]['neighbors']
            for neighbor in neighbors:
                neighbor_id = neighbor['id']
                if neighbor_id not in visited:
                    queue.append((neighbor_id, path + [get_city_name(neighbor_id, graph)]))

    return []


def dfs(graph, start_city, target_city):
    name_to_id = {node['name']: node['id'] for node in graph}
    start_id = name_to_id.get(start_city)
    target_id = name_to_id.get(target_city)

    if start_id is None or target_id is None:
        print("Geçersiz şehir ismi")
        return []

    visited = set()
    stack = [(start_id, [start_city])]

    while stack:
        current_node, path = stack.pop()

        if current_node == target_id:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node - 1]['neighbors']
            for neighbor in neighbors:
                neighbor_id = neighbor['id']
                if neighbor_id not in visited:
                    stack.append((neighbor_id, path + [get_city_name(neighbor_id, graph)]))

    return []