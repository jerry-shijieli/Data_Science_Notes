# -*- coding: utf-8 -*-

from nltk.tokenize import sent_tokenize, word_tokenize # tokenize text into sentences and words
from nltk.corpus import stopwords # find and filter very common words

from collections import defaultdict # dictionary with default value

from string import punctuation # punctuation symbols

from heapq import nlargest # return n largest elements in given list

class FrequencySummarizer:
    # initialize variables
    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut # word frequency smaller than this will be ignored
        self._max_cut = max_cut # word frequency larger than this will be ignored
        self._stopwords = set(stopwords.words('english') + list(punctuation))

    # count word  and then filter by frequency thresholds
    def _compute_frequencies(self, word_sent):
        freq = defaultdict(int) # key: words, value: counts
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        # normalize frequency using max value
        m = float(max(freq.values()))
        for w in freq.keys():
            freq[w] = freq[w] / m
            if freq[w]>=self._max_cut or freq[w]<=self._min_cut:
                del freq[w]

        return freq

    # summarize text using limited number of sentences
    def summarize(self, text, n):
        sents = sent_tokenize(text) # break text into sentences
        assert n <- len(sents) # check if summary is shorter than original text
        word_sent = [word_tokenize(s.lower()) for s in sents] # break each sentence into list of words
        self._freq = self._compute_frequencies(word_sent) # get word count and filter words by frequency
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w] # rank sentence as sum of words in it
        sents_idx = nlargest(n, ranking, key=ranking.get) # select the index of top ranked sentence

        return [sents[j] for j in sents_idx]  # return top ranked sentence text