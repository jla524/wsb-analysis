#!/usr/bin/env python3
"""
Define helper functions
"""
from pathlib import Path
import pandas as pd


def load_data() -> pd.DataFrame:
    """Read the subreddit posts as a DataFrame"""
    root_path = Path(__file__).resolve(strict=True).parent.parent
    data_path = root_path / 'data'
    file_path = data_path / 'reddit_wsb.csv'
    return pd.read_csv(file_path)


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    df.dropna(subset=['body'], inplace=True)
    words_in_title = df['title'].str.count(word)
    words_in_body = df['body'].str.count(word)
    word_found = df[(words_in_title > 0) | (words_in_body > 0)]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})
