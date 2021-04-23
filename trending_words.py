import pandas as pd
import matplotlib.pyplot as plt
from helper import get_word_count


if __name__ == '__main__':
    data = pd.read_csv('reddit_wsb.csv')
    data['date'] = pd.to_datetime(data['timestamp']).dt.round('D')
    fig = plt.figure(figsize=(16, 9)) 
    plt.title('Keyword count over time')

    for word in ['buy', 'GME', 'AMC', 'NOK', 'to the moon']:
        count_df = get_word_count(data, word)
        plt.plot(count_df['date'], count_df['count'], label=word)
   
    plt.legend()
    plt.show()
