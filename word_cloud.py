#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from string import punctuation


def clean_text(text: str) -> str:
    """Remove special characters from text"""
    return ''.join(c for c in text if c not in punctuation)


if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')

    # Store title and body text into numpy array
    title = data['title'].apply(clean_text)
    body = data['body'].fillna('').apply(clean_text)
    words = np.concatenate((title, body), axis=None)

    # Create and display word cloud
    wc = WordCloud(width=1600, height=900, background_color='white')
    wc.generate(''.join(words))
    plt.figure(figsize=(16, 9))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
