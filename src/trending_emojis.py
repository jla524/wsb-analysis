#!/usr/bin/env python3
"""
Plot the count of emojis over time in r/wallstreetbets
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from helper import load_data, get_word_count

# Use a third-party backend for plotting emojis
matplotlib.use("module://mplcairo.macosx")
prop = FontProperties(fname='/System/Library/Fonts/Apple Color Emoji.ttc')
emojis = ['🚀', '💎', '🤲', '🐻']

if __name__ == '__main__':
    posts = load_data()
    posts['date'] = pd.to_datetime(posts['timestamp']).dt.round('D')
    fig = plt.figure(figsize=(16, 9))
    plt.title('Emoji count over time')

    for emoji in emojis:
        word_counts = get_word_count(posts, emoji)
        plt.plot(word_counts['date'], word_counts['count'], label=emoji)

    plt.legend(prop=prop)
    plt.show()
