from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()

# The polarity score() method returns a float for the sentiment strength based on the input text;
statements11 = [
    "What a wonderful day",
    # "Thank you for clarifying that my eye cancer will not yield me deaf. I consider myself extremely fortunate that an intellectual giant such as yourself would choose to operate on me",
    # "We shared our sadness at the waste of two barely emerging lives with the remainder of the celebratory bourbon.",
    # "She didn't know whether to be angry or frightened because she had never been propositioned before."
    "atrocious wicked cruel henious character",
    "worst behaviour",
    "stupid response",
    "very bad",
    "bad",
    "not good",
    "average",
    "not bad",
    "good",
    "very good",
    "superb and splending, excellent response, totally satisfied"
]

statements12 = [
    "What a wonderful day",
    "Thank you for clarifying that my eye cancer will not yield me deaf. I consider myself extremely fortunate",
    "We shared our sadness at the waste of two barely emerging lives with the remainder of the celebratory bourbon.",
    "She didn't know whether to be angry or frightened because she had never been propositioned before."
    "atrocious wicked cruel henious character",
    "superb and splending, excellent response, totally satisfied"
]

str23 = "Thank you for clarifying that my eye cancer will not yield me deaf. I consider myself extremely fortunate"
scr_pos = sa.polarity_scores(str23)["pos"]
print("scr_pos ============> ", scr_pos)
scr_neg = sa.polarity_scores(str23)["neg"]
print("scr_neg ============> ", scr_neg)

for s in statements11:
    scr = sa.polarity_scores(s)
    # scr = sa.polarity_scores(s)["compound"]
    # print(f'Sentiment value of:-\n"{s}" =====> {scr}')
    print("Sentiment value of ", s[0:20] ," =====>", scr, '\t\t___', scr["compound"])