#!/usr/bin/env python3
"""
Show the top N=50 posts by score.
"""
import pandas as pd
from helper import load_data

# Define number of rows (n) and columns to print
n = 50
columns = ['title', 'score', 'url', 'timestamp']

if __name__ == '__main__':
    posts = load_data()
    posts.sort_values(by='score', ascending=False, inplace=True)
    print(posts.head(n)[columns])
