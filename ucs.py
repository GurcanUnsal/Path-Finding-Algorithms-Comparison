import heapq
import graph as map

graph = map.graph

# Şehir adıyla bir şehrin id değerini bulur
def get_city_id_by_name(graph, city_name):
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def uniform_cost_search(graph, start_city_name, goal_city_name):
    start_id = get_city_id_by_name(graph, start_city_name)
    goal_id = get_city_id_by_name(graph, goal_city_name)

    if start_id is None or goal_id is None:
        return float('inf'), [], 0

    visited = set()
    heap = [(0, start_id, [start_id])]
    node_count = 0  # Sayaç başlatılır
    while heap:
        (cost, current_id, path) = heapq.heappop(heap) #Minimum maliyetli düğümü çıkar
        if current_id in visited:
            continue
        visited.add(current_id)
        print(f"Şu an {graph[current_id - 1]['name']} şehrindeyiz.")

        if current_id != goal_id:
            print("Komşular ve Mesafeler:")
            visited_neighbors = set(path)  # Keep track of visited neighbors separately
            for neighbor in graph[current_id - 1]['neighbors']:
                neighbor_id = neighbor['id']
                neighbor_name = graph[neighbor_id - 1]['name']
                distance = neighbor['distance']
                print(f"   - {neighbor_name}: {distance} km")
        node_count += 1  # Her adımda bir node'a uğranıldığında sayaç arttırılır
        if current_id == goal_id:
            return cost, path, node_count # Hedef düğüme ulaşıldığında sonuçları döndür
        neighbors = graph[current_id - 1]['neighbors']
        for neighbor in neighbors:
            neighbor_id = neighbor['id']
            if neighbor_id not in visited:
                new_cost = cost + neighbor['distance']
                new_path = path + [neighbor_id]
                heapq.heappush(heap, (new_cost, neighbor_id, new_path)) # Yeni düğümü öncelikli kuyruğa ekle
    return float('inf'), [], 0  # Geçersiz hedef

#while True:
#    print("######################## Şehirler Arası Mesafe Hesaplama - Uniform Cost Search (Çıkış yapmak için 'q' giriniz) #########################")
#    start_city_name = input("Başlangıç Şehri: ")
#    goal_city_name = input("Hedef Şehir: ")
    
#    if start_city_name == "q" or goal_city_name == "q":
#        break

#    start_time = time.perf_counter_ns()
#    distance, path, node_count = uniform_cost_search(graph, start_city_name, goal_city_name)
#    end_time = time.perf_counter_ns()

#    if distance == float('inf'):
#        print(f"Geçersiz Şehir, Tekrar Deneyiniz...")
#    else:
#        print(f"Hesaplanan mesafe: {distance} km.")
#        print(f"Bulunan Yol: {' -> '.join([graph[node - 1]['name'] for node in path])}")
#        print(f"Toplam {node_count} adet şehir(düğüm) ziyaret edildi.")
#        print(f"Toplam Süre: {end_time - start_time} ns.")
