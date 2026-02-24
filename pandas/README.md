# Pandas Cheatsheet

Practical Pandas operations and data manipulation techniques.

## Contents

### Interactive Guide

**pandas_cheatsheet.ipynb**
- Comprehensive Jupyter notebook with examples
- DataFrame operations
- Data cleaning and transformation
- Time series manipulation
- Visualization basics

### LeetCode with Pandas

**LeetCode_AC_list.md**
- LeetCode problems solved using Pandas
- Data manipulation techniques
- SQL-like operations in Pandas

### Reference Materials

**img/strftime.png**
- Date/time formatting reference
- strftime directives
- Common patterns

## Quick Reference

### Data Loading
```python
import pandas as pd

# Read various formats
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
df = pd.read_html("file.html")[0]

# With options
df = pd.read_csv("file.csv",
                 sep=",",
                 header=0,
                 index_col=0,
                 parse_dates=["date_column"])
```

### Data Inspection
```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.info()           # Column types and non-null counts
df.describe()       # Statistical summary
df.shape            # (rows, columns)
df.columns          # Column names
df.dtypes           # Data types
```

### Data Selection
```python
# Column selection
df["column"]
df[["col1", "col2"]]

# Row selection
df.loc[0]           # By label
df.iloc[0]          # By position
df[df["age"] > 25]  # Conditional

# Combined
df.loc[df["age"] > 25, ["name", "age"]]
```

### Data Manipulation
```python
# Filter
df[df["column"] > value]
df[df["column"].isin([val1, val2])]

# Sort
df.sort_values("column", ascending=True)
df.sort_values(["col1", "col2"], ascending=[True, False])

# Group by
df.groupby("column").mean()
df.groupby("column").agg({"col1": "sum", "col2": "mean"})

# Merge
pd.merge(df1, df2, on="key", how="inner")  # inner, outer, left, right
```

### Data Cleaning
```python
# Missing values
df.isnull().sum()           # Count nulls per column
df.dropna()                 # Drop rows with nulls
df.fillna(value)            # Fill nulls
df.fillna(df.mean())        # Fill with column mean

# Duplicates
df.duplicated().sum()       # Count duplicates
df.drop_duplicates()        # Remove duplicates

# Type conversion
df["column"] = df["column"].astype(int)
df["date"] = pd.to_datetime(df["date"])
```

### Time Series
```python
# Date manipulation
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.day_name()

# Resampling
df.set_index("date").resample("D").mean()  # Daily average
df.set_index("date").resample("M").sum()   # Monthly sum

# Date formatting
df["date"].dt.strftime("%Y-%m-%d")
```

### Feature Engineering
```python
# Create new columns
df["total"] = df["price"] * df["quantity"]
df["is_adult"] = df["age"] >= 18

# Apply functions
df["column"] = df["column"].apply(lambda x: x * 2)
df["name"] = df["name"].apply(str.upper)

# Binning
df["age_group"] = pd.cut(df["age"],
                         bins=[0, 18, 35, 60, 100],
                         labels=["Child", "Young", "Adult", "Senior"])
```

### Common Patterns

#### Find and Replace
```python
df["column"] = df["column"].replace(old_value, new_value)
df["column"] = df["column"].str.replace("old", "new")
```

#### Conditional Operations
```python
df["category"] = df["score"].apply(
    lambda x: "High" if x > 80 else "Medium" if x > 50 else "Low"
)

# or using np.where
import numpy as np
df["category"] = np.where(df["score"] > 80, "High",
                 np.where(df["score"] > 50, "Medium", "Low"))
```

#### Pivot Tables
```python
pivot = df.pivot_table(
    values="sales",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0
)
```

## Performance Tips

1. **Use vectorized operations** instead of loops
2. **Use categorical dtype** for columns with few unique values
3. **Read large files in chunks** with `chunksize` parameter
4. **Use query() method** for complex filters
5. **Avoid chained indexing** (use .loc instead)

## Common Mistakes

```python
# Bad: Chained indexing
df[df["A"] > 5]["B"] = 10

# Good: Use .loc
df.loc[df["A"] > 5, "B"] = 10

# Bad: Loop over rows
for i in range(len(df)):
    df.iloc[i, 0] = df.iloc[i, 0] * 2

# Good: Vectorized operation
df.iloc[:, 0] = df.iloc[:, 0] * 2
```

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
