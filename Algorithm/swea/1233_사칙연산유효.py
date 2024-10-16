import sys
from collections import defaultdict
sys.stdin = open('1233_사칙연산유효.txt', 'r')

class BTNode :
    def __init__(self, data, left=None, right=None) :
        self.data = data
        self.left = left
        self.right = right
    
    def isLeaf(self):
        return self.left is None and self.right is None

def isCalcValid(node : BTNode) :
    if node is None :
        return 0
    elif node.isLeaf() :
        if node.data.isdecimal() :
            return 1
        else :
            return 0
    else :
        op1 = isCalcValid(tree[node.left])
        op2 = isCalcValid(tree[node.right])
        return op1 and op2
        

for test_case in range(1, 11) :
    N = int(input())
    tree = defaultdict(BTNode)

    for _ in range(N) :
        info = input().split()
        if len(info) == 4 :
            tree[int(info[0])] = BTNode(info[1], int(info[2]), int(info[3]))
        else :
            tree[int(info[0])] = BTNode(info[1])
    
    print(f'#{test_case} {isCalcValid(tree[1])}')