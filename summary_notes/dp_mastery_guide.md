# Dynamic Programming Mastery Guide

## The Universal 5-Step Framework

Every DP problem follows this structure:

1. **Define dp[i] meaning** - What does this index represent?
2. **Find the recurrence relation** - How does dp[i] relate to previous states?
3. **Initialize base cases** - What are dp[0], dp[1], etc.?
4. **Determine iteration order** - Left-to-right or right-to-left?
5. **Trace an example** - Debug with a small test case

---

## Problem Classification and Patterns

### Pattern 1: 1D Linear DP (Single Array)

**When to use:** Current state depends only on previous positions in a single sequence

**Structure:**
```python
dp = [base_value] * (n + 1)
dp[0] = initial_condition

for i in range(1, n + 1):
    dp[i] = f(dp[i-1], dp[i-2], ..., current_element)
```

**Examples:**

| Problem | dp[i] Meaning | Recurrence | Key Trick |
|---------|---------------|------------|-----------|
| Climbing Stairs | Ways to reach step i | dp[i] = dp[i-1] + dp[i-2] | Pure Fibonacci |
| House Robber | Max money up to house i | dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]) | Cannot rob adjacent |
| Decode Ways | Ways to decode s[0:i] | dp[i] = dp[i-1] + dp[i-2] (if valid) | Check 1-digit and 2-digit |
| Jump Game | Can reach position i? | dp[i] = True if reachable from any j < i | Track max_reach for optimization |

**Common Tricks:**
- Always check dp[i-1] (one step back) and dp[i-2] (two steps back)
- Use max() for optimization problems (House Robber)
- Use sum() or += for counting problems (Climbing Stairs, Decode Ways)

---

### Pattern 2: Knapsack / Unbounded Resource Problems

**When to use:** You have items/coins and need to fill a target/amount

**Structure:**
```python
dp = [base_value] * (target + 1)
dp[0] = initial_condition

for i in range(target + 1):  # outer loop: target
    for item in items:       # inner loop: items
        if can_use_item:
            dp[i] = update_function(dp[i], dp[i - item])
```

**Examples:**

| Problem | dp[i] Meaning | Update Rule | Notes |
|---------|---------------|-------------|-------|
| Coin Change | Min coins for amount i | dp[i] = min(dp[i], dp[i-coin] + 1) | Use float('inf') for impossible |
| Combination Sum IV | Number of ways to sum to i | dp[i] += dp[i-num] | Order matters (permutations) |
| Word Break | Can break s[0:i]? | dp[i] = True if dp[j] and s[j:i] in words | Check all split points j |

**Critical Distinctions:**

```
COMBINATIONS (order does not matter):
    for item in items:
        for i in range(target):
            ...

PERMUTATIONS (order matters):
    for i in range(target):
        for item in items:
            ...

MINIMUM/MAXIMUM (order does not matter):
    Either order works (Coin Change)
```

**Tricks:**
- Always check dp[i - item] != float('inf') before using it
- For "word break" style: iterate through all possible split points j < i
- Initialize dp[0] = 1 for counting, dp[0] = 0 for min/max

---

### Pattern 3: Subsequence DP (Compare/Match Elements)

**When to use:** Finding longest/best subsequence with constraints

**Structure:**
```python
dp = [1] * n  # Each element is a subsequence of length 1

for i in range(n):
    for j in range(i):  # Look back at ALL previous elements
        if condition(nums[j], nums[i]):
            dp[i] = max(dp[i], dp[j] + 1)
```

**Examples:**

| Problem | dp[i] Meaning | Condition | Return Value |
|---------|---------------|-----------|--------------|
| Longest Increasing Subsequence | LIS ending at i | nums[j] < nums[i] | max(dp) |
| Longest Common Subsequence | LCS of text1[0:i], text2[0:j] | text1[i-1] == text2[j-1] | dp[m][n] |

**Key Insight:**
```
dp[i] = length of best subsequence ENDING AT position i

This is different from:
dp[i] = best answer considering first i elements
```

**Tricks:**
- Initialize all dp[i] = 1 (each element alone is valid)
- Must check ALL previous positions j < i
- Return max(dp), not dp[n]
- For 2D LCS: dp[i][j] uses i-1 and j-1 indexing

---

### Pattern 4: 2D Grid DP

**When to use:** Robot movement, grid paths, or 2D state problems

**Structure:**
```python
dp = [[0] * n for _ in range(m)]

# Initialize borders
for i in range(m): dp[i][0] = ...
for j in range(n): dp[0][j] = ...

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]  # or other combination
```

**Examples:**

| Problem | dp[i][j] Meaning | Recurrence | Border Init |
|---------|------------------|------------|-------------|
| Unique Paths | Number of paths to (i,j) | dp[i-1][j] + dp[i][j-1] | First row/col = 1 |
| Longest Common Subsequence | LCS of text1[0:i], text2[0:j] | Match: dp[i-1][j-1] + 1<br>No match: max(dp[i-1][j], dp[i][j-1]) | First row/col = 0 |

**Tricks:**
- Robot can only move right or down: dp[i][j] = dp[i-1][j] + dp[i][j-1]
- LCS match: take diagonal + 1
- LCS no match: take max of neighbors

