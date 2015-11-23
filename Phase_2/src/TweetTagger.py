import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.util import ngrams
import os
import sys

list_treebank_tags = ["JJ","JJR", "JJS", "NN", "NNS", "NNPS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "USR" ]
print os.getcwd()
text = ""
with open("../../data/f_hashtag_prediction/train_data_combined.txt", "a") as output_combined_file:
    with open("../../data/f_hashtag_prediction/train_data_tweets_processed.txt", "a") as output_file:
        with open("../../data/f_hashtag_prediction/train_data_tweets_tagged.txt", "rb") as input_file:
            for line in input_file:
                line = " ".join(line.split())
                words = line.split()
                processed_words = []
                processed_hashtags = []
                if len(words) > 0:
                    for w in words:
                        if '#' not in w:
                            if any(tag in w for tag in list_treebank_tags):
                                processed_words.append(w.split('/')[0].lower())
                        elif '#' in w or "HT" == w.split('/')[2]:
                            processed_hashtags.append(w.split('/')[0].lower())
                t = " ".join(processed_words)
                output_file.write("%s\n" % t)
                for tag in processed_hashtags:
                    tt = t + " " + tag
                    output_combined_file.write("%s\n" % tt)


sys.exit(0)

mytext = nltk.word_tokenize(text)
print nltk.pos_tag(mytext)

four_grams = list(ngrams([1,2,3,4,5], 4, pad_right=True,pad_symbol="END"))
print four_grams

ngrams_statistics = {}

for ngram in four_grams:
  if not ngrams_statistics.has_key(ngram):
      ngrams_statistics.update({ngram:1})
  else:
      ngram_occurrences = ngrams_statistics[ngram]
      ngrams_statistics.update({ngram:ngram_occurrences+1})

print ngrams_statistics

ngrams_statistics_sorted = sorted(ngrams_statistics.iteritems(), reverse=True)
print ngrams_statistics_sorted

