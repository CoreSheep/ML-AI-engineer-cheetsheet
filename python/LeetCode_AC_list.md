## LeetCode Problems Solved (Python)

**Total Solved: 26 problems** | **Difficulty: 26 Easy, 0 Medium**

| # | Problem ID | Difficulty | Problem Name |
|---|:----------:|:----------:|:-------------|
| 1 | 14 | Easy | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |
| 2 | 20 | Easy | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |
| 3 | 28 | Easy | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| 4 | 58 | Easy | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) |
| 5 | 67 | Easy | [Add Binary](https://leetcode.com/problems/add-binary/) |
| 6 | 125 | Easy | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |
| 7 | 168 | Easy | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) |
| 8 | 171 | Easy | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) |
| 9 | 205 | Easy | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) |
| 10 | 242 | Easy | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |
| 11 | 243 | Easy | [Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/) |
| 12 | 246 | Easy | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) |
| 13 | 257 | Easy | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) |
| 14 | 266 | Easy | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) |
| 15 | 290 | Easy | [Word Pattern](https://leetcode.com/problems/word-pattern/) |
| 16 | 293 | Easy | [Flip Game](https://leetcode.com/problems/flip-game/) |
| 17 | 344 | Easy | [Reverse String](https://leetcode.com/problems/reverse-string/) |
| 18 | 345 | Easy | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) |
| 19 | 383 | Easy | [Ransom Note](https://leetcode.com/problems/ransom-note/) |
| 20 | 387 | Easy | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) |
| 21 | 412 | Easy | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) |
| 22 | 415 | Easy | [Add Strings](https://leetcode.com/problems/add-strings/) |
| 23 | 434 | Easy | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) |
| 24 | 459 | Easy | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |
| 25 | 482 | Easy | [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) |
| 26 | 500 | Easy | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) |


### File Reading

#### 1. how to read different file types in python?
```python
# 1. read csv, excel, json, html using pandas
import pandas as pd

df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")s
df = pd.read_json("file.json")
df = pd.read_html("file.html")

# 2. Use with ... open() to read file
with open("file.csv", "r") as file:
    reader = csv.reader(file) 
    for row in reader: # read the file line by line
        print(row)

with open("file.txt", "r") as file: # read the file as a whole string
    content = file.read()
    print(content)

with open("file.txt", "r") as file: # read the file line by line
    for line in file:
        print(line)

with open("file.txt", "r") as file: # read all lines into a list
    lines = file.readlines()
    print(lines)

# 3. Use StringIO to read csv file from a string
from io import StringIO
import pandas as pd

csv_string = """name,age
John,25
Jane,30"""
df = pd.read_csv(StringIO(csv_string)) # read the csv file from the string
print(df)
```

### String
#### 1. how to use ord() and chr() in python?
```python
# ord() converts a character to its ASCII value
# Think of "order" or "ordinal number" - it gives you the order/position of a character in the character set.
print(ord("A")) # 65

# chr() converts an ASCII value to its character
print(chr(65)) # A
```

#### 2. how to use Counter() in python?
- Initialize a Counter from a string, list, dictionary, or keyword arguments
```python
from collections import Counter

# Method 1: From a string
counter1 = Counter("hello")
print(counter1)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Method 2: From a list
counter2 = Counter([1, 2, 2, 3, 3, 3])
print(counter2)  # Counter({3: 3, 2: 2, 1: 1})

# Method 3: From a dictionary
counter3 = Counter({'a': 3, 'b': 2})
print(counter3)  # Counter({'a': 3, 'b': 2})

# Method 4: From keyword arguments
counter4 = Counter(a=3, b=2, c=1)
print(counter4)  # Counter({'a': 3, 'b': 2, 'c': 1})

# Method 5: Empty counter
counter5 = Counter()
print(counter5)  # Counter()
```

- Accessing and updating counts
```python
from collections import Counter

c = Counter("aabbbc")
print(c)  # Counter({'b': 3, 'a': 2, 'c': 1})

# Access count of an element
print(c['a'])  # 2
print(c['b'])  # 3
print(c['c'])  # 1

# Accessing non-existent element returns 0 (not KeyError!)
print(c['z'])  # 0 ← This is special!

# Compare with regular dict:
regular_dict = {'a': 2, 'b': 3}
# print(regular_dict['z'])  # KeyError ❌
print(c['z'])  # 0 ✓ (Counter returns 0 for missing keys)
```

- Most common elements
```python
c = Counter("abracadabra")
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Get all elements sorted by frequency
print(c.most_common())
# [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

# Get top 2 most common
print(c.most_common(2))
# [('a', 5), ('b', 2)]

# Get top 1
print(c.most_common(1))
# [('a', 5)]
```

- + and - operations
```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

result = c1 + c2
print(result)  # Counter({'a': 4, 'b': 3})

# Only keeps positive counts
c3 = Counter(a=2, b=-1)
c4 = Counter(a=1, b=2)
result = c3 + c4
print(result)  # Counter({'a': 3, 'b': 1})

c1 = Counter(a=4, b=2, c=0)
c2 = Counter(a=1, b=2, c=1)

result = c1 - c2
print(result)  # Counter({'a': 3})
# Note: Only keeps positive counts! (b=0 and c=-1 are removed)

# Real-world example: Ransom Note
ransom = Counter("aa")
magazine = Counter("aab")
missing = ransom - magazine
print(missing)  # Counter() - empty, so ransom can be constructed!

ransom2 = Counter("aaa")
magazine2 = Counter("aab")
missing2 = ransom2 - magazine2
print(missing2)  # Counter({'a': 1}) - need 1 more 'a's
```

#### 3. how to use <= (is subset) and >= (is superset) in set in python?
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1 <= set2) # True
print(set1 >= set2) # False
```

