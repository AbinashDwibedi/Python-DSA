# Maximum Product of Splitted Binary Tree

def maxProduct(self, root: Optional[TreeNode]) -> int:
        diffSums = []
        maxi = 0
        def dfs(root):
            if not root:
                return 0
            summ = root.val + dfs(root.right) + dfs(root.left)
            diffSums.append(summ)
            return summ
        maxSum = dfs(root)
        for num in diffSums:
            maxi = max(maxi,(maxSum-num)*num)
        return maxi % (10**9 + 7)