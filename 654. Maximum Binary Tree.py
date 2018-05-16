"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root=TreeNode(None)
        self.t=[]
    def add(self,val):
        treenode=TreeNode(val)
        if self.root.val==None:
            self.root=treenode
            self.t.append(self.root)
            return
        else:
            tree_exist_node=self.t[0]
            print(self.t[0].val)
            if tree_exist_node.left==None:
                tree_exist_node.left=treenode
                self.t.append(tree_exist_node.left)
                return
            else:
                tree_exist_node.right=treenode
                self.t.append(tree_exist_node.right)
                self.t.pop(0)

"""
构造思路：init()方法，初始化一棵树，这棵树包含了root根结点和一个t队列，存储树的节点顺序。 
    先判断树是不是为空（即判断根结点是不是为None），如果是，则把现在传入的这个节点treenode当作树的根。 
    如果树不为空，则先读入目前的根节点self.t[0]，如果目前的根结点的左子树为空，则把现在传入的treenode赋上去。 
    如果树不为空，则先读入目前的根节点self.t[0]，如果目前的根结点的左子树不为空，右子树为空，则把现在传入的treenode赋上去。 
    如果一个节点的左右子树都赋过值了，就将它从t中弹出（用pop操作）。一定要弹出左右子树都满了的节点，这样，下一次读入self.t[0]
    的时候才能切换成后面的节点。否则一直都只有三个节点，这个树是构建不起来的。即tree_exist_node=self.t[0]和self.t.pop(0)是
    一对呼应的语句，缺一不可。
"""

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(None)

        def d(root, nums):
            print(nums)
            if not nums:
                return
            i = nums.index(max(nums))
            root.val = nums[i]
            if nums[:i]:
                root.left = TreeNode(None)
                d(root.left, nums[:i])
            if nums[i + 1:]:
                root.right = TreeNode(None)
                d(root.right, nums[i + 1:])

        d(dummy, nums)
        return dummy

    def test(self):
        grid = [3, 0, 8, 4]
        self.constructMaximumBinaryTree(grid)

s = Solution()
s.test()