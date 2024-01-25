import heapq
import time
import matplotlib.pyplot as plt
#from turkiye import graph

def get_city_id_by_name(graph, city_name):
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def get_city_name_by_id(graph, city_id):
    for city in graph:
        if city['id'] == city_id:
            return city['name']
    return None

def plot_path(graph, path):
    # Visualise
    x, y = [], []
    for i in path:
        x.append(graph[i - 1]["lon"])
        y.append(graph[i - 1]["lat"])
        plt.text(graph[i - 1]["lon"], graph[i - 1]["lat"], get_city_name_by_id(graph, i))

    x.append(x[0])
    y.append(y[0])
    plt.title("Dijkstra Algorithm")
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()
    plt.draw()

def dijkstra(graph, start, goal):
    start_time = time.perf_counter_ns()

    start_city_id = get_city_id_by_name(graph, start)
    goal_city_id = get_city_id_by_name(graph, goal)

    if start_city_id is None or goal_city_id is None:
        print("Geçersiz şehir adı. Lütfen doğru şehir adları girin.")
        return

    priority_queue = [(0, start_city_id, [start_city_id])]
    visited = set()

    while priority_queue:
        current_cost, current_city, path = heapq.heappop(priority_queue)

        if current_city == goal_city_id:
            end_time = time.perf_counter_ns()
            print("Başlangıç Şehiri:", get_city_name_by_id(graph, start_city_id))
            print("Hedef Şehiri:", get_city_name_by_id(graph, goal_city_id))
            for city_id in path:
                city_name = get_city_name_by_id(graph, city_id)
                if city_name:
                    print(f"Şu an {city_name} şehrindeyiz.")
                    print("Komşular ve Mesafeler:")
                    for neighbor in graph[city_id - 1]["neighbors"]:
                        neighbor_id = neighbor["id"]
                        neighbor_name = get_city_name_by_id(graph, neighbor_id)
                        print(f"- {neighbor_name}: {neighbor['distance']:.15f} km")
                    print()
            print(f"saplanan mesafe: {current_cost:.15f} km.")
            print(f"Bulunan Yol: {' - » '.join([get_city_name_by_id(graph, city_id) for city_id in path if get_city_name_by_id(graph, city_id)])}")
            print(f"Toplam {len(path)} adet şehir(düğüm) ziyaret edildi.")
            print(f"Toplam Süre: {end_time - start_time} ns.")

            # Çözüm yolunu görselleştir
            plot_path(graph, path)

            return
        if current_city in visited:
            continue

        visited.add(current_city)

        for neighbor in graph[current_city - 1]["neighbors"]:
            neighbor_id = neighbor["id"]
            new_cost = current_cost + neighbor["distance"]

            # Öncelik kuyruğunu güncelle: En küçük maliyetli yolu seç
            heapq.heappush(
                priority_queue, (new_cost, neighbor_id, path + [neighbor_id])
            )

    end_time = time.perf_counter_ns()
    print("No path found!")
    print(f"Toplam Süre: {end_time - start_time} ns.")

# Example usage:
#start_city_name = input("Enter the current city: ")
#goal_city_name = input("Enter the goal city: ")

#dijkstra(graph, start_city_name, goal_city_name)
