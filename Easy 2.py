class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val,self.left,self.right=val,left,right

def sorted_arr(nums):
    return None if not nums else TreeNode(nums[len(nums)//2],sorted_arr(nums[:len(nums)//2]),sorted_arr(nums[len(nums)//2+1:]))
                            
def print_tree(root):
    if not root:
        return []
    
    left=print_tree(root.left)
    right=print_tree(root.right)

    return [root.val] + left + right if left or right else [root.val]

nums=[int(num) for num in input().split(",")]

output_tree=print_tree(sorted_arr(nums))
print(output_tree)