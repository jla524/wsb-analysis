import pandas as pd
import matplotlib.pyplot as plt


def get_word_count(df: pd.DataFrame, word: str) -> pd.DataFrame:
    """Compute the number of times word is mentioned on WSB"""
    word_in_title = df['title'].str.contains(word, regex=False)
    word_in_body = df['body'].str.contains(word, regex=False)
    word_found = df[word_in_title | word_in_body][['date', 'title']]
    word_count = word_found.groupby('date').count().reset_index()
    return word_count.rename(columns={'title': 'count'})


if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')
    data['date'] = pd.to_datetime(data['timestamp']).dt.round('D')
    fig = plt.figure(figsize=(16, 9)) 
    plt.title('Keyword count over time')

    for word in ['GME', 'AMC', 'NOK', 'DD']:
        count_df = get_word_count(data, word)
        plt.plot(count_df['date'], count_df['count'], label=word)
   
    plt.legend()
    plt.show()
