from Humboldt_Cities import humboldt_cities

def graphDFS(start, end, graph=humboldt_cities):
    print("DFS") 

    stack = [(start, [start], 0)]  # (current_node, path_so_far, cost_so_far)
    explored = set()

    while stack:
        current, path, cost = stack.pop()

        if current == end:
            print("Path:", path)
            print("Cost:", cost)
            print("Explored:", list(explored))
            print("Optimal:", False)  # DFS is not optimal
            return {
                "search_used": "Depth First Search",
                "path": path,
                "cost": cost,
                "explored_nodes": list(explored),
                "is_optimal": False
            }

        if current not in explored:
            explored.add(current)

            for neighbor, edge_cost in reversed(graph.get(current, [])): # it pops the stack in reverse cus i wanted it to search the first branch in our dictionary
                if neighbor not in explored:
                    stack.append((neighbor, path + [neighbor], cost + edge_cost))

    # If no path found
    print("No path found.")
    print("Explored:", list(explored))
    return {
        "search_used": "Depth First Search",
        "path": None,
        "cost": None,
        "explored_nodes": list(explored),
        "is_optimal": False
    }

