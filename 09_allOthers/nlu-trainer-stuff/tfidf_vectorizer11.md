`TfidfVectorizer`
- Convert a collection of raw documents to a matrix of <TF-IDF features>
- https://www.capitalone.com/tech/machine-learning/understanding-tf-idf/

https://goodboychan.github.io/python/datacamp/natural_language_processing/2020/07/17/04-TF-IDF-and-similarity-scores.html

`TF-IDF`
- term frequency - inverse document frequency
- quantify the importance of strings/words/phrases/lemmas
- in a document amongst a collection of documents (ie corpus)

`term frequency (tf)`
- number of times a word appears in document
- tf adjusted for length of document    
    madrid appears 23 times in 100 word document
    madrid appears 11 times in 15 word document

`inverse document frequency (idf)`
- how common/uncommon a word is amongst the corpus (corpus === 44 documents)


# higher TF-IDF score ====> more important the term is

<!-- --------------------------------- -->

# Applications

`NLP`
- when dealing with textual data
- data first needs to be converted to a vector
- <TF-IDF vectorization> involves calculating the <TF-IDF score> for <every word> in your corpus
- see if two documents are similar

`information retrieval`
- search with keyword ---> returns 5000 results
- rank/sort/order search results based on relevance
- words with the highest relevance ===> come at top of search result


<!-- --------------------------------- -->

# Other NLP algorithms

`Bag of Words (BoW)`
- simply counts the frequency of words in document
- doesnt incorporate IDF

`Word2Vec`
- ingest a corpus & produce sets of vectors (1 vector for each word)
- in word2vec, more work need to convert <set of vectors> into <singular vector>
- But TF-IDF doesnt take into consideration <context of words> in the corpus, but word2vec does

`BERT`
- BERT (dvlpd by Google), uses deep neural networks, computationally expensive
- TF-IDF doesnt take into account semantic meaning (or) word context, but BERT does
<!-- --------------------------------- -->