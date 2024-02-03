import networkx as nx
import matplotlib.pyplot as plt
import heapq

G = nx.DiGraph()

edges = [
    ("B 1", "B 2", {"weight": 5}),
    ("B 1", "B 3", {"weight": 3}),
    ("B 2", "B 3", {"weight": 2}),
    ("B 2", "B 4", {"weight": 7}),
    ("B 3", "B 4", {"weight": 4}),
    ("B 4", "B 5", {"weight": 6}),
    ("B 5", "B 6", {"weight": 4}),
    ("B 4", "B 7", {"weight": 3}),
    ("B 7", "B 8", {"weight": 5}),
    ("B 6", "B 8", {"weight": 2}),
    ("B 7", "B 9", {"weight": 4}),
    ("B 8", "B 9", {"weight": 6}),
    ("B 9", "B 10", {"weight": 3}),
]

G.add_edges_from(edges)

fixed_positions = {
    "B 1": (0, -1),
    "B 2": (1, 2),
    "B 3": (1, -2),
    "B 4": (2, -1),
    "B 5": (3, 2),
    "B 6": (4, -2),
    "B 7": (4, 1),
    "B 8": (5, 2),
    "B 9": (5, -2),
    "B 10": (6, -1),
}


def visualize_graph(graph, fixed_positions):
    nx.draw(
        graph,
        fixed_positions,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=8,
        font_color="black",
        font_weight="bold",
        edge_color="blue",
        width=2,
        arrowsize=30,
    )
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(
        graph, fixed_positions, edge_labels=labels, font_color="red"
    )
    plt.show()


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph.get_edge_data(current_node, neighbor)["weight"]
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    start_node = "B 1"

    for node, paths in list(dijkstra(G, start_node).items())[1:]:
        print(f"Найкоротший шлях з вершини {start_node} до вершини {node} = {paths}")

    visualize_graph(G, fixed_positions)


if __name__ == "__main__":
    main()
