import graph as map
import heapq
import time

graph = map.graph   ## graph.py dosyasından gerekli grafı ve fonksiyonu alır
calculate_heuristic = map.calculate_heuristic

def get_city_id_by_name(graph, city_name):      ## adı verilen şehrin id'sini döner
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def get_city_name_by_id(graph, city_id):        ## id'si verilen şehrin adını döner
    for city in graph:
        if city['id'] == city_id:
            return city['name']
    return None

def calculate_total_real_distance(graph, visited):
    total_distance = 0

    for i in range(len(visited) - 1):
        current_city_id = visited[i]
        next_city_id = visited[i + 1]

        current_city = graph[current_city_id - 1]
        next_city_neighbors = current_city["neighbors"]

        for neighbor in next_city_neighbors:
            if neighbor["id"] == next_city_id:
                total_distance += neighbor["distance"]

    return total_distance


def greedy_search(graph, start_city, goal_city):        ## greedy search algoritması
    start_time = time.perf_counter_ns()     ## fonksiyonun ne kadar sürede çalıştığını bulmak için sayaç

    priority_queue = [(0, start_city, [start_city])]    ## şehirlerin eklendiği öncelik listesi
    visited = []     ## ziyaret edilen şehirlerin eklendiği küme
    real_cost = 0
    while priority_queue:
        _, current_city, path = heapq.heappop(priority_queue)   ## öncelik kuyruğundan en küçük öğeyi çıkartır ve bu öğeyi döndürür

        if current_city == goal_city:   ## hedefe ulaşılmışsa
            end_time = time.perf_counter_ns()
            print("Yol bulundu!")
            for city_id in path:
                print(get_city_name_by_id(graph, city_id), end=" -> ")
            print(f"\nToplam Süre: {end_time - start_time} nano saniye")
            start_lat = graph[start_city - 1]["lat"]
            start_lon = graph[start_city - 1]["lon"]
            goal_lat = graph[goal_city - 1]["lat"]
            goal_lon = graph[goal_city - 1]["lon"]
            first_heuristic = calculate_heuristic(start_lat, start_lon, goal_lat, goal_lon)
            print(f"{get_city_name_by_id(graph, start_city)} & {get_city_name_by_id(graph, goal_city)} arası Sezgisel Maaliyet: {first_heuristic:.2f} km")
            real_cost = calculate_total_real_distance(graph, visited)
            print(f"{get_city_name_by_id(graph, start_city)} & {get_city_name_by_id(graph, goal_city)} arası Gerçek Maaliyet: {real_cost:.2f} km")
            return

        if current_city in visited:
            continue

        visited.append(current_city)   ## gidilen şehri visited kümesine ekler

        print(f"{get_city_name_by_id(graph, current_city)} şehrinin komşularının sezgisel maaliyeti kontrol ediliyor:")
        for neighbor in graph[current_city - 1]["neighbors"]:
            neighbor_id = neighbor["id"]
            heuristic = calculate_heuristic(
                graph[neighbor_id - 1]["lat"],
                graph[neighbor_id - 1]["lon"],
                graph[goal_city - 1]["lat"],
                graph[goal_city - 1]["lon"],
            )
            print(f"   {get_city_name_by_id(graph, neighbor_id)}: {heuristic:.2f} km")
            ## öncelik sırasına o an hesaplanan komşu düğümü ekler
            heapq.heappush(
                priority_queue, (heuristic, neighbor_id, path + [neighbor_id])
            )

    end_time = time.perf_counter_ns()
    print("Yol bulunamadı...")
    print(f"Toplam Süre: {end_time - start_time} nano saniye")


# Kullanıcı girişi
#start_city_name = input("Başlangıç şehrini girin: ")
#goal_city_name = input("Hedef şehri girin: ")

## Şehir adına göre id'leri bul
#start_city = get_city_id_by_name(graph, start_city_name)
#goal_city = get_city_id_by_name(graph, goal_city_name)

## Algoritmayı çalıştır
#greedy_search(graph, start_city, goal_city)