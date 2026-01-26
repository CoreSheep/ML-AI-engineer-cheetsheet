#!/bin/python3

import os
from collections import OrderedDict


def filter_transactions(threshold=50):
    def decorator(func):
        def wrapper(transactions):
            # Add original index
            indexed = [(name, amount, idx) for idx, (name, amount) in enumerate(transactions)]
            
            # Filter: keep if negative/zero OR >= threshold
            # "positive transactions below threshold" means amount > 0 and amount < threshold gets filtered
            filtered = [(name, amount, idx) for name, amount, idx in indexed 
                       if amount <= 0 or amount >= threshold]
            return func(filtered)
        return wrapper
    return decorator


def combine_transactions(func):
    def wrapper(transactions):
        first_occur = {}
        combined = OrderedDict()
        
        # Input is 3-tuple (name, amount, idx)
        for name, amount, idx in transactions:
            if name not in combined:
                combined[name] = amount
                first_occur[name] = idx
            else:
                combined[name] += amount
        
        # Exclude zero balances
        result = [(name, amount, first_occur[name]) 
                  for name, amount in combined.items() if amount != 0]
        return func(result)
    return wrapper


def sort_transactions(func):
    def wrapper(transactions):
        # Sort by amount descending, then by first occurrence ascending for ties
        sorted_trans = sorted(transactions, key=lambda x: (-x[1], x[2]))
        # Remove index - use different variable name!
        final = [(name, amount) for name, amount, _ in sorted_trans]
        return func(final)  # Return 2-tuples
    return wrapper


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    transactions = []
    for i in range(n):
        transaction = input().split(' ')
        transactions.append((transaction[0], int(transaction[1])))
    
    @filter_transactions(threshold=50)
    @combine_transactions
    @sort_transactions    
    def display_total_transactions(transactions):
        for person, total_amount in transactions:
            amount_str = f"${total_amount}" if total_amount >= 0 else f"-${total_amount*-1}"
            fptr.write(f"{person}: {amount_str}\n")
    
    display_total_transactions(transactions)
    fptr.close()