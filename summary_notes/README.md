# Algorithm Summary Notes

Comprehensive guides for mastering algorithm patterns and problem-solving techniques.

## Contents

### dp_mastery_guide.md

A complete guide to Dynamic Programming with:

- **Universal 5-Step Framework**: Systematic approach to any DP problem
- **Pattern Classification**: 5 major DP patterns with examples
- **Problem Mappings**: Direct links to LeetCode Blind 75 problems
- **Code Templates**: Ready-to-use patterns for each category

## DP Patterns Overview

```
Dynamic Programming Patterns
│
├── 1D Linear DP
│   └── Examples: Climbing Stairs, House Robber, Decode Ways
│
├── Knapsack / Unbounded Resource
│   └── Examples: Coin Change, Combination Sum, Word Break
│
├── Subsequence DP
│   └── Examples: LIS, LCS, Palindrome Subsequence
│
├── 2D Grid DP
│   └── Examples: Unique Paths, Min Path Sum, Edit Distance
│
└── State Machine DP
    └── Examples: Stock Trading, Paint House
```

## Quick Reference

### The 5-Step Framework

1. **Define dp[i] meaning**: What does this index represent?
2. **Find recurrence relation**: How does dp[i] relate to previous states?
3. **Initialize base cases**: What are dp[0], dp[1], etc.?
4. **Determine iteration order**: Left-to-right or right-to-left?
5. **Trace an example**: Debug with a small test case

### Pattern Recognition

**Use 1D Linear DP when**:
- Current state depends on previous positions in a sequence
- Examples: "Ways to reach step i", "Max profit up to house i"

**Use Knapsack when**:
- Items/coins filling a target/amount
- Examples: "Min coins for amount", "Can partition array"

**Use Subsequence DP when**:
- Finding longest/best subsequence with constraints
- Examples: "Longest increasing subsequence", "Longest common subsequence"

**Use 2D Grid DP when**:
- Two sequences to compare or align
- Grid/matrix traversal
- Examples: "Edit distance", "Unique paths in grid"

**Use State Machine when**:
- Multiple states with transitions
- Cooldown or constraint periods
- Examples: "Stock trading with cooldown", "Paint house with rules"

## Key Insights

### Loop Order Matters

For knapsack problems:
```python
# COMBINATIONS: items outer → target inner
for item in items:
    for i in range(target + 1):
        dp[i] = update(dp[i], dp[i - item])

# PERMUTATIONS: target outer → items inner
for i in range(target + 1):
    for item in items:
        dp[i] = update(dp[i], dp[i - item])
```

### Common Pitfalls

1. **Off-by-one errors**: Carefully define index meanings
2. **Base case initialization**: Don't assume dp[0] = 0
3. **Iteration direction**: Some problems need reverse iteration
4. **State definition**: Include all necessary information
5. **Edge cases**: Empty arrays, single elements

## Study Plan

1. **Start with 1D Linear DP**: Build intuition
2. **Master Knapsack**: Understand bounded vs unbounded
3. **Practice Subsequence DP**: Develop pattern recognition
4. **Tackle 2D Grid DP**: Learn state representation
5. **Challenge State Machine DP**: Apply multiple concepts

## References

- [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)
- [LeetCode Blind 75](../LeetCode_blind75_list.md)
- [DP Patterns on LeetCode](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
