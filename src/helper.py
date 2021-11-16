#!/usr/bin/env python3
"""
Define helper functions
"""
import pandas as pd


def load_data() -> pd.DataFrame:
    """Read the subreddit posts as a DataFrame"""
    return pd.read_csv('../data/reddit_wsb.csv')


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    df.dropna(subset=['body'], inplace=True)
    words_in_title = df['title'].str.count(word)
    words_in_body = df['body'].str.count(word)
    word_found = df[(words_in_title > 0) | (words_in_body > 0)]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})
