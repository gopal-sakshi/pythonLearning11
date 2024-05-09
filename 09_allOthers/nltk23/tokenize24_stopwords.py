import nltk

from nltk.corpus import stopwords
# nltk.download()                   ### trying to download whole data in nltk ---> takes very long time
nltk.download("stopwords")          ### only download stopwords

print("stopwords in english ===> ", stopwords.words("english"))
# print("stopwords in german ===> ", stopwords.words("german"))




