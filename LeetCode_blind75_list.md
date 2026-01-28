## Blind 75 - Complete List
Blind 75 - Complete List
solved: 57/75
The famous list from a Meta engineer, organized by pattern:

### Arrays & Hashing (9) ✅

#### Two Sum ✅
- [Two Sum](https://leetcode.com/problems/two-sum/)  
-solution: hash table (seen)  
- space: O(n) - seen hash table  
- time: O(n) - one pass through the array  

#### Best Time to Buy and Sell Stock ✅  
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
- solution: two pointers (left and right) - left is the minimum price, right is the maximum price  
- space: O(1) - min_price and max_profit  
- time: O(n) - one pass through the array  

#### Contains Duplicate ✅
- [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)  
- solution: hash table (seen) - if the number is already in the hash table, return True  
- space: O(n) - seen hash table  
- time: O(n) - one pass through the array  
- note: use set() instead of hash table for better performance  
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False

# initialize the seen set
seen = set()
seen = {1, 2, 3, 4, 5}
seen = set([1, 2, 3, 4, 5])

# add, remove, check if in set
seen.add(6)
seen.remove(1)
if 2 in seen:
    print("2 is in the set")
else:
    print("2 is not in the set")
```

#### Product of Array Except Self ✅
- [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)  
- solution: prefix and suffix product  
- space: O(n) - answer array  
- time: O(n) - two passes through the array, prefix and suffix product  
- note: use prefix and suffix product to calculate the product of the array except self  
```python
 def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix_prod = 1  # the prefix product of all  previous elements
        for i in range(len(nums)):
            answer[i] *= prefix_prod  # update for each prefix product
            prefix_prod *= nums[i]

        suffix_prod = 1  # the suffix product of all previous element from back to front
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix_prod  # update for each suffix product
            suffix_prod *= nums[i]  # the answer should be prefix product * suffix product
        return answer
```


#### Maximum Subarray ✅
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)  
- solution: Kadane's Algorithm (dynamic programming)  
- space: O(1) - max_sum, current_sum  
- time: O(n) - one pass through the array  
- note: use Kadane's Algorithm to check if the current sum is greater than the current number, if it is, extend the current sum, if it is not, restart the current sum.  
```python
def maxSubArray(self, nums: List[int]) -> int:
    cursum = nums[0]
    maxsum = nums[0]

    for num in nums[1: ]:
        cursum = max(num, num + cursum)  # extend or restart?
        maxsum = max(maxsum, cursum)  # update for the global maxsum
    return maxsum
```

#### Maximum Product Subarray ✅  
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)  
- solution: Kadane's Algorithm (dynamic programming)  
- space: O(1) - max_product, min_product, max_product  
- time: O(n) - one pass through the array  
- note: A little different from the maximum subarray, because we need to consider the negative numbers. (save the min_product and max_product)  
```python
def maxProduct(self, nums: List[int]) -> int:
    cur_min = nums[0]
    cur_max = nums[0]
    max_prod = nums[0]

    for num in nums[1: ]:
        candidates = {num, cur_min * num, cur_max * num}
        cur_min = min(candidates)  # 保存当前的最小值，因为可能后面cur_min * num会成为当前的最大值
        # The reason that we save cur_min is that maybe later
        # the cur_min * num could be the current largest
        cur_max = max(candidates)  # 保存当前的最大值，因为可能后面cur_max * num会成为当前的最小值
        max_prod = max(max_prod, cur_max)  # 更新当前的最大值
    return max_prod
```


#### Find Minimum in Rotated Sorted Array ✅
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  
solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: use binary search to find the minimum number in the rotated sorted array<br>
```python
def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if  nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
        return nums[l]
```

#### Search in Rotated Sorted Array ✅
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
solution: binary search, find the sorted half and check if the target is in the sorted half<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: use binary search to find the target number in the rotated sorted array<br>
```python
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if nums[m] == target:
            return m
        
        # Left half is sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1  # target in left half
            else:
                l = m + 1  # target in right half
        
        # Right half is sorted
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1  # target in right half
            else:
                r = m - 1  # target in left half
    return -1
```

#### 3Sum ✅
- [3Sum](https://leetcode.com/problems/3sum/)  
solution: 
    - sort the array<br>
    - fix one number and use two pointers to find the other two numbers<br>
    - skip the duplicate numbers<br>  
- time: O(n^2)<br>
- note: use two pointers to find the b + c = -a<br>
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining two numbers
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            
            while l < r:
                total = nums[l] + nums[r]
                
                if total == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return result
```

### Two Pointers (3) ✅

#### Summary
1. skip duplicates:
    - 3Sum 

2. move pointers:
    - 3Sum: move the left pointer to the right if the sum is less than the target, move the right pointer to the left if the sum is greater than the target
    - Container With Most Water: move the shorter height to see if there's larger height
    - Valid Palindrome: move the two pointers to the center from both sides

3. ending condition:
    - 3Sum: when the first number is the same as the previous one or the left pointer is greater than the right pointer
    - Container With Most Water: when the left pointer is greater than the right pointer
    - Valid Palindrome: when the left pointer is greater than the right pointer

#### Valid Palindrome ✅
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use two pointers to check if the string is a palindrome from both sides<br>
- note2: use isalnum() to check if the character is alphanumeric, use lower() to convert the character to lowercase, for list comprehension, put if condition after the for loop if you want to filter the characters<br>
```python
def isPalindrome(self, s: str) -> bool:
    # 'a'.isalnum(), 'a'.isalpha(), '4'.isdigit()
    # remove non-alphanumeric characters and convert them to lowercase letters
    s_new = "".join([c for c in s if c.isalnum()]).lower()
    
    # two points
    l, r = 0, len(s_new) - 1
    while l < r:
        if s_new[l] != s_new[r]:
            return False
        l += 1
        r -= 1
    return True
```

#### Container With Most Water ✅
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use two pointers to find the maximum area, pay attention to how to move the pointers<br>
- note2: tricky part is how to move the pointers, move the shorter height to see if there's larger height<br>
```python
def maxArea(self, height: List[int]) -> int:
    max_area = float('-inf')
    i, j = 0, len(height) - 1

    while i < j:
        min_height = min(height[i], height[j])
        width = j - i
        max_area = max(max_area, min_height * width)

        if height[i] > height[j]:  # move the shorter height to see if there's larger height
            j -= 1
        else:
            i += 1
    
    return max_area
```

#### 3Sum (also listed above) ✅🤔
- [3Sum](https://leetcode.com/problems/3sum/)  
- solution: two pointers<br> (need to catch up later)
- space: O(1)<br>
- time: O(n^2)<br>
- note: fix one number and use two pointers to find the other two numbers that sum to -fixed number<br>
- note2: skip the duplicate numbers (skip duplicates for the first number and the left and right pointers if matched)<br>
- summary:
1. sort a list(inplace and non-inplace)<br>
    - inplace: use nums.sort(reverse=False) method<br>
    - non-inplace: use sorted(nums, reverse=False) function<br>
    - sort based on different key: use nums.sort(key=lambda x: x[0]) method<br>

2. sort vs sorted:
    - sort: inplace, modify the original list, return None; use nums.sort(reverse=False) method<br>
    - sorted: non-inplace, create a new list, return the new list; use sorted(nums, reverse=False) function<br>

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found a triplet!
                res.append([nums[i], nums[left], nums[right]])
                
                # ✅ Skip duplicates for left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # ✅ Skip duplicates for right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # ✅ MUST move both pointers!
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1  # ✅ Just move, no need to skip here
                
            else:  # current_sum > target
                right -= 1  # ✅ Just move, no need to skip here
    
    return res
```


### Sliding Window (4) ✅
滑动窗口的核心是在一个数组或者一个子串里找到一个连续的窗口一个区间（子序列，子数组，子字符串等等），这个窗口满足某个条件，然后返回这个窗口的长度或者内容。
The core idea is to use a window to slide through the array, and use two pointers to keep track of the window. Move the right pointer to expand the window, and move the left pointer to shrink the window when a duplicate is found. Stop when the right pointer hits the end of the array.

#### Summary
1. 左指针的移动方式
    - 首先判断移一次还是可以移多次，已多次需要使用while loop来移动左指针，直到不满足条件为止
    - 移动的条件：
        1. 当找到重复字符时，左指针需要移动到，并更新seen set
        2. 当前的窗口需要replace的字符数大于k时，左指针需要移动到，并更新count dict
        3. 只要当前窗口满足条件，就移动左指针，直到不满足条件为止
        4. 下一个潜在的更低的价格即移动的位置
    - 

#### Longest Substring Without Repeating Characters ✅🤔
- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use sliding window to find the longest substring without repeating characters<br>

1. version 1: use set to store the seen letters
- note: use while loop to shrink the left pointer of the window when a duplicate is found until no duplicate is found, and use set to store the seen letters, update the max_len for each right pointer move<br>
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    # sliding window
    # Stop: when r hits the end
    # move l when meeting a repeated letter unless no repeated letters
    # expand right, shrink left when duplicate found
    if len(s) == 0 or len(s) == 1:
        return len(s)

    l, r = 0, 0
    seen = set()
    max_len = 0

    while r < len(s):
        while s[r] in seen:  # found duplicate, then shrink the left pointer of the window until no duplicate is found
            seen.remove(s[l])  # remove the leftmost letter from the window
            l += 1
        seen.add(s[r])  # add the new letter to the window
        r += 1  # move the right pointer to the next position
        max_len = max(max_len, r - l)
    return max_len
```

2. version 2: cleaner version
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    seen = {}
    max_len = 0

    for r in range(len(s)):
        while s[r] in seen:  # found duplicate
            seen.remove(s[l])  # shrink the left point of current window
            l += 1
        seen.add(s[r])  # add new char to the window
        r += 1  # move right pointer
        max_len = max(max_len, r - l)  # update max_len for each right pointer move
    return max_len
```

#### Longest Repeating Character Replacement ✅
- [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)  
- solution: sliding window<br>
- space: O(1) - count hash table<br>
- time: O(n)<br>
- note: 
    - The Key Insight 💡（在当前窗口中，统计最频繁的那个字符的频率，如果需要替换的字符数大于k，则缩小窗口）
    - To make all characters the same in a window, we need to:
        1. Keep the most frequent character (don't replace it!)
        2. Replace all other characters with that frequent one
        3. If we need to replace more than k characters, the window is too big!
    - formula:
        - window_size - max_freq <= k
```python
def characterReplacement(self, s: str, k: int) -> int:
    # sliding window
    # use count to find the max_freq for current window
    # if the num of characters(need to be replaced) > k, shrink the window
    # update the max_len
    count = {}
    l = 0
    max_len = 0
    max_freq = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(count[s[r]], max_freq)

        # window invalid: too many characters to replace
        while (r - l + 1) - max_freq > k:  # shrink the window
            count[s[l]] -= 1
            l += 1
        max_len = max(r - l + 1, max_len)
    return max_len
```

#### Minimum Window Substring ✅🤔
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
- solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
- note: 
    - The Key Insight 💡（通过两个字符统计字典need和window，统计需要的字符和当前窗口中的字符，使用have和required两个变量来判断当前窗口是否满足条件，如果满足条件，则更新结果result和最小长度min_len；然后shrink window，缩小的过程需要更新window和have）
    1. 初始化need和window字典，统计需要的字符和当前窗口中的字符
    2. 使用have和required两个变量来判断当前窗口是否满足条件，如果满足条件，则更新结果result和最小长度min_len
    3. 然后shrink window，缩小的过程需要更新window和have
    4. 返回结果result
    - 难点：
    1. 如何判断当前窗口是否满足条件？(have == required)
    2. 如何更新window和have？(window[left_c] -= 1; if left_c in need and window[left_c] < need[left_c], then have -= 1)

```python
def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    from collections import Counter
    
    need = Counter(t)       # chars we need
    required = len(need)    # unique chars to satisfy
    have = 0                # unique chars satisfied
    
    window = {}
    l = 0
    result = ""
    min_len = float('inf')
    
    for r in range(len(s)):
        # Add right char to window
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        # Check if this char is now satisfied
        if c in need and window[c] == need[c]:
            have += 1
        
        # Shrink window while valid
        while have == required:
            # Update result if smaller
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                result = s[l:r+1]
            
            # Remove left char
            left_c = s[l]
            window[left_c] -= 1  # 移除左边字符，如果打破了平衡，则更新have flag
            if left_c in need and window[left_c] < need[left_c]:
                have -= 1  # have用于判断当前窗口是否满足条件
            l += 1
    
    return result
```


#### Best Time to Buy and Sell Stock (revisited with window) ✅
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
- solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
- note: if you find a smaller buy price, update the buy price, and update the max profit<br>
```python
def maxProfit(self, prices: List[int]) -> int:
    # sliding window
    # expand and shrink
    l = 0
    max_profit = float('-inf')

    for r in range(len(prices)):  # expand the r
        if prices[l] < prices[r]:
            max_profit = max(prices[r] - prices[l], max_profit)
        else:
            l = r  # shrink the l (when you find smaller buy day)
    return max_profit if max_profit != float('-inf') elses 0
```


### Stack (1) ✅

#### Valid Parentheses
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)  
- solution: stack<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use stack to check if the parentheses are valid<br>
```python
    def isValid(self, s: str) -> bool:
        # '(', '{' --> push
        # ')' --> pop to see if they match
        # stop: empty stack
        parentheses_dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        right_parentheses = [')', ']', '}']
        stack = []
        for c in s:
            if c in parentheses_dic:  # '(', '{', '[' --> push
                stack.append(parentheses_dic[c])  # 压入对应的右括号
            elif c in right_parentheses:  # ')', ']', '}' --> pop to see if they match
                if not stack:  # if stack is empty
                    return False
                if stack and stack.pop() != c:  # if top stack element does not match the current parentheses
                    return False
        return not stack  # if there's still element in stack, return False, otherwise return True
```

### Binary Search (2) ✅

#### Find Minimum in Rotated Sorted Array ✅
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  
- solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: 
    1. 这道题需要注意最小值一定在无序的那一半，即当nums[m] > nums[r]时，最小值在右半部分，因为左半部分是有序的，最小值不会在左半部分
    2. 当不在有半部分时，需要更新r = m，因为m可能是最小值，而不是r = m - 1，因为m可能是最小值
    3. 最后返回nums[l]，因为l是最终的候选位置（m也可以，因为最后l和r会相等）

```python
def findMin(self, nums: List[int]) -> int:
    # binary search
    # the minimum is always on the unsorted half
    # update l, r, m

    l, r = 0, len(nums) - 1
    minimum = float('inf')
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:  # go to the right unsorted half to find the minimum
            l = m + 1
        else:
            r = m  # keep m as candidate when jump to the left half
    return nums[l]
```

#### Search in Rotated Sorted Array ✅
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
- solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: 
    1. 这道题难点在于如何判断target在哪一半，然后如何更新左右指针
    2. 只要判断好target在哪一班，search就比较好找了，属于binary search的变形
```python
def search(self, nums: List[int], target: int) -> int:
    # same as find the minimum in rotated sorted array
    # find which half is sorted half, then check if the target is in that half
    # otherwise go check the other half
    l, r = 0, len(nums) - 1

    while l <= r:  # 这里注意终止条件是l <= r，因为target可能等于nums[m]=nums[l]=nums[r]的情况，再比较一次
        m = (l + r) // 2

        if nums[m] == target:
            return m

        # left half is sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:  # 左边有序，且target在左边，则往左边找，更新r = m - 1（不用考虑m=l的情况，因为中间已经比较过）
                r = m - 1
            else:
                l = m + 1

        # right half is sorted
        else:
            if nums[m] < target <= nums[r]:  # 同理
                l = m + 1
            else:
                r = m - 1
    return -1

```


### Linked List (6) ✅

#### Reverse Linked List ✅
- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  
- solution: iterative<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use pre, cur, tmp pointers to reverse the linked list<br>
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pre = None
    cur = head
    while cur:
        tmp = cur.next  # 保存下一个节点，因为cur.next会被覆盖
        cur.next = pre
        pre = cur  # 更新pre指针
        cur = tmp  # 更新cur指针
    return pre
```

#### Merge Two Sorted Lists ✅
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)  
- solution: iterative<br>
- space: O(1)<br>
- time: O(n)<br><br>
- note: 
    1. 使用dummy node创建一个新的链表，两个指针移动通过两个链表，并attach剩余的链表
    2. 在加入新节点时，比较两个链表的当前节点，选择较小的节点加入新链表，然后移动指针到下一个节点
    3. 最后attach剩余的链表（这里不要忘记判断如果list1或list2不空，则直接attach剩余的链表到新链表的末尾）
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # three points + dummy node
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:  # attach the remaining list
        curr.next = list1
    if list2:
        curr.next = list2

    return dummy.next
```


#### Linked List Cycle

#### Reorder List ✅
- [Reorder List](https://leetcode.com/problems/reorder-list/)  
- solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: find the middle of the list and reverse the second half, then merge the two lists<br>
```python
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    1. find the middle
    2. reverse the second half
    3. merge two half
    """
    # 1. find the middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. reverse the second half
    second = slow.next  # start from the second half
    slow.next = None  # cut the first half
    pre = None  # 用于反转链表
    cur = second
    while cur:
        tmp = cur.next  # 保存下一个节点，因为cur.next会被覆盖
        cur.next = pre  # 反转链表
        pre = cur  # 更新pre指针
        cur = tmp  # 更新cur指针
    
    # 3. merge two halves
    first, second = head, pre  # 合并两个链表
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
```
#### Remove Nth Node From End of List
#### Merge K Sorted Lists


### Trees (11) (5/11) ✅

#### Invert Binary Tree ✅
- [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)  
- solution: recursive<br>
- space: O(h) - height of the tree<br>
- time: O(n)<br>
- note: use recursive to invert the binary tree<br>
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left  # 交换左右子树
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

# using stack
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
```

#### Maximum Depth of Binary Tree ✅
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)  
- solution: recursive<br>
- space: O(h) - height of the tree<br>
- time: O(n)<br>
- note: use recursive to find the maximum depth of the binary tree<br>
```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# using iterative   
# level order traversal
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([(root, 1)])
    max_depth = 0
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return max_depth
```

#### Same Tree ✅
- [Same Tree](https://leetcode.com/problems/same-tree/)  
- solution: recursive<br>
- space: O(h) - height of the tree<br>
- time: O(n)<br>
- note: use recursive to check if the two trees are the same<br>
```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

#### Subtree of Another Tree ✅
- [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)  
- solution: recursive<br>
- space: O(h) - height of the tree<br>
- time: O(n)<br>
- note: use recursive to check if the root has the same structure as the subRoot<br>
```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if subRoot and not root:
        return False
    
    def isSame(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return isSame(p.left, q.left) and isSame(p.right, q.right)

    if isSame(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```
#### Lowest Common Ancestor of BST
#### Binary Tree Level Order Traversal
#### Validate Binary Search Tree ✅
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)  
- solution: recursive<br>
- space: O(h) - height of the tree<br>
- time: O(n)<br>
- note: use recursive to check if the node's value is within the range of left and right<br>
```python
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def validate(node, left, right):
        if not node:  # 如果节点为空，则返回True
            return True
        if not (left < node.val < right):  # 然后检查根节点值是否在范围内，如果不在，则返回False
            return False
        return validate(node.left, left, node.val) and validate(node.right, node.val, right)  # 然后递归检查左右子树
    return validate(root, float('-inf'), float('inf'))
```
#### Kth Smallest Element in BST
#### Construct Binary Tree from Preorder and Inorder
#### Binary Tree Maximum Path Sum
#### Serialize and Deserialize Binary Tree


### Tries (3) ✅

#### Implement Trie (Prefix Tree) ✅
- [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)  
- solution: trie<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
1. What is a Trie? (前缀树)
    - A tree where each path from root spells out a word.
2. Key ideas to implement a Trie:
    - Children — map of character → next node (字典)
    - is_end — "Does a word end here?" (是否是一个完整的单词)

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char → TrieNode (字典)
        self.is_end = False  # does a word end here?


class Trie: #(前缀树，字典树)
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # mark end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # must be a complete word!

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # just need to exist, don't check is_end
```

#### Design Add and Search Words Data Structure ✅
- [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)  
- solution: trie<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use trie to implement the add and search words data structure, the search function uses DFS to search the trie (note for the wildcard '.' case, search all the children)<br>
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            # Base case: reached end of word
            if i == len(word):
                return node.is_end
            
            char = word[i]
            
            if char == '.':
                # Wildcard: try ALL children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Normal char: go to specific child
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)
```

#### Word Search II ✅
- [Word Search II](https://leetcode.com/problems/word-search-ii/)  
- solution: trie<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use DFS to search the trie, and use a set to store the result to avoid duplicates<br>
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word here!


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store word at end node
        
        # Step 2: DFS from each cell
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            char = board[r][c]
            
            # Not in Trie path? Stop.
            if char not in node.children:
                return
            
            next_node = node.children[char]
            
            # Found a word!
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates
            
            # Mark visited
            board[r][c] = '#'
            
            # Explore 4 directions
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            # Restore cell
            board[r][c] = char
        
        # Start DFS from every cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return result
```

### Heap / Priority Queue (3) ✅
#### Summary
1. How to use heap/priority queue:
    - import heapq: from heapq import heappush, heappop, heapify
    - heap push: heapq.heappush(heap, (value, index, node)) (if same value, use index to break tie)
    - heap pop: heapq.heappop(heap)
    - heap is a min heap by default
    - heapify: heapq.heapify(heap)
    - A heap is implemented as a complete binary tree. The root is the smallest element.
2. How to create a max heap:
    - use negative values: heapq.heappush(heap, -num)
    - So the top of the heap is the largest element (but we need to convert it back to positive)
    - max_num = -heapq.heappop(heap) or -heap[0]
    - heapq.heappush(heap, -num)

#### Merge K Sorted Lists ✅
- [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)  
- solution: heap/priority queue<br>
- space: O(n)<br>
- time: O(n log k)<br>
- note: 
1. use min heap/priority queue to merge the k sorted lists<br>
2. use index to break tie so the heap can compare the ListNode directly<br>

- 注意点:
1. 如何使用index来break tie？
2. k个链表中有可能有空链表，存头结点时，需要判断是否为空
3. 压入下一个节点时，需要判断是否为空，不为空才压入，不然会报错

```python
import heapq

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Min heap: (value, index, node)
    # index is tiebreaker (can't compare ListNode directly)
    heap = []
    
    # Add all heads to heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))  # index用于两个表中的节点相同时，用来break tie
            # 这里最后传node的原因是后序在pop时，需要知道是哪个链表的节点，所以需要传node.next进入堆heap
    
    dummy = ListNode(0)  # 创建一个虚拟头结点，用于返回结果，最后返回dummy.next
    curr = dummy  # 创建一个当前节点，用于遍历结果链表
    
    while heap:
        val, i, node = heapq.heappop(heap)  # 从堆heap中弹出最小的节点，val是节点值，i是节点索引，node是节点
        
        # Add to result
        curr.next = node
        curr = curr.next
        
        # Push next node from same list
        if node.next:  # 如果节点有下一个节点，则将下一个节点压入堆heap
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

#### Top K Frequent Elements ✅
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)  
- solution: heap/priority queue<br>
- space: O(n)<br>
- time: O(n log k)<br>
- note: use min heap to maintain the top k frequent elements<br>
```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequencies
    count = Counter(nums)
    
    # Step 2: Use min heap of size k
    # heap stores (frequency, number)
    heap = []
    
    for num, freq in count.items():  # 注意不是count.values()
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:  # 动态维护堆的大小，如果堆的大小大于k，则弹出最小的频率，保证最后堆中剩下的都是频率最大的k个元素
            heapq.heappop(heap)  # remove smallest frequency
    
    # Step 3: Extract numbers from heap
    return [num for freq, num in heap]  # 使用list comprehension来提取数字比循环更快
```

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]  # most common返回值是一个列表，里面是(num, freq)元组，like most common k（k=2）: [(1, 3), (2, 2)]
    # 并非一个字典
```

#### Find Median from Data Stream ✅
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)  
- solution: heap/priority queue<br>
- space: O(n)<br>
- time: O(n log n)<br>
- note: 
1. use two heaps small and large to find the median (small is a max heap, large is a min heap), so we can always get the median by the top of the heaps<br>
2. need to maintain the balance of two heaps (add a number to small heap first, then move the max of small to large, then balance the two heaps)<br>
3. if the number of elements is odd, the median is the top of the small heap<br>
4. if the number of elements is even, the median is the average of the top of the small heap and the top of the large heap<br>
```python
class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (use negative values)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: Add to small (max heap, so negate)
        heapq.heappush(self.small, -num)
        
        # Step 2: Move max of small to large
        max_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, max_small)
        
        # Step 3: Balance - large can't be bigger
        if len(self.large) > len(self.small):
            min_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -min_large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # Odd count - small has extra element
            return -self.small[0]
        else:
            # Even count - average of two middles
            return (-self.small[0] + self.large[0]) / 2
```


### Backtracking (2) ✅
#### Summary
#### Template:
1. check if the current state is valid
2. search for the next state
3. backtrack if hit the dead end to the previous state
4. return the result if the current state is valid


#### Combination Sum ✅
- [Combination Sum](https://leetcode.com/problems/combination-sum/)  
- solution: backtracking<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use backtracking to find the combination sum<br>
```python
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtrack(start, path, left):  # start是当前遍历的起点，path是当前的路径，left是当前的剩余目标值
        if left == 0:
            res.append(path.copy())  # use copy to save the real values or path[:]
            return
        if left < 0:
            return

        for i in range(start, len(candidates)):  # use start to avoid duplicates (all choices)
            path.append(candidates[i])
            backtrack(i, path, left - candidates[i])  # pass i instead of i + 1 (unlimited use)
            path.pop()  # backtrack, current path does not work
    
    backtrack(0, [], target)
    
    return res
```

#### Word Search ✅
- [Word Search](https://leetcode.com/problems/word-search/)  
- solution: backtracking<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use DFS to search the word in the board, if the current letter is not the same as the word[i], return False, if the current letter is the same as the word[i], then mask the current letter and search the 4 directions, if found the word, return True, otherwise return False<br>
```python
def exist(self, board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            board[r][c] != word[i] or
            board[r][c] == '#'):
            return False

        temp = board[r][c]
        board[r][c] = '#'  # mask current letter, then go check 4 directions

        found = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1) )

        board[r][c] = temp  # unmask after the search for other choices
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):  # bubble up the result if found the word (only if all the letters are found)
                return True
    
    return False
```

### Graphs (8) ✅
#### Summary
- 1. Graph representation:
    - Adjacency Matrix: a 2D array of size n x n, where n is the number of nodes
    - Adjacency List: a list of lists, where each list contains the neighbors of a node (represented as a list of edges)

```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
```

---

##### Comparison

| | Adjacency Matrix | Adjacency List |
|---|---|---|
| **Space** | O(n²) | O(n + edges) |
| **Check edge exists?** | O(1) ✓ | O(degree) |
| **Get all neighbors** | O(n) | O(degree) ✓ |
| **Add edge** | O(1) | O(1) |
| **Best for** | Dense graphs | Sparse graphs |

---

##### Visual for Donkeys

Adjacency Matrix:
```python
graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
```

**Matrix = Big table, mostly empty:**
```
    0  1  2  3
  ┌────────────
0 │ 0  1  1  0     ← lots of zeros
1 │ 1  0  0  1        if graph is sparse
2 │ 1  0  0  1
3 │ 0  1  1  0
```

**List = Only store what you need:**
```
0 → [1, 2]     ← compact!
1 → [0, 3]
2 → [0, 3]
3 → [1, 2]
```

---

##### When to Use What?

**Use Matrix when:**
- Graph is dense (many edges)
- Need fast "does edge exist?" checks
- n is small

**Use List when:**
- Graph is sparse (few edges)
- Need fast "give me all neighbors"
- n is large

---

##### Real Example: Social Network

1 billion users, average 500 friends each.

**Matrix:** 1B × 1B = 10¹⁸ cells = 💀
**List:** 1B × 500 = 5×10¹¹ = manageable ✓

---

##### TL;DR
```
Matrix = 2D table, good for "is there an edge?"
List   = Each node has neighbor list, good for "who are my neighbors?"
```

2. Graph Algorithms:
    - Breadth-First Search (BFS): a graph traversal algorithm that explores all the nodes at the current depth level before moving on to the nodes at the next depth level.
    - Depth-First Search (DFS): a graph traversal algorithm that explores as far as possible along each branch before backtracking.
    - Dijkstra's Algorithm: a graph traversal algorithm that finds the shortest path between two nodes in a graph.
    - Kruskal's Algorithm: a graph traversal algorithm that finds the minimum spanning tree of a graph.
    - Prim's Algorithm: a graph traversal algorithm that finds the minimum spanning tree of a graph.
    - Bellman-Ford Algorithm: a graph traversal algorithm that finds the shortest path between two nodes in a graph.
    - Floyd-Warshall Algorithm: a graph traversal algorithm that finds the shortest path between all pairs of nodes in a graph.
    

#### Number of Islands ✅
- [Number of Islands](https://leetcode.com/problems/number-of-islands/)  
- solution: depth first search (DFS)<br>
- space: O(m * n)<br>
- time: O(m * n)<br>
- note: 
1. use DFS to find the number of islands<br>    
    - Use recursive to explore all the 4 directions
    - Boundary check: if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'
2. use BFS to find the number of islands<br>
    - Use queue to explore all the 4 directions
    - Boundary check: if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and grid[nr][nc] == '1'
```python
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Out of bounds or water? Stop.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Sink this land (mark visited)
        grid[r][c] = '0'

        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'  # masked the land to water
                    queue.append((nr, nc))  # add current land to queue for next level exploration

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1  # found new island!
                dfs(r, c)  # sink it (set land to water 1 -> 0)
    return count    
```
```python
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Out of bounds or water? Stop.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Sink this land (mark visited)
        grid[r][c] = '0'

        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1  # found new island!
                dfs(r, c)  # sink it (set land to water 1 -> 0)
    return count    
```

#### Clone Graph ✅
- [Clone Graph](https://leetcode.com/problems/clone-graph/)  
- solution: depth first search (DFS)<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
1. use DFS/BFS to clone the graph<br>
    - Use recursive to explore all the neighbors
    - Use a hash table to store the visited nodes (prevent infinite loop)
    - Use a queue to store the nodes to be visited
    - Link the clone to the cloned neighbor
```python
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    
    visited = {}  # 用于map原节点到克隆节点

    def dfs(node):
        if node in visited:
            return visited[node]
        
        clone = Node(node.val)  # 克隆当前节点
        visited[node] = clone  # 将原节点到克隆节点的映射关系存储到visited字典中
        
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))  # 递归克隆邻居节点
        
        return clone  # 返回克隆节点
    
    return dfs(node)

def cloneGraph(self, node: 'Node') -> 'Node':
    # BFS
    if not node:
        return None
    
    visited = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                # Clone neighbor
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            
            # Link clone to cloned neighbor
            visited[curr].neighbors.append(visited[neighbor])
    
    return visited[node]
```

#### Pacific Atlantic Water Flow ✅
- [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)  
- solution: depth first search (DFS)<br>
- space: O(m * n)<br>
- time: O(m * n)<br>
- note: 
1. use DFS to find the nodes that can flow to both the Pacific and Atlantic oceans<br>
    - Use recursive to explore all the 4 directions
    - Boundary check: if r < 0 or r >= rows or c < 0 or c >= cols
    - Boundary check: if (r, c) in visited
    - Boundary check: if heights[r][c] < prev_height
    - Add the current node to the visited set
    - Compute the intersection of the two visited sets (pacific & atlantic)
```python
def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()   # cells that can reach Pacific
    atlantic = set()  # cells that can reach Atlantic
    
    def dfs(r, c, visited, prev_height):
        # Out of bounds?
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        # Already visited?
        if (r, c) in visited:
            return
        # Can't flow uphill from prev? (going backwards!)
        if heights[r][c] < prev_height:
            return
        
        visited.add((r, c))
        
        # Explore all 4 directions
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])
    
    # Start from Pacific edges (top row + left column)
    for c in range(cols):
        dfs(0, c, pacific, 0)        # top row
    for r in range(rows):
        dfs(r, 0, pacific, 0)        # left column
    
    # Start from Atlantic edges (bottom row + right column)
    for c in range(cols):
        dfs(rows - 1, c, atlantic, 0)  # bottom row
    for r in range(rows):
        dfs(r, cols - 1, atlantic, 0)  # right column
    
    # Return intersection
    return [[r, c] for r, c in pacific & atlantic]
```

#### Course Schedule ✅
- [Course Schedule](https://leetcode.com/problems/course-schedule/)  
- solution: depth first search (DFS)<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use three states to mark the nodes: unvisited, visiting, visited
```python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq → course
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses
    
    def hasCycle(node):
        if state[node] == 1:  # visiting → cycle!
            return True
        if state[node] == 2:  # already done
            return False
        
        state[node] = 1  # mark visiting
        
        for neighbor in graph[node]:
            if hasCycle(neighbor):
                return True
        
        state[node] = 2  # mark visited
        return False
    
    # Check all nodes (graph might be disconnected)
    for i in range(numCourses):
        if hasCycle(i):
            return False
    
    return True
```

#### Course Schedule II ✅
- [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)  
- solution: depth first search (DFS)<br>
- space: O(n)<br>
- time: O(n)<br>
- note: Reverse the result to get the correct order<br>
```python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        result = []
        
        def dfs(node):
            if state[node] == 1:  # cycle!
                return False
            if state[node] == 2:  # already done
                return True
            
            state[node] = 1  # visiting
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2  # visited
            result.append(node)  # add AFTER exploring all neighbors
            return True
        
        # Check all nodes
        for i in range(numCourses):
            if not dfs(i):
                return []  # cycle found
        
        return result[::-1]  # reverse!  
```

#### Number of Connected Components (premium)
#### Number of Provinces (replace Number of Connected Components)
- [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)  
- solution: depth first search (DFS)<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use DFS to find the number of provinces<br>
- idea:
```
isConnected = [
  [1,1,0],
  [1,1,0],
  [0,0,1]
]

visited = [F, F, F]

i=0: not visited → new province! count=1
     DFS: visit 0 → visit 1 (connected) → done
     visited = [T, T, F]

i=1: already visited → skip

i=2: not visited → new province! count=2
     DFS: visit 2 → no connections → done
     visited = [T, T, T]

return count = 2 ✓
```

```python
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n
    count = 0
    
    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            count += 1  # found new province!
            dfs(i)      # mark all connected cities
    
    return count
```

#### Graph Valid Tree (premium)
#### Redundant Connection 
- [Redundant Connection](https://leetcode.com/problems/redundant-connection/)  
- solution: depth first search (DFS)<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use DFS to find the redundant connection<br>
```python
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(set)
    
    def hasPath(src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in graph[src]:
            if neighbor not in visited:
                if hasPath(neighbor, dst, visited):
                    return True
        return False
    
    for a, b in edges:
        # Before adding edge, check if path already exists
        if hasPath(a, b, set()):
            return [a, b]
        graph[a].add(b)
        graph[b].add(a)
    
    return []
```

#### Alien Dictionary (premium)


### Dynamic Programming (11) ✅

#### Summary
- 5 steps
1. 确定dp数组（dp table）以及下标的含义 (dp[0] 通常为idle的无意义的，或者为0)
2. 确定递推公式 (通常跟前一个状态有关和cost有关)
3. dp数组如何初始化(最先的一步一般是确定dp[0] ~ dp[2]初始值，根据dp[j]的定义)
4. 确定遍历顺序 (from left to right or from right to left) （爬楼梯是从前往后，背包问题一般从后往前）
5. 举例推导dp数组 (用于debug)

#### Climbing Stairs ✅
- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use dynamic programming to find the number of ways to climb the stairs<br>
```python
def climbStairs(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1  # 0 stairs has 1 way to climb, no stairs to climb
    dp[1] = 1  # 1 stair has 1 way to climb, only 1 step to climb

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```


#### Coin Change ✅
- [Coin Change](https://leetcode.com/problems/coin-change/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
1. 这道题遍历target和coins顺序无所谓，最后如果dp[amount] == float('inf')，则说明无法凑成amount，返回-1
2. 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
3. 如果求排列数就是外层for遍历背包，内层for遍历物品。（即背包顺序有所谓，物品顺序无所谓）
4. 如果求最小数，那么两层for循环的先后顺序就无所谓了，相关题目如下：
    - 322. 零钱兑换
    - 279. 完全平方数
    - 139. 单词拆分
    - 518. 零钱兑换 II
```python
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1) # dp[i]表示凑成金额i所需的最少硬币数
    dp[0] = 0 # 凑成金额0所需的最少硬币数为0

    for i in range(amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):  # check if the subproblem is solvable
                dp[i] = min(dp[i], dp[i - coin] + 1)  # update the minimum number of coins needed to make up the amount

    return dp[amount] if dp[amount] != float('inf') else -1
```

#### Longest Increasing Subsequence ✅
- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i]表示以nums[i]结尾的最长递增子序列的长度<br>
1. 初始化dp数组为1，因为每个元素本身就是一个递增子序列
2. 遍历nums，对于每个元素，遍历之前的所有元素，如果当前元素大于之前的元素，则更新dp[i]
3. 返回dp数组中的最大值
```python
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, i): # check all the previous elements
            if nums[i - 1] > nums[j - 1]: # if the current element is greater than the previous element, then update the dp[i]
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) # return the maximum value of the dp array
```


#### Longest Common Subsequence ✅
- [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i][j]表示text1[0:i]和text2[0:j]的最长公共子序列的长度<br>
1. 初始化dp数组为0，因为空字符串和任何字符串的最长公共子序列都是0 (下标的意义：dp[i][j]表示text1[0:i]和text2[0:j]的最长公共子序列的长度)
2. 遍历text1和text2，对于每个元素，如果当前元素相同，则用对角线上的值+1更新dp[i][j]，否则用左边的值和上边的值中的最大值更新dp[i][j]
3. 返回dp数组中的最大值
```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # dp[i][j]表示text1[0:i]和text2[0:j]的最长公共子序列的长度, 下标从1开始，每次更新dp[i][j]时，需要考虑text1[i-1]和text2[j-1]是否相同

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # YES → Take diagonal + 1, because the current element is the same as the previous element in text1 and text2
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # NO → Take the better neighbor, because the current element is not the same as the previous element in text1 and text2
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    return dp[m][n]
```

#### Word Break ✅
- [Word Break](https://leetcode.com/problems/word-break/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i]表示s[0:i]是否可以被拆分成wordDict中的单词，是否是breakable的<br>
1. 初始化dp数组为False，因为空字符串可以被拆分成空字符串
2. 遍历s，对于每个i之前的元素，如果dp[j]为True且s[j:i]在wordDict中，则dp[i]为True
3. 返回dp数组中的最后一个元素
```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)  # faster lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is breakable
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words: # if the previous substring is breakable and the s[j:i] is in the wordDict, then the current substring is also breakable
                dp[i] = True
                break  # found one valid break, no need to continue
    
    return dp[n]
```

---

##### Visual for Donkeys
```
"leetcode"
 ↑___↑____↑
 0   4    8

dp[0]=T  dp[4]=T  dp[8]=T
         "leet"✓  "code"✓
```

---

##### TL;DR
```
For each position i:
    Look back at all positions j
    If dp[j]=True AND s[j:i] is a word:
        dp[i] = True
```

#### Combination Sum IV ✅
- [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i]表示组成target i的排列数<br>
1. 初始化dp数组为0，因为空target的排列数为0
2. 遍历target，对于每个target，遍历nums，如果加上num可以从上一个dp状态跳到当前状态，则更新dp[i]
3. 返回dp数组中的最后一个元素
```python
def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1  # Number of ways to sum 0: 1 way -- use nothing

    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]  # Sum up all the possible ways
    
    return dp[target]
```
---

##### Visual for Donkeys
```
dp[4] = ?

"How did I get to 4?"

     +1      +2      +3
dp[3] →   dp[2] →   dp[1] →   dp[4]
  4    +    2    +    1    =    7
```

---

##### TL;DR
```
dp[i] = How many ways to reach sum i?
      = dp[i-num1] + dp[i-num2] + dp[i-num3] + ...
```
      
"Add up all the ways I could have arrived here"

#### House Robber ✅
- [House Robber](https://leetcode.com/problems/house-robber/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
    - dp[i]表示偷到第i个房子时能偷到的最大金额<br>
    - 此题有点类似爬楼梯问题，但是不能偷相邻的房子，所以需要用前前一个房子的最大金额加上当前房子的金额更新dp[i]，否则用前一个房子的最大金额更新dp[i]
    - 当前问题与之前的子问题有关，所以是动态规划问题
1. 初始化dp数组为0，因为空房子能偷到的最大金额为0
2. 遍历所有房子nums[i]，如果偷当前房子，则用前前一个房子的最大金额加上当前房子的金额更新dp[i]，否则用前一个房子的最大金额更新dp[i]
3. 返回dp数组中的最后一个元素，即能偷到的最大金额
```python
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * (n + 1)
    dp[1] = nums[0]  # 前1房子里能偷到的最大金额就是第一个房子里的金额
    dp[2] = max(nums[0], nums[1])  # 前2房子里能偷到的最大金额就是第一个房子和第二个房子里的金额中的最大值，因为不能偷相邻的房子

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])  # 如果偷当前房子，则用前前一个房子的最大金额加上当前房子的金额更新dp[i]，否则用前一个房子的最大金额更新dp[i]，因为不能偷相邻的房子，所以只能选择偷前一个房子或者偷前前一个房子加上当前房子的金额

    return dp[n]     
```

#### House Robber II ✅
- [House Robber II](https://leetcode.com/problems/house-robber-ii/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
    - dp[i]表示偷到第i个房子时能偷到的最大金额<br>
    - 此题与House Robber不同的是，房子是环形的，所以需要考虑第一个房子和最后一个房子不能同时偷，所以可以计算nums[1:]和nums[:-1]的dp数组，然后取其中的最大值
##### 🤡 The Trick (Super Simple)
```
Circle means: Can't rob both first AND last house.
So split into two problems:
- Rob houses 0 to n-2 (exclude last)
- Rob houses 1 to n-1 (exclude first)
```
```python
def rob(self, nums: List[int]) -> int:
    def rob_not_adjacent(houses):
        n = len(houses)s
        dp = [0] * (n + 1)
        if n == 1:
            return houses[0]
        dp[1] = houses[0]
        dp[2] = max(houses[0], houses[1])

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i - 1])
        
        return dp[n]
    if len(nums) == 1:
        return nums[0]
    # You can not rob the first and the last houses, so split the hourses
    return max(rob_not_adjacent(nums[:-1]), rob_not_adjacent(nums[1:]))  # trick
```

#### Decode Ways ✅
- [Decode Ways](https://leetcode.com/problems/decode-ways/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i]表示s[0:i]的解码方式数<br>
1. 初始化dp数组为0，因为空字符串的解码方式数为0
2. 遍历s，对于每个i之前的元素子序列，如果子序列可以表示成成功解码一个字符和解码两个字符的和（需要剔除'0'）
3. 返回dp数组中的最后一个元素

```python
 def numDecodings(self, s: str) -> int:
        DIGITS = [str(i) for i in range(1, 27)]  # same as the wordDict in the Word Break problem
        n = len(s)
        dp = [0] * (n + 1) # dp[i]表示s[0:i]的解码方式数
        dp[0] = 1  # empty string has 1 way to decode

        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in DIGITS: # if the current substring s[j:i] is a valid digit, then add the number of ways to decode the previous substring
                    dp[i] += dp[j]
        
        return dp[n]
```

---

##### Visual for Donkeys
```
s = "226"

Position:  _  2  2  6
           0  1  2  3

At each spot:
  "Can I take 1 digit?" → add dp[i-1]
  "Can I take 2 digits?" → add dp[i-2]

dp = [1, 1, 2, 3]
              ↑
           answer
```

---

##### Edge Cases

| Input | Output | Why |
|-------|--------|-----|
| "0" | 0 | '0' alone invalid |
| "06" | 0 | Leading zero |
| "10" | 1 | Only (10) works |
| "27" | 1 | Only (2,7), since 27>26 |

---

##### TL;DR
```
dp[i] = ways to decode s[0..i-1]

At each position:
  If last 1 digit valid (not '0'):
      dp[i] += dp[i-1]
  If last 2 digits valid (10-26, no leading zero):
      dp[i] += dp[i-2]
```

#### Unique Paths (robot grid problem) ✅
- [Unique Paths](https://leetcode.com/problems/unique-paths/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i][j]表示到达(i,j)的所有可能的唯一路径数<br>
1. 初始化dp数组为0，因为起点(0,0)的唯一路径数为1
2. 遍历grid，对于每个当前grid元素，可以从左边或者上边到达，所以dp[i][j] = dp[i-1][j] + dp[i][j-1]
3. 返回dp数组中的最后一个元素
```python
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]

    for i in range(n):  # 初始化第一行，因为只能从左边到达
        dp[0][i] = 1
    
    for i in range(m):  # 初始化第一列，因为只能从上边到达
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 从左边或者上边到达
    
    return dp[m-1][n-1]
```

#### Jump Game ✅
- [Jump Game](https://leetcode.com/problems/jump-game/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: dp[i]表示是否可以从起点到达第i个位置<br>
1. 初始化dp数组为False，第一个位置是可达的（dp[0] = True）
2. 遍历nums，对于每个位置i，如果可达，则更新最远能到达的位置max_reach
3. 每一步都检查当前位置i是否可以到达，如果可以，则更新最远能到达的位置max_reach，否则返回False
4. mark positions只需从max_reach + 1到new_reach + 1和n的相对小值标记即可（即标记[max_reach + 1, min(new_reach + 1, n)]范围内的位置为可达）
```python
def canJump(self, nums: list[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[0] = True  # start position is reachable
    
    max_reach = 0  # furthest index we can reach, to make it faster to check if the current position is reachable
    
    for i in range(n):
        if not dp[i]:  # can't reach this position
            return False

        max_reach = max(max_reach, i + nums[i])
        
        # Mark all positions I can jump to
        for j in range(i, min(max_reach + 1, n)):
            dp[j] = True
        
        if dp[n - 1]:
            return True
    
    return dp[n - 1]
```



### 1-D DP (2 additional problems) ✅

#### Maximum Product Subarray ✅
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)  
- solution: dynamic programming<br>
- space: O(1)<br>
- time: O(n)<br>
- note: 
1. use dynamic programming to find the maximum product subarray<br>

2. define dp:
    - dp_max[i] to store the maximum product of subarray ending at index i<br>
    - dp_min[i] to store the minimum product of subarray ending at index i<br>

3. two dp tables are needed because the minimum negative product can become the maximum positive product later<br>
- formula: dp_max[i] = max(
    nums[i],                    ← start fresh
    dp_max[i-1] * nums[i],      ← extend max
    dp_min[i-1] * nums[i]       ← min × negative = big positive!
)
- formula: dp_min[i] = min(
    nums[i],                    ← start fresh
    dp_max[i-1] * nums[i],      ← extend min
    dp_min[i-1] * nums[i]       ← negative × negative = big positive!
)

4. return the maximum value of dp_max<br>
    - max_prod = max(float('-inf'), dp_max[i])<br>
```python
def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    dp_max = [0] * (n + 1)
    dp_min = [0] * (n + 1)

    dp_max[0] = 1  # dp_max[i] = maximum product of subarray ENDING AT index i-1
    dp_min[0] = 1

    result = float('-inf')

    for i in range(1, n + 1):
        num = nums[i - 1]  # get the current num from nums
        dp_max[i] = max(  # update current max product of nums[i]
            num,  # fresh start
            dp_max[i - 1] * num,
            dp_min[i - 1] * num  # a negative num * dp_min could be a max number
        )

        # same for updating dp_min
        dp_min[i] = min(
            num,
            dp_max[i - 1] * num,
            dp_min[i - 1] * num
        )

        result = max(dp_max[i], result)  # update the result to make sure the global maximum product
    return result
```

#### Partition Equal Subset Sum ✅
- [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 
1. use dynamic programming to find if the subset sum is equal to the target sum<br>
2. dp[j] = max sum we can achieve with capacity j<br>
3. for each item, update the dp array backwards<br> （we can only use each item once）
4. return True if the max sum is equal to the target sum, otherwise return False<br>
```python
def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    
    # Can't split odd sum into two equal parts
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    # dp[j] = max sum we can achieve with capacity j
    dp = [0] * (target + 1)
    
    for num in nums:  # for each item
        for j in range(target, num - 1, -1):  # backwards!
            dp[j] = max(dp[j], dp[j - num] + num)
    
    return dp[target] == target
```

### Intervals (3/5)

#### Insert Interval ✅
- [Insert Interval](https://leetcode.com/problems/insert-interval/)  
- solution: interval manipulation<br>
- space: O(n)<br>
- time: O(n)<br>
- note: three steps to insert the new interval into the intervals:
1. add intervals before overlap<br>
2. handle overlaps<br>
3. add intervals after overlap<br>
```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    i = 0
    n = len(intervals)

    # 1. add intervals before overlap
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    # 2. handle overlaps
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    res.append(newInterval)

    # 3. add intervals after overlap
    while i < n:
        res.append(intervals[i])
        i += 1
    
    return res
```

#### Merge Intervals ✅
- [Merge Intervals](https://leetcode.com/problems/merge-intervals/)  
- solution: interval manipulation<br>
- space: O(n)<br>
- time: O(n)<br>
- note: sort the intervals by start time, then compare each interval with the last one in result, if overlap, merge, if not, add new<br>
```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # The Idea
    # 1. Sort by start time
    # 2. Compare each interval with the last one in result
    # Overlap? Merge. No overlap? Add new.
    intervals.sort(key=lambda x: x[0])  # how to sort based on different key

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        if curr[0] <= last[1]:  # overlap
            last[1] = max(last[1], curr[1])  # extent current last one end
        else:  # no overlap, then add new interval
            res.append(curr)

    return res
```
#### Non-overlapping Intervals ✅
- [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)  
- solution: interval manipulation<br>
- space: O(n)<br>
- time: O(n)<br>
- note: sort the intervals by start time, then compare each interval with the last one in result, if overlap, remove the interval with the larger end, if not, add new, finally return the number of overlaps<br>
```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    overlaps = 0

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        if curr[0] < last[1]:  # overlap exists
            overlaps += 1
            last[1] = min(last[1], curr[1])  # keep the smaller end for the last one
        else:
            res.append(curr)
    
    return overlaps
```

#### Meeting Rooms (premium)
#### Meeting Rooms II (premium)


### Greedy (2) ✅

#### Maximum Subarray ✅
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)  
- solution: dynamic programming<br>
- space: O(1)<br>
- time: O(n)<br>
- note: 
1. greedy贪心贪在哪里呢？
    - 如果 -2 1 在一起，计算起点的时候，一定是从 1 开始计算，因为负数只会拉低总和，这就是贪心贪的地方！
    - 局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。<br>
    - 全局最优：选取最大“连续和”
```python
def maxSubArray(self, nums: List[int]) -> int:
    curSum = 0
    maxSum = float('-inf')

    for num in nums:
        curSum += num
        maxSum = max(maxSum, curSum)
        if curSum < 0:
            curSum = 0

    return maxSum
```

#### Jump Game ✅
- [Jump Game](https://leetcode.com/problems/jump-game/)  
- solution: dynamic programming<br>
- space: O(n)<br>
- time: O(n)<br>
- note: 用贪心算法，每次更新最远能到达的位置cover，如果cover >= n - 1，则返回True，否则返回False<br>
```python
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    cover = 0  # the furtherest we can reach

    for i in range(n):
        if i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= n - 1:  # if we can reach the end
                return True
    return False  
```


### Math & Geometry (3) ✅

#### Rotate Image ✅
- [Rotate Image](https://leetcode.com/problems/rotate-image/)  
- solution: matrix manipulation<br>
- space: O(1)<br>
- time: O(n^2)<br>
- note: 
1. tanspose the matrix, then reverse each row
2. how to transpose a matrix?
    - for i in range(n):
        for j in range(i + 1, n):  # only upper triangle!
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
3. how to reverse a row?
    - row.reverse() (raw is a list)
```python
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):  # only upper triangle!
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
```

#### Spiral Matrix ✅
- [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)  
- solution: matrix manipulation<br>
- space: O(1)<br>
- time: O(n^2)<br>
- note: 
1. 这题难点在于如何控制边界，以及如何避免重复打印，左上 -> 右上后 top + 1，右上 -> 右下后 right - 1，右下 -> 左下后 bottom - 1，左下 -> 左上后 left + 1
2. 如何避免重复打印？
    - 在打印完top row后，top + 1
    - 在打印完right column后，right - 1
    - 在打印完bottom row后，bottom - 1
    - 在打印完left column后，left + 1
3. 这题matrix可能不是方阵，所以需要检查边界是否有效，不然会报错
    - if top <= bottom:
        - 在打印完bottom row后，bottom - 1
    - if left <= right:
        - 在打印完left column后，left + 1
```python
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Go RIGHT along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1  # start from the second number next round
        
        # Go DOWN along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Go LEFT along bottom row (if still valid)
        if top <= bottom:  # we check first, the loop might ends earlier for non-squre matrices [[1, 2, 3, 4]] (in this case we don't need to go left)
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Go UP along left column (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result
```

#### Set Matrix Zeroes ✅
- [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)  
- solution: matrix manipulation<br>
- space: O(1)<br>
- time: O(n^2)<br>
- note: 
1. use two sets to store the rows and columns that need to be zeroed
2. iterate through the matrix to find the zeros and add the rows and columns to the sets
3. iterate through the matrix again to zero out the rows and columns
```python
def setZeroes(self, matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    
    zero_rows = set()
    zero_cols = set()
    
    # Step 1: Find zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    # Step 2: Zero out
    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
```

### Bit Manipulation (5) ✅
#### Bit Manipulation Summary

- important functions:
    - bin(n) -> binary representation of the number (integer to binary string e.g. bin(10) = '0b1010')
    - int(bin_str, 2) -> binary string to integer (e.g. int('0b1010', 2) = 10)
    - bin(n).count('1') -> count the number of 1 bits in the binary representation of the number (e.g. bin(10).count('1') = 2)
    - shift operations: >>= (shift right), <<= (shift left)
    - mask operations: & (AND), | (OR), ^ (XOR), ~ (NOT)
    - mask = 0xFFFFFFFF (32-bit mask)
    - MAX_INT = 0x7FFFFFFF (32-bit max integer)
    - signed = unsigned - 0x100000000 (32bit)

```python
&: AND (同为1，否则为0)
|: OR (有1则为1，否则为0)
^: XOR (a ^ a = 0, a ^ 0 = a) 不同为1，相同为0
~: NOT (取反)
<<: LEFT SHIFT (左移，相当于乘以2)
>>: RIGHT SHIFT (右移，相当于除以2)
>>>: RIGHT SHIFT (无符号右移，相当于除以2)
```
- Example:
```python
10 = 1010
12 = 1100
10 & 12 = 1000 = 8
10 | 12 = 1110 = 14
10 ^ 12 = 0110 = 6
```

#### Number of 1 Bits ✅
- [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)  
- solution: bit manipulation<br>
- space: O(1)<br>
- time: O(1)<br>
- note: use bit manipulation to count the number of 1 bits in the binary representation of the number<br>
```python
def hammingWeight(self, n: int) -> int:
    # using & or bin(num)
    # n = 1 => bin(n) = "0b1011" => count('1')
    return bin(n).count('1')

# using bit manipulation & and >>= (shift right), <<= (shift left)
def hammingWeight(self, n: int) -> int:
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1  # shift right
    return cnt
```

#### Counting Bits ✅
- [Counting Bits](https://leetcode.com/problems/counting-bits/)  
- solution: bit manipulation (bin(i).count('1'))<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use bit manipulation to count the number of 1 bits in the binary representation of the number<br>
```python
def countBits(self, n: int) -> List[int]:
    return [bin(i).count('1') for i in range(n + 1)]
```

#### Reverse Bits ✅
- [Reverse Bits](https://leetcode.com/problems/reverse-bits/)  
- solution: bit manipulation<br>
- space: O(1)<br>
- time: O(1)<br>
- note: use bit manipulation to reverse the bits of the number<br>
```python
def reverseBits(self, n: int) -> int:
    return int(''.join(reversed(bin(n)[2:])), 2)

# using bit manipulation & and >>= (shift right), <<= (shift left)
def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res |= bit << (31 - i)
    return res
```

#### Missing Number ✅
- [Missing Number](https://leetcode.com/problems/missing-number/)  
- solution: bit manipulation (XOR) or math formula<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use bit manipulation XOR to find the missing number<br>
```python
# using math formula
def missingNumber(self, nums: List[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)

# using bit manipulation XOR
# a ^ a = 0, a ^ 0 = a
def missingNumber(self, nums: List[int]) -> int:
    res = len(nums)
    for i in range(len(