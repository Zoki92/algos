from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) != 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

print(graph.breadthFirstSearch([]))

"""
Complexity explanation:
Throughout the execution of the algorithm we get to store every Node inside
curent atleast once. That's O(v). On top of that for every Vertex we go 
and iterate it's children, which is actually the number of edges, hence
O(e) in the nested for loop. Added all together we get O(v + e). Space will be
O(v) because we only store nodes, and that's worst scenario.

"""