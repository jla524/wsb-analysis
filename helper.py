import pandas as pd


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    word_in_title = df['title'].str.contains(word, regex=False)
    word_in_body = df['body'].str.contains(word, regex=False)
    word_found = df[word_in_title | word_in_body][['date', 'title']]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})
