# Dynamic Programming Mastery Guide

## The Universal 5-Step Framework

Every DP problem follows this structure:

1. **Define dp[i] meaning** - What does this index represent?
2. **Find the recurrence relation** - How does dp[i] relate to previous states?
3. **Initialize base cases** - What are dp[0], dp[1], etc.?
4. **Determine iteration order** - Left-to-right or right-to-left?
5. **Trace an example** - Debug with a small test case

---

## Pattern Classification

### Pattern 1: 1D Linear DP

**When to use:** Current state depends only on previous positions in a single sequence

```python
dp = [base_value] * (n + 1)
dp[0] = initial_condition

for i in range(1, n + 1):
    dp[i] = f(dp[i-1], dp[i-2], ..., current_element)
```

| Problem | dp[i] Meaning | Recurrence |
|---------|---------------|------------|
| Climbing Stairs | Ways to reach step i | `dp[i] = dp[i-1] + dp[i-2]` |
| House Robber | Max money up to house i | `dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])` |
| Decode Ways | Ways to decode s[0:i] | `dp[i] = dp[i-1] + dp[i-2]` (if valid) |
| Max Product Subarray | Track both max/min | `dp_max[i] = max(num, dp_max[i-1]*num, dp_min[i-1]*num)` |

**Tips:**
- Check dp[i-1] and dp[i-2] for state transitions
- Use `max()` for optimization, `+=` for counting
- Initialize dp[0] and dp[1] carefully

---

### Pattern 2: Knapsack / Unbounded Resource

**When to use:** Items/coins filling a target/amount

```python
dp = [base_value] * (target + 1)
dp[0] = initial_condition

for i in range(target + 1):
    for item in items:
        if can_use_item:
            dp[i] = update_function(dp[i], dp[i - item])
```

| Problem | dp[i] Meaning | Update Rule |
|---------|---------------|-------------|
| Coin Change | Min coins for amount i | `dp[i] = min(dp[i], dp[i-coin] + 1)` |
| Combination Sum IV | Ways to sum to i | `dp[i] += dp[i-num]` |
| Word Break | Can break s[0:i]? | `dp[i] = True if dp[j] and s[j:i] in words` |
| Partition Equal Subset | Can achieve sum? | `dp[j] = max(dp[j], dp[j-num] + num)` |

**Loop Order Matters:**
```
COMBINATIONS: items outer → target inner
PERMUTATIONS: target outer → items inner
MIN/MAX: either order works
```

---

### Pattern 3: Subsequence DP

**When to use:** Finding longest/best subsequence with constraints

```python
dp = [1] * n  # Each element is a subsequence of length 1

for i in range(n):
    for j in range(i):  # Look back at ALL previous elements
        if condition(nums[j], nums[i]):
            dp[i] = max(dp[i], dp[j] + 1)
```

| Problem | dp[i] Meaning | Condition | Return |
|---------|---------------|-----------|--------|
| LIS | LIS ending at i | `nums[j] < nums[i]` | `max(dp)` |
| LCS | LCS of text1[0:i], text2[0:j] | `text1[i-1] == text2[j-1]` | `dp[m][n]` |

**Key Insight:** `dp[i]` = best subsequence **ENDING AT** position i, not considering first i elements.

---

### Pattern 4: 2D Grid DP

**When to use:** Robot movement, grid paths, 2D state problems

```python
dp = [[0] * n for _ in range(m)]

# Initialize borders
for i in range(m): dp[i][0] = ...
for j in range(n): dp[0][j] = ...

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

| Problem | dp[i][j] Meaning | Recurrence |
|---------|------------------|------------|
| Unique Paths | Paths to (i,j) | `dp[i-1][j] + dp[i][j-1]` |
| LCS | LCS length | Match: `dp[i-1][j-1] + 1`, No: `max(neighbors)` |

---

## Quick Reference

### Initialization Patterns

| dp[0] Value | Use Case | Example |
|-------------|----------|---------|
| `0` | Empty state is 0 | Coin Change |
| `1` | Empty state is valid | Climbing Stairs |
| `True` | Empty state reachable | Word Break |
| `float('inf')` | Impossible state | Coin Change (all amounts) |

### Index Gymnastics

```python
# dp size (n+1), nums size n:
for i in range(1, n + 1):
    dp[i] relates to nums[i-1]

# dp size n, nums size n:
for i in range(n):
    dp[i] relates to nums[i]

# 2D LCS:
dp[i][j] compares text1[i-1] with text2[j-1]
```

### Space Optimization

```python
# If dp[i] only depends on dp[i-1] and dp[i-2]:
prev2, prev1 = dp[0], dp[1]
for i in range(2, n):
    curr = prev1 + prev2
    prev2, prev1 = prev1, curr
```

---

## Problem-Specific Patterns

### House Robber II (Circular)
```python
# Run twice: exclude first OR exclude last
return max(rob(nums[:-1]), rob(nums[1:]))
```

### Word Break (Split Point)
```python
for i in range(1, n + 1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break
```

### Jump Game (Greedy)
```python
max_reach = 0
for i in range(n):
    if i > max_reach:
        return False
    max_reach = max(max_reach, i + nums[i])
return True
```

---

## Debugging Checklist

- [ ] Initialized dp[0] correctly?
- [ ] Using i-1 when dp is size n+1?
- [ ] For knapsack: i - item >= 0?
- [ ] For subsequence: checking j < i?
- [ ] Return `max(dp)` vs `dp[n]`?
- [ ] For min: checked `float('inf')`?
- [ ] For 2D: initialized borders?

---

## Complexity Reference

| Pattern | Time | Space |
|---------|------|-------|
| Fibonacci-like | O(n) | O(1) optimized |
| Knapsack | O(n × m) | O(n) |
| Subsequence | O(n²) | O(n) |
| 2D Grid | O(m × n) | O(m × n) |

---

## LeetCode Blind 75 Reference

See [LeetCode_blind75_list.md](../LeetCode_blind75_list.md) for complete solutions.

### 1D Linear DP
| Problem | Link |
|---------|------|
| Climbing Stairs | [#70](https://leetcode.com/problems/climbing-stairs/) |
| House Robber | [#198](https://leetcode.com/problems/house-robber/) |
| House Robber II | [#213](https://leetcode.com/problems/house-robber-ii/) |
| Decode Ways | [#91](https://leetcode.com/problems/decode-ways/) |
| Max Product Subarray | [#152](https://leetcode.com/problems/maximum-product-subarray/) |

### Knapsack
| Problem | Link |
|---------|------|
| Coin Change | [#322](https://leetcode.com/problems/coin-change/) |
| Word Break | [#139](https://leetcode.com/problems/word-break/) |
| Combination Sum IV | [#377](https://leetcode.com/problems/combination-sum-iv/) |
| Partition Equal Subset Sum | [#416](https://leetcode.com/problems/partition-equal-subset-sum/) |

### Subsequence
| Problem | Link |
|---------|------|
| Longest Increasing Subsequence | [#300](https://leetcode.com/problems/longest-increasing-subsequence/) |
| Longest Common Subsequence | [#1143](https://leetcode.com/problems/longest-common-subsequence/) |

### 2D Grid
| Problem | Link |
|---------|------|
| Unique Paths | [#62](https://leetcode.com/problems/unique-paths/) |

---

## Study Order

1. **1D Linear:** Climbing Stairs → House Robber → Decode Ways
2. **Knapsack:** Coin Change → Word Break → Partition Equal Subset Sum
3. **Subsequence:** LIS → LCS
4. **Advanced:** Max Product Subarray → Combination Sum IV
