# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        currentNode = self
        array.append(currentNode.name)
        length = len(currentNode.children)
        if length > 0:
            for i in range(length):
                self.children[i].depthFirstSearch(array)
        return array
        
    # O(v + e) time | O(v) space
    def dfs_pythonic(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

print(graph.depthFirstSearch([]))