---

## Mental Models and Tricks

### 1. The "How Did I Get Here?" Principle

For every dp[i], ask: **"What are ALL the ways I could have arrived at state i?"**

```
Climbing Stairs:  "I came from step i-1 or i-2"
Coin Change:      "I used coin c and came from state i-c"
LIS:              "I extended the best subsequence ending before me"
```

### 2. Initialization Patterns

| Meaning of dp[0] | Use Case | Example |
|------------------|----------|---------|
| dp[0] = 0 | Empty/idle state is 0 | Coin Change (0 coins for amount 0) |
| dp[0] = 1 | Empty state is valid | Climbing Stairs (1 way to stay at ground) |
| dp[0] = True | Empty state is reachable | Word Break (empty string is breakable) |
| dp[0] = float('inf') | Impossible state | Coin Change (all amounts start impossible) |

### 3. Index Gymnastics Cheat Sheet

```python
# When dp is size (n+1) and nums is size n:
for i in range(1, n + 1):
    dp[i] relates to nums[i-1]

# When dp is size n and nums is size n:
for i in range(n):
    dp[i] relates to nums[i]

# For 2D LCS problems:
dp[i][j] compares text1[i-1] with text2[j-1]
```

**Pro Tip:** Drawing a small table helps visualize the indices.

### 4. Common Optimization Tricks

**Space Optimization:**
```python
# If dp[i] only depends on dp[i-1] and dp[i-2]:
# Replace dp array with two variables
prev2, prev1 = dp[0], dp[1]
for i in range(2, n):
    curr = prev1 + prev2
    prev2, prev1 = prev1, curr
```

**Early Exit:**
```python
# For boolean problems (Word Break, Jump Game):
if dp[target]:
    return True  # Do not continue if already found
```

**Greedy Alternative:**
```python
# Some DP problems have O(n) greedy solutions:
# Jump Game: Track max_reach
# House Robber: Use prev1, prev2 variables
```

---

## Problem-Specific Hacks

### House Robber Series

```python
# House Robber I: Linear houses
dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

# House Robber II: Circular houses (first and last connected)
# Trick: Run the algorithm TWICE
return max(rob(nums[:-1]), rob(nums[1:]))
# Exclude last house OR exclude first house
```

### Coin Change vs Combination Sum IV

```python
# Coin Change (order does not matter):
for i in range(amount + 1):
    for coin in coins:
        ...

# Combination Sum IV (order matters - permutations):
for i in range(target + 1):
    for num in nums:
        dp[i] += dp[i - num]
```

### Word Break Pattern

```python
# The "split point" technique:
for i in range(1, n + 1):
    for j in range(i):  # Try ALL possible splits
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break  # Early exit for boolean
```

### Decode Ways Edge Cases

```python
# Watch out for:
- Leading zeros: "06" is invalid
- Single '0': "0" is invalid
- Valid two-digit: 10-26 only
- "27": Only (2, 7) works since 27 > 26
```

### Jump Game Optimization

```python
# Instead of marking every position:
max_reach = 0
for i in range(n):
    if i > max_reach:
        return False
    max_reach = max(max_reach, i + nums[i])
    if max_reach >= n - 1:
        return True
```

---

## The DP Decision Tree

```
Is this a DP problem?
- Optimal substructure?
- Overlapping subproblems?
    |
    v
What type of DP?
    |
    |-- 1D Linear?
    |     Single array, dp[i-1], dp[i-2]
    |
    |-- Knapsack?
    |     Target/amount with items
    |
    |-- Subsequence?
    |     Compare elements, nested loop
    |
    |-- 2D Grid?
          Robot paths, LCS
    |
    v
Apply the 5-step framework
```

---

## Debugging Checklist

When your DP solution does not work:

- [ ] Did you initialize dp[0] correctly?
- [ ] Are you using i-1 when dp is size n+1?
- [ ] For knapsack: Is i - item >= 0?
- [ ] For subsequence: Are you checking j < i?
- [ ] Did you return max(dp) instead of dp[n]?
- [ ] For minimization: Did you check for float('inf')?
- [ ] For 2D: Did you initialize borders?
- [ ] Trace a small example by hand

---

## Quick Reference Table

| Problem Type | Time | Space | Key Trick |
|--------------|------|-------|-----------|
| Fibonacci-like | O(n) | O(n) to O(1) | Two variables |
| Knapsack | O(n × m) | O(n) | Item order matters for permutations |
| Subsequence | O(n²) | O(n) | Nested loop, check all j < i |
| 2D Grid | O(m × n) | O(m × n) | Initialize borders first |

---

## Study Strategy

1. Master the 1D patterns first (Climbing Stairs, House Robber)
2. Understand knapsack variations (Coin Change, Word Break)
3. Practice subsequence problems (LIS, LCS)
4. Tackle 2D grids last (Unique Paths, Edit Distance)

**Remember:** DP is about breaking down problems into smaller subproblems and building up solutions. If you can define what dp[i] means and how it relates to previous states, you have solved 80% of the problem.

---

## Final Pro Tips

