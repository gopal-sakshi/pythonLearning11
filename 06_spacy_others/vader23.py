from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()

# The polarity score() method returns a float for the sentiment strength based on the input text;
statements11 = [
    "What a wonderful day",
    # "Thank you for clarifying that my eye cancer will not yield me deaf. I consider myself extremely fortunate that an intellectual giant such as yourself would choose to operate on me",
    # "We shared our sadness at the waste of two barely emerging lives with the remainder of the celebratory bourbon.",
    # "She didn't know whether to be angry or frightened because she had never been propositioned before."
    "worst behaviour",
    "stupid response",
    "very bad",
    "bad",
    "not good",
    "average",
    "not bad",
    "good",
    "very good"
]


for s in statements11:
    scr = sa.polarity_scores(s)["compound"]
    # print(f'Sentiment value of:-\n"{s}" =====> {scr}')
    print("Sentiment value of ", s[0:20] ," =====>", scr)