class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_bst_from_list(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    for val in nodes[1:]:
        insert_into_bst(root, val)
    return root

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    elif val > root.val:
        root.right = insert_into_bst(root.right, val)
    return root

def lowestCommonAncestor(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root

user_input_bst = input()
bst_nodes = eval(user_input_bst)

p_value = int(input())
q_value = int(input())

bst_root = build_bst_from_list(bst_nodes)

p = TreeNode(p_value)
q = TreeNode(q_value)

lca = lowestCommonAncestor(bst_root, p, q)

print(lca.val if lca else "None")
