import time

from bfs_dfs import bfs, dfs
from graph import graph
from astar import a_star_search
from ucs import uniform_cost_search
from greedy import greedy_search
from dijkstra import dijkstra

def get_city_id_by_name(graph, city_name):      ## adı verilen şehrin id'sini döner
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def main():
    
    start_node = input("Başlangıç şehrini giriniz: ")
    target_node = input("Hedef şehri giriniz: ")
    
    #Rüzgar Tutku Başbay
    # BFS
    print("\n\n########################## Breadth First Search ##########################")
    bfs_start_time = time.perf_counter_ns()
    result_bfs = bfs(graph, start_node, target_node)
    bfs_end_time = time.perf_counter_ns()

    if result_bfs:
        print(f"BFS Yol: {result_bfs}")
        print(f"BFS Zaman: {bfs_end_time - bfs_start_time} ns")
    else:
        print("BFS Yolu bulunamadı.")

    #Rüzgar Tutku Başbay
    # DFS
    print("\n\n########################## Depth First Search ##########################")
    dfs_start_time = time.perf_counter_ns()
    result_dfs = dfs(graph, start_node, target_node)
    dfs_end_time = time.perf_counter_ns()

    if result_dfs:
        print(f"DFS Yol: {result_dfs}")
        print(f"DFS Zaman: {dfs_end_time - dfs_start_time} ns")
    else:
        print("DFS Yol bulunamadı.")

    #Gürcan Ünsal
    # UCS
    print("\n\n########################## Uniform Cost Search ##########################")
    ucs_start_time = time.perf_counter_ns()
    distance, path, node_count = uniform_cost_search(graph, start_node, target_node)
    ucs_end_time = time.perf_counter_ns()


    if distance == float('inf'):
        print(f"Geçersiz Şehir, Tekrar Deneyiniz...")
    else:
        print(f"Hesaplanan mesafe: {distance} km.")
        print(f"Bulunan Yol: {' -> '.join([graph[node - 1]['name'] for node in path])}")
        print(f"Toplam {node_count} adet şehir(düğüm) ziyaret edildi.")
        print(f"Toplam Süre: {ucs_end_time - ucs_start_time} ns.")

    #Yılmaz Can Akdağ
    #Greedy
    print("\n\n########################## Greedy Search ##########################")
    greedy_search(graph, get_city_id_by_name(graph, start_node), get_city_id_by_name(graph, target_node))

    #Emre Ergeldi
    #A*
    print("\n\n########################## A* Search ##########################")
    a_star_search(graph, get_city_id_by_name(graph, start_node), get_city_id_by_name(graph, target_node))

    #Güney Kılıçel
    #Dijkstra
    print("\n\n########################## Dijkstra Search ##########################")
    dijkstra(graph, start_node, target_node)
    

if __name__ == "__main__":
    main()
