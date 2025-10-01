## Create Greedy Best-First Search algorithm here

        # remember how the heuristic works
        # consider: dist(A,C) <= dist(A,B) + dist(B,C)
        # therefor: abs(dist(L, goal) - dist(L, current)) is our heuristic
        # accessing these distances is:
        # nodesX, _ = dijktras("Redding", goal)
        # abs(nodesX[goal].d - (nodesX[current]))

# define a landmark
landmark = "Redding"

import heapq

def graphGBFS(start, end, graph=humboldt_cities):
    # Run dijkstra from landmark to goal once
    nodesX, _ = dijkstras(landmark, end)

    queue = []
    heapq.heappush(queue, (0, start, [start], 0))  # (heuristic, node, path, pathCost)
    explored = set()

    # handle bad input here
    # check if end is in cities
    if (end not in graph):
        print("ERROR. destination not found")
        return
    # check if start is in cities
    if (start not in graph):
        print("ERROR. location not found.")
        return

    while queue:
        heur, current, path, pathCost = heapq.heappop(queue)

        if current in explored:
            continue
        explored.add(current)

        # Goal check
        if current == end:
            # Check optimality using Dijkstra
            optimalNodes, _ = dijkstras(start, end)
            optimalCost = optimalNodes[end].d
            isOptimal = (pathCost == optimalCost)

            print("Search: Greedy Best First Search (Landmark Heuristic)")
            print("Path:", " -> ".join(path))
            print("Path Cost:", pathCost)
            print("Explored Nodes:", explored)
            print("Optimal Path Cost:", optimalCost)
            print("Path Optimal?:", "Yes" if isOptimal else "No")
            return path, pathCost

        # Expand neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor not in explored:
                # Landmark heuristic calculation
                nodesY, _ = dijkstras("Redding", neighbor)
                heurValue = abs(nodesX[end].d - nodesY[neighbor].d)
                heapq.heappush(queue, (heurValue, neighbor,
                                          path + [neighbor], pathCost + weight))

    print("No path found")
    return None, float("inf")
