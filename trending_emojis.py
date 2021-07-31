#!/usr/bin/env python3
import matplotlib
import mplcairo
import pandas as pd
from helper import get_word_count
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Use a third-party backend for plotting emojis
matplotlib.use("module://mplcairo.macosx")
prop = FontProperties(fname='/System/Library/Fonts/Apple Color Emoji.ttc')
emojis = ['🚀', '💎', '🤲', '🐻']

if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')
    data['date'] = pd.to_datetime(data['timestamp']).dt.round('D')
    fig = plt.figure(figsize=(16, 9))
    plt.title('Emoji count over time')

    for emoji in emojis:
        count_df = get_word_count(data, emoji)
        plt.plot(count_df['date'], count_df['count'], label=emoji)

    plt.legend(prop=prop)
    plt.show()
