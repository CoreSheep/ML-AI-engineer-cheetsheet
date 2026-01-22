# Futu OA
## 1. a: "xyzxxyzxyz", b: "xyz", return how many times b is in a
```python
def count_b_in_a(a, b):
    # sliding window
    count = 0
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            count += 1
    return count
    # time: O(n * m)
    # space: O(1)
```
    
## 2. Give a complete binary tree, with inorder traversal as a list, return the layer order traversal of the tree
[4, 2, 5, 1, 6, 3, 7] -> [1, 2, 3, 4, 5, 6, 7]
```python
def inorder_to_levelorder(inorder):
    """
    Convert inorder to level order for complete binary tree
    Time: O(n)
    Space: O(n)
    """
    if not inorder:
        return []
    
    n = len(inorder)
    tree = [0] * n  # Array to store level order
    
    def build(arr_idx, start, end):
        """
        arr_idx: where to place in result array
        start, end: range in inorder array
        """
        # Base case: no more elements
        if start > end or arr_idx >= n:
            return
        
        # Find middle element (root of this subtree)
        mid = (start + end) // 2
        
        # Place middle element at arr_idx
        tree[arr_idx] = inorder[mid]
        
        # Build left subtree
        # Left child goes to index: 2*arr_idx + 1
        build(2 * arr_idx + 1, start, mid - 1)
        
        # Build right subtree
        # Right child goes to index: 2*arr_idx + 2
        build(2 * arr_idx + 2, mid + 1, end)
    
    # Start building from root (index 0)
    build(0, 0, n - 1)
    
    return tree
```