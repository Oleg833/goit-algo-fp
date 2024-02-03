import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_heap_edges(graph, heap, pos, layer=1, index=0, x=0, y=0):
    if index < len(heap):
        node = heap[index]
        graph.add_node(node.id, color=node.color, label=node.val)
        if 2 * index + 1 < len(heap):
            graph.add_edge(node.id, heap[2 * index + 1].id)
            l = x - 1 / 2 ** layer
            pos[heap[2 * index + 1].id] = (l, y - 1)
            add_heap_edges(graph, heap, pos, layer=layer + 1, index=2 * index + 1, x=l, y=y - 1)
        if 2 * index + 2 < len(heap):
            graph.add_edge(node.id, heap[2 * index + 2].id)
            r = x + 1 / 2 ** layer
            pos[heap[2 * index + 2].id] = (r, y - 1)
            add_heap_edges(graph, heap, pos, layer=layer + 1, index=2 * index + 2, x=r, y=y - 1)

def draw_heap(heap):
    heap_graph = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    add_heap_edges(heap_graph, heap, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def main():
    heap = [Node(10), Node(5), Node(6), Node(4), Node(2), Node(3), Node(1)]

    draw_heap(heap)


if __name__ == "__main__":
    main()