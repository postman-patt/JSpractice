
# the-quickest-way-up - HackerRank

def quickestWayUp(ladders, snakes):

    from collections import deque

    paths = {}

    for i in ladders + snakes:
        paths[i[0]] = i[1]

    # Initial position and with 0 rolls
    queue = deque([(1, 0)])

    # Set of the visited positions with the MINIMUM number of rolls required for each position visited
    visited = set()


    while len(queue)> 0:

        pos, roll = queue.popleft()


        if pos == 100:
            return roll

        visited.add((pos, roll))

        # Visit every possible position from the current one. Adding 1-6.
        for n in range(1, 7):
            next = pos + n

            # If position has been visited, continue. We can guarantee if the position has been visited, then it would be the shortest path(roll) to that position already (min roll). This due to the nature of BFS, the first time visiting the position would provide the minimum number of rolls requried to get there.
            if (next, roll) in visited or next > 100: continue

            # Add to list of positions to visit
            queue.append((next in paths and paths[next] or next, roll + 1))

    return -1
    
print(
quickestWayUp([[32, 62], [42, 68], [12, 98]], [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]))