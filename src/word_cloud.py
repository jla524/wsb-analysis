#!/usr/bin/env python3
"""
Create a word cloud using text from r/wallstreetbets
This may take a while to execute
"""
from string import punctuation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from helper import load_data


def clean_text(text: str) -> str:
    """Remove special characters from text"""
    return ''.join(c for c in text if c not in punctuation)


if __name__ == '__main__':
    posts = load_data()

    # Store title and body text into numpy array
    title = posts['title'].apply(clean_text)
    body = posts['body'].fillna('').apply(clean_text)
    words = np.concatenate((title, body), axis=None)

    # Create and display word cloud
    wc = WordCloud(width=1600, height=900, background_color='white')
    wc.generate(''.join(words))
    plt.figure(figsize=(16, 9))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
