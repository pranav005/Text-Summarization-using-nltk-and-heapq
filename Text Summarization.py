#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
f=open("test.txt",encoding="utf8")
article_text=f.read()


# In[2]:


# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'.\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)


# In[3]:


print(article_text)


# In[4]:


formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)


# In[5]:


print(formatted_article_text)


# In[6]:


import nltk
sentence_list = nltk.sent_tokenize(article_text)


# In[7]:


stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


# In[8]:


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


# In[9]:


sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


# In[10]:


import heapq
summary_sentences = heapq.nlargest(4, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)


# In[ ]:




