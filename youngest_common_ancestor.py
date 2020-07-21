"""Youngest common ancestor
You are given three inputs all of which are instances of an Ancestral tree, class that has
an ancestor property and name property. Write a function that returns the youngest ancestor
of two descendants in the ancestral tree which are given as inputs.
"""

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) time O(1) space, where d is the depth(height) of the ancestral tree

def getYoungestCommonAncestor(top_ancestor, descendant_one, descendant_two):
	depth_one = getDepth(descendant_one, top_ancestor)
	depth_two = getDepth(descendant_two, top_ancestor)
	if depth_one > depth_two:
		return backTrackTree(descendant_one, descendant_two, depth_one-depth_two)
	else:
		return backTrackTree(descendant_two, descendant_one, depth_two-depth_one)


def getDepth(descendant, top):
	count = 0
	while descendant != top:
		count += 1
		descendant = descendant.ancestor
	return count

def backTrackTree(lower_node, higher_node, diff):
	while diff > 0:
		lower_node = lower_node.ancestor
		diff -= 1
	while lower_node != higher_node:
		lower_node = lower_node.ancestor
		higher_node = higher_node.ancestor
	return lower_node


# Another version
# Time O(d) where d is the depth of the ancestral tree and space O(n) where n 
# can be the number of all nodes in the tree if it's skewed
def getYoungestCommonAncestor2(top_ancestor, descendant_one, descendant_two):
    current_node = descendant_one
    hash_map = {}
    while current_node is not None:
        hash_map[current_node.name] = True
		if current_node.ancestor == []:
			current_node = None
		else:
        	current_node = current_node.ancestor
    current_node = descendant_two
    while current_node is not None and current_node.name not in hash_map:
        current_node = current_node.ancestor

    if current_node is not None:
        return current_node
    return top_ancestor