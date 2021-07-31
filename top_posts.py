#!/usr/bin/env python3
import pandas as pd

# Define number of rows (n) and columns to print
n = 50
columns = ['title', 'score', 'url', 'timestamp']

if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')
    data.sort_values(by='score', ascending=False, inplace=True)
    print(data.head(n)[columns])
