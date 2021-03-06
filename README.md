# WSB Analysis

An deep dive on WallStreetBets posts.


## Quickstart Guide
1. Clone this repository
   ```
   git clone git@github.com:jla524/wsb-analysis.git
   cd wsb-analysis
   ```
2. [Download the dataset][0] from Kaggle into the `data/` directory
3. Create a virtual environment (optional)
   ```
   python3 -m venv env
   source env/bin/activate
   ```
4. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the scripts in the `src/` directory


## Outputs
### Top Posts
Print a list of top N posts (ranked by score) in the subreddit.
```
                                                   title   score                                                url            timestamp
19162                             Times Square right now  348241                    https://v.redd.it/x64z70f7eie61  2021-01-31 04:00:38
16009                      GME YOLO update β Jan 28 2021  225870                https://i.redd.it/opzucppb15e61.png  2021-01-29 07:06:23
17771               GME YOLO month-end update β Jan 2021  219779                https://i.redd.it/r557em3t5ce61.png  2021-01-30 07:04:45
34179                      GME YOLO update β Feb 19 2021  201168                https://i.redd.it/2xswz0h11ii61.png  2021-02-20 07:05:55
18273                                  Itβs treason then  195782                https://i.redd.it/d3t66lv1yce61.jpg  2021-01-30 09:40:59
```

### Trending Emojis
Given a list of emojis, display the number of times they have been used (in title or body) for each day.
![emoji.png][1]

### Trending Words
Similar to emojis, but take a list of words (or phrases).
![word.png][2]

### Word Cloud
Generate a word cloud using all words in the dataset.
![cloud.png][3]


## Acknowledgement
The [dataset][0] is provided by Gabriel Preda and hosted on Kaggle


[0]: https://www.kaggle.com/gpreda/reddit-wallstreetsbets-posts
[1]: https://github.com/jla524/wsb-analysis/blob/main/images/emoji.png?raw=true
[2]: https://github.com/jla524/wsb-analysis/blob/main/images/word.png?raw=true
[3]: https://github.com/jla524/wsb-analysis/blob/main/images/cloud.png?raw=true
