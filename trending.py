import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


register_matplotlib_converters()


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    word_in_title = df['title'].str.contains(word, regex=False)
    word_in_body = df['body'].str.contains(word, regex=False)
    word_found = df[word_in_title | word_in_body][['date', 'title']]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})


def plot_word_count(df: pd.DataFrame) -> None:
    fig = plt.figure(figsize=(16, 9))
    plt.title('Keyword count over time')
    sns.lineplot(data=df, x='date', y='count', hue='keyword')
    fig.autofmt_xdate(ha='center')
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')
    data['date'] = pd.to_datetime(data['timestamp']).dt.round('D')
    counts = []

    for word in ['GME', 'AMC', 'NOK', 'DD']:
        count_df = get_word_count(data, word)
        count_df['keyword'] = word
        counts.append(count_df)

    plot_word_count(pd.concat(counts, sort=True))
