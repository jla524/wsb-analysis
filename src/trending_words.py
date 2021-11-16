#!/usr/bin/env python3
"""
Plot the count of words over time in r/wallstreetbets
"""
import pandas as pd
import matplotlib.pyplot as plt
from helper import load_data, get_word_count

# Define keywords to plot
keywords = ['buy', 'GME', 'AMC', 'NOK', 'to the moon']

if __name__ == '__main__':
    posts = load_data()
    posts['date'] = pd.to_datetime(posts['timestamp']).dt.round('D')
    fig = plt.figure(figsize=(16, 9))
    plt.title('Keyword count over time')

    for keyword in keywords:
        word_counts = get_word_count(posts, keyword)
        plt.plot(word_counts['date'], word_counts['count'], label=keyword)

    plt.legend()
    plt.show()
