import sys
sys.stdin = open('1231_중위순회.txt', 'r')

class BTNode :
    def __init__(self, elem, left=None, right=None) :
        self.data = elem
        self.left = left
        self.right = right

def inorder(node : BTNode) :
    if node is not None :
        inorder(node.left)
        answer.append(node.data)
        inorder(node.right)

for test_case in range(1, 11) :
    N = int(input())
    tree = [None]
    answer = []
    for _ in range(N) :
        info = input().split()
        tree.append(BTNode(info[1]))
        
    for i in range(1, (N//2)+1) :
        try :
            tree[i].left = tree[2*i]
            tree[i].right = tree[2*i+1]
        except IndexError :
            tree[i].right = None
        
    inorder(tree[1])
    print(f'#{test_case} {"".join(answer)}')