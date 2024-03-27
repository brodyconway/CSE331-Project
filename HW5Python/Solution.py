import queue

class Solution:
    def __init__(self, start_node, end_node, graph):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node

    def outputPath(self):
  ################# YOUR CODE GOES HERE ##################
        
        q = queue.PriorityQueue()
        distance = {}
        previous = {}
        q.put((0, self.start_node))
        distance[self.start_node] = 0
        while not q.empty():
            current = q.get()[1]
            if current == self.end_node:
                break
            x = 0
            for i in self.graph[current]:
                if x == 0:
                    x += 1
                    continue
                w = self.graph[i][0]
                dist = distance[current] + w
                if not distance.get(i) and previous.get(current) != i:
                    distance[i] = dist
                    q.put((dist, i))
                    previous[i] = current
                elif dist < distance[i] and previous[current] != i:
                    distance[i] = dist
                    previous[i] = current
                    q.put((dist, i))
        prev = []
        while True:
            if not prev:
                if not previous.get(self.end_node):
                    return []
                prev.append(previous.get(self.end_node))
                if prev[0] == self.start_node:
                    break
                continue
            if not previous.get(prev[0]):
                return []
            prev.insert(0, previous.get(prev[0]))
            if prev[0] == self.start_node:
                break
        prev.append(self.end_node)
        return prev
