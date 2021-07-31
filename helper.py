import pandas as pd


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    df.dropna(subset=['body'], inplace=True)
    word_in_title = df['title'].str.count(word)
    word_in_body = df['body'].str.count(word)
    word_found = df[(word_in_title > 0) | (word_in_body > 0)]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})
