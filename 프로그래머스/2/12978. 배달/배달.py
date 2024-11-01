import heapq
from dataclasses import dataclass

@dataclass
class Node:
    index: int
    distance: int
    
    def __lt__(self, other):
        return self.distance < other.distance

def solution(N, road, K):
    graph = [list() for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append(Node(b, c))
        graph[b].append(Node(a, c))
        
    def dijkstra(start: int):
        d = [float("inf") for _ in range(N + 1)]
        d[start] = 0
        
        queue = []
        heapq.heappush(queue, Node(start, 0))
        
        while queue:
            current_node = heapq.heappop(queue)
            for next_node in graph[current_node.index]:
                new_distance = current_node.distance + next_node.distance
                if d[next_node.index] > new_distance:
                    d[next_node.index] = new_distance
                    heapq.heappush(queue, Node(next_node.index, distance=new_distance))
                    
        return d
    
    d = dijkstra(1)

    return len([x for x in d if x <= K])