from re import A


class Node:
    def __init__(self, data):
        self.data = data
        self.goal = None
        self.children = []
        self.cost = []
        self.route = []
        self.accumCost = 0
        self.backPointer = None
    def addChild(self, child, costFloat):
        self.children.append(child)
        self.cost.append(costFloat)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n1.addChild(n2, 2)
n1.addChild(n4,3)
n2.addChild(n5,7)
n2.addChild(n3,5)
n3.addChild(n6,8)
n4.addChild(n5,4)
n4.addChild(n7,6)
n5.addChild(n6,2)
n5.addChild(n8,9)
n6.addChild(n9,10)
n7.addChild(n8,8)
n8.addChild(n9,2)


def depthFirst(node):
        if node:
            if node.goal:
                print(node.data)
                print("Success")
                return False
            print(node.data)
            for x in range(len(node.children)):
                if len(node.children) > 0:
                    if(depthFirst(node.children[x]) == False):
                        return False

def breathFirst(node, q = []):
    if node:
        if node.goal:
            print(node.data)
            print("SUCCESS")
            return False
        print(node.data)
        q.extend(node.children)
        if len(q) > 0:
            breathFirst(q.pop(0))

def djikstraFindRoute(node, goal, oldNode = None, cost = 0):
    if node:
        #print(node.data)
        if node.backPointer == None and oldNode != None:
                node.backPointer = oldNode
                node.accumCost = cost
        elif node.backPointer != None:
            if cost < node.accumCost:
                node.accumCost = cost
                node.backPointer = oldNode
        for x in range(len(node.children)):
            cost = node.accumCost + node.cost[x]
            djikstraFindRoute(node.children[x], goal, node, cost)

def findRoute(node):
    print(node.data)
    if node.data != 1:
        findRoute(node.backPointer)

def djikstra(node, goal):
    djikstraFindRoute(node, goal)
    print("ROUTE: ")
    findRoute(goal)
    print("Cost: ")
    print(goal.accumCost)
    
#depthFirst(n1)
djikstra(n1,n9)

#breathFirst(n1)
