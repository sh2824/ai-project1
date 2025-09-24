## Lets define the BFS search algorithm
#  input(graph, start node, end node)
#  output "BFS: {path taken}, cost: {cost of path}, explored nodes: {explored nodes}, path optimal? {yes/no}

# LOOPING DETECTED IN THE EXPLORED LIST

def graphBFS (graph, start, end):
    # create a variable to track path cost
    pathCost = 0
    
    # create a queue and put the start node into the queue
    first = (start, pathCost)
    queue = [first]

    # create a list to track explored nodes
    explored = []

    #create a list to track parent nodes
    parent = {start: None}
    
    # while theres stuff in the queue
    while(queue):
        # check if we are at goal
        if (queue[0][0] == end): 
            pathCost = queue[0][1]     # set pathcost for print
            break                      # exit loop
        # check if end is in cities
        if (end not in graph):
            print("ERROR. destination not found")
            break

        # NOTE: queue[x][y]
        # x is the tuple that is in the queue, y=0 is the location name y=1 is Pathcost of said tuple
        
        # find and add adjacent nodes of front node
        if queue[0][0] in graph:
            #print("current node:",queue[0][0])
            for neighbor, cost in graph[queue[0][0]]:       # for each connection in the list to the location at the front of the queue
                #print(neighbor)                                      # TESTING
                if neighbor not in [city for city, _ in explored]:    # if that location has not been explored yet
                    appendable = (neighbor, queue[0][1] + 1)          # create a tuple of the location and path cost
                    queue.append(appendable)                          # add said tuple to queue
                    parent[neighbor] = queue[0][0]                    # track parent
                    #print(neighbor, "not found in explored, added to queue") # testing
                else:
                    # TESTING PURPOSES ONLY
                    porkfriedrice = 4 # ignore this line it only exists to prevent error when disabling the debug print below
                    #print(neighbor, "found in explored, NOT added to queue")
        else:
            print("ERROR. location not found")
            break
        
        # do a check here to see if item is in explored if not then add to explored
        if queue[0][0] not in [city for city, _ in explored]:
            exTuple = (queue[0][0], queue[0][1])
            explored.append(exTuple)    # add the item about to be dequeued to explored list
            #print("added to explored:", exTuple)
        queue.pop(0)                 # this is working as intended by removing the last item from the queue

    # Reconstruct path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    
    # Print results
    print("BFS path:", path)
    print("Path cost:", pathCost)
    print("Explored nodes:", explored)
    print("Path optimal?", "yes" if path else "no")