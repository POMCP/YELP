import pandas as pd
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from gensim import corpora, models
from collections import defaultdict
import time

'''Generate Data structures
# Business
print 'Loading Business json file...'
load_data('yelp_academic_dataset_business.json', {'business_id', 'name', 'stars', 'categories'})
print 'Done loading'

Review
print 'Loading Review json file...'
load_data('yelp_academic_dataset_user.json', {'business_id', 'user_id', 'stars', 'text'})
print 'Done loading'

User
print 'Loading User json file...'
load_data('yelp_academic_dataset_user.json', {'user_id', 'name', 'friends'})
print 'Done loading'''

df_b = pd.read_pickle('df_b.pkl')
df_r = pd.read_pickle('df_rf.pkl')
df_u = pd.read_pickle('df_u.pkl')

'''==========================================================
Generating a lda model
============================================================='''
# compile reviews into a list
doc_set = [item.decode('utf-8').encode('ascii', 'ignore') for item in df_r['text']]

'''Tokenize the data'''
tokenizer = RegexpTokenizer(r'\w+')
raw = [i.lower() for i in doc_set]  # Convert to lower case
tokens = [tokenizer.tokenize(i) for i in raw]

'''Remove stop words form the tokens'''
# create English stop words list
en_stop = get_stop_words('en')
stop_tokens = [[i for i in j if not i in en_stop and len(i) != 1] for j in tokens]

# remove words that appear only once
frequency = defaultdict(int)
for text in stop_tokens:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]for text in stop_tokens]

'''Generating the LDA model'''
# traverses texts, assigning a unique integer id to each unique token
# while also collecting word counts and relevant statistics.
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]  # Converting dictionary to Bag of Words
tfidf = models.TfidfModel(corpus)  # Transforming the vector space
corpus = tfidf[corpus]

'''Train the LDA model'''
print 'Model Training Time: '
print 'start time'
ldamodel = models.ldamulticore.LdaMulticore(corpus, num_topics=50, id2word=dictionary, passes=2)
print 'end time'
dictionary.save('full_dictionary')
ldamodel.save('full_model')
print '================================='
print 'Time Ended: ', time.time()
print '==================================='