1. Always draw the dp table for the first few values
2. Start with brute force recursion, then memoize, then bottom-up
3. Check if greedy works first (some DP problems have O(n) solutions)
4. Write down the recurrence relation before coding
5. Test with edge cases: empty input, size 1, size 2

---

## Common Mistakes to Avoid

**Index Out of Bounds:**
- Always verify i-1, i-2 are valid before accessing
- For 2D problems, check both i-1 and j-1

**Wrong Return Value:**
- Subsequence problems: return max(dp), not dp[n]
- Grid problems: return dp[m-1][n-1] or dp[m][n] depending on indexing

**Initialization Errors:**
- Coin Change: Start with float('inf'), not 0
- Counting problems: Start with 0, except dp[0] = 1
- Boolean problems: Start with False, except dp[0] = True

**Loop Order Confusion:**
- Combinations: items outer, target inner
- Permutations: target outer, items inner
- Always double-check which order your problem needs

---

## Summary

Dynamic Programming problems share common patterns that can be recognized and applied systematically. The key is to:

1. Identify the pattern (1D, Knapsack, Subsequence, 2D Grid)
2. Define what dp[i] represents clearly
3. Find the recurrence relation (how current state relates to previous states)
4. Initialize base cases correctly
5. Implement with proper loop order and indexing

With practice, you will start recognizing these patterns immediately and know which approach to apply. Focus on understanding the underlying principles rather than memorizing solutions.

---

## LeetCode Blind 75 DP Problems Reference

The following problems from the Blind 75 list demonstrate these patterns. See [LeetCode_blind75_list.md](../ML-AI-engineer-cheetsheet/LeetCode_blind75_list.md) for complete solutions.

### Pattern 1: 1D Linear DP

| Problem | Link | Key Insight |
|---------|------|-------------|
| Climbing Stairs | [LeetCode #70](https://leetcode.com/problems/climbing-stairs/) | Pure Fibonacci: `dp[i] = dp[i-1] + dp[i-2]` |
| House Robber | [LeetCode #198](https://leetcode.com/problems/house-robber/) | Cannot rob adjacent: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| House Robber II | [LeetCode #213](https://leetcode.com/problems/house-robber-ii/) | Circular: run twice excluding first or last |
| Decode Ways | [LeetCode #91](https://leetcode.com/problems/decode-ways/) | Check valid 1-digit and 2-digit combinations |
| Maximum Product Subarray | [LeetCode #152](https://leetcode.com/problems/maximum-product-subarray/) | Track both max and min (negative × negative = positive) |

### Pattern 2: Knapsack / Unbounded Resource

| Problem | Link | Key Insight |
|---------|------|-------------|
| Coin Change | [LeetCode #322](https://leetcode.com/problems/coin-change/) | Min coins: `dp[i] = min(dp[i], dp[i-coin] + 1)` |
| Word Break | [LeetCode #139](https://leetcode.com/problems/word-break/) | Split point technique: check all j < i |
| Combination Sum IV | [LeetCode #377](https://leetcode.com/problems/combination-sum-iv/) | Permutations: target outer, items inner |
| Partition Equal Subset Sum | [LeetCode #416](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 Knapsack: iterate backwards |

### Pattern 3: Subsequence DP

| Problem | Link | Key Insight |
|---------|------|-------------|
| Longest Increasing Subsequence | [LeetCode #300](https://leetcode.com/problems/longest-increasing-subsequence/) | Check all j < i, return `max(dp)` |
| Longest Common Subsequence | [LeetCode #1143](https://leetcode.com/problems/longest-common-subsequence/) | Match: diagonal+1, No match: max of neighbors |

### Pattern 4: 2D Grid DP

| Problem | Link | Key Insight |
|---------|------|-------------|
| Unique Paths | [LeetCode #62](https://leetcode.com/problems/unique-paths/) | `dp[i][j] = dp[i-1][j] + dp[i][j-1]` |

### Quick Code Reference

```python
# Climbing Stairs - Pure Fibonacci
dp[i] = dp[i - 1] + dp[i - 2]

# Coin Change - Unbounded Knapsack
dp[i] = min(dp[i], dp[i - coin] + 1)

# LIS - Subsequence with condition
if nums[i-1] > nums[j-1]:
    dp[i] = max(dp[i], dp[j] + 1)

# LCS - 2D Match
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# Word Break - Split Point
if dp[j] and s[j:i] in words:
    dp[i] = True

# Maximum Product Subarray - Track Min/Max
dp_max[i] = max(num, dp_max[i-1]*num, dp_min[i-1]*num)
dp_min[i] = min(num, dp_max[i-1]*num, dp_min[i-1]*num)

# Partition Equal Subset Sum - 0/1 Knapsack (backwards)
for j in range(target, num - 1, -1):
    dp[j] = max(dp[j], dp[j - num] + num)
```

### Study Order Recommendation

1. **Start Simple:** Climbing Stairs → House Robber → Decode Ways
2. **Knapsack Basics:** Coin Change → Word Break → Partition Equal Subset Sum
3. **Subsequence:** LIS → LCS
4. **Advanced:** Maximum Product Subarray → Combination Sum IV