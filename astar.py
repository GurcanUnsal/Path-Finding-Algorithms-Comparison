import graph as map
import heapq
import time

graph = map.graph
calculate_heuristic = map.calculate_heuristic

def get_city_id_by_name(graph, city_name):
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def a_star_search(graph, start_city, goal_city):
    start_time = time.perf_counter_ns()

    priority_queue = [(0, start_city, [start_city])]
    visited = set()

    while priority_queue:
        current_cost, current_city, path = heapq.heappop(priority_queue)

        if current_city == goal_city:
            end_time = time.perf_counter_ns()
            for city_id in path:
                print(graph[city_id - 1]["name"], end=" -> ")
            print("\nTotal Time:", end_time - start_time, "nano seconds")
            return
        if current_city in visited:
            continue

        print(f'Visiting {graph[current_city - 1]["name"]}')
        visited.add(current_city)

        for neighbor in graph[current_city - 1]["neighbors"]:
            neighbor_id = neighbor["id"]
            new_cost = current_cost + neighbor["distance"]
            heuristic = calculate_heuristic(
                graph[neighbor_id - 1]["lat"],
                graph[neighbor_id - 1]["lon"],
                graph[goal_city - 1]["lat"],
                graph[goal_city - 1]["lon"],
            )
            total_cost = new_cost + heuristic
            print(f'Neighbor: {graph[neighbor_id - 1]["name"]} - Cost: {total_cost}')
            heapq.heappush(
                priority_queue, (total_cost, neighbor_id, path + [neighbor_id])
            )

    end_time = time.time()
    print("No path found!")
    print("Total Time:", end_time - start_time, "nano seconds")

# Example usage:
# Assuming 'cities' is your dictionary array
#start_city_name = input("Enter the current city: ")
#goal_city_name = input("Enter the goal city: ")

## Find city IDs based on city names
#start_city = get_city_id_by_name(graph, start_city_name)
#goal_city = get_city_id_by_name(graph, goal_city_name)

## Run A* algorithm
#a_star_search(graph, start_city, goal_city)