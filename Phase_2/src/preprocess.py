import csv
import time
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import sys

def extract_hashtags(s):
    return set(part[1:].lower().strip().rstrip(',') for part in s.split() if part.startswith('#'))

#split into userid, tweets, location
def split_dataset(fileName, file_userid, file_tweets, file_location):

    f_userid = open(file_userid, "w")
    f_tweets = open(file_tweets, "w")
    f_location = open(file_location, "w")

    with open(fileName) as input_file:
        for line in input_file:
            line = " ".join(line.split())
            words = line.split()
            userid = words[0]
            tweet = words[1:len(words)-2]
            location = words[len(words)-2:]
            f_userid.write("%s\n" % userid)
            f_tweets.write("%s\n" % " ".join(tweet))
            f_location.write("%s\n" % " ".join(location))

    f_userid.close()
    f_tweets.close()
    f_location.close()

def extract_tags(fileName, f_allhashtags):
    list_all_hashtags = []
    with open(fileName) as f:
        with open(f_allhashtags, "wb") as output:
            unique_hashtags = set()
            num_total_hashtags = 0
            num_total_tweets = 0
            for line in f:
                num_total_tweets = num_total_tweets + 1
                hashtags = extract_hashtags(line)
                for i in hashtags:
                    list_all_hashtags.append(i)
                unique_hashtags.update(hashtags)
                num_total_hashtags = num_total_hashtags + len(hashtags)
                output.write("%s\n" % ",".join(hashtags))

            print "Total number of tweets: " + str(num_total_tweets)

def read_tweets(fileName, f_allhashtags, f_uniquetags, fileName_train_hashtag_histogram):
    list_all_hashtags = []
    with open(f_allhashtags, "wb") as output:
        with open(fileName) as f:
            unique_hashtags = set()
            num_total_hashtags = 0
            num_total_tweets = 0
            for line in f:
                num_total_tweets = num_total_tweets + 1
                hashtags = extract_hashtags(line)
                for i in hashtags:
                    list_all_hashtags.append(i)
                unique_hashtags.update(hashtags)
                num_total_hashtags = num_total_hashtags + len(hashtags)
                output.write("%s\n" % ",".join(hashtags))
            with open(f_uniquetags, "wb") as output_unique:
                output_unique.write("%s\n" % ",".join(unique_hashtags))

            print "Total number of tweets: " + str(num_total_tweets)
            print "Number of total hashtags: " + str(num_total_hashtags)
            print "Number of unique hashtags: " + str(len(unique_hashtags))
            print "Average number of hashtags per tweet : " + str(num_total_hashtags * 1.0 /num_total_tweets)

            dict_hashtag_counts = Counter(list_all_hashtags)
            with open(fileName_train_hashtag_histogram,"wb") as f:
                for k,v in dict_hashtag_counts.most_common():
                    f.write("{} {}\n".format(k,v))



def histogram_plot(counts):
    words = [x[0] for x in counts[:100]]
    values = [int(x[1]) for x in counts[:100]]
    print words
    plt.bar(range(len(words)), values, color='green', alpha=0.4)

    plt.xlabel('Word Index')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Chart')
    plt.legend()

#     # Label the raw counts and the percentages below the x-axis...
#     bin_centers = 0.5 * np.diff(bins) + bins[:-1]
#     for count, x in zip(counts, bin_centers):
#         #Label the raw counts
#         ax.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
#         xytext=(0, -18), textcoords='offset points', va='top', ha='center')
#
#     # Label the percentages
#     percent = '%0.0f%%' % (100 * float(count) / counts.sum())
#     ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
#         xytext=(0, -32), textcoords='offset points', va='top', ha='center')
#
#
# #   Give ourselves some more room at the bottom of the plot
#     plt.subplots_adjust(bottom=0.15)
    plt.show()
#main
# tweet = "111648679	ALL TEARGAS IN ONE PLACE! http://t.co/RIgMZ5B2 #1staid4 #Egypt #Syria #Libya #Yemen #Bahrain #Firstaid #Homs #Sudan #Tunisia RT *	0	0"
# print extract_hashtags(tweet)
start_time = time.time()

fileName_train_data = "../data/f_hashtag_prediction/train_data_raw.txt"
fileName_train_userid = "../data/f_hashtag_prediction/train_data_userid.txt"
fileName_train_tweets = "../data/f_hashtag_prediction/train_data_tweets.txt"
fileName_train_location = "../data/f_hashtag_prediction/train_data_location.txt"

split_dataset(fileName_train_data, fileName_train_userid, fileName_train_tweets, fileName_train_location)

fileName_train_tweet_all_hashtags = "../data/f_hashtag_prediction/train_data_all_hashtags.txt"
fileName_train_tweet_unique_hashtags = "../data/f_hashtag_prediction/train_data_unique_hashtags.txt"
fileName_train_hashtag_histogram = "../data/f_hashtag_prediction/train_data_histogram_hashtags.txt"

read_tweets(fileName_train_tweets,fileName_train_tweet_all_hashtags,fileName_train_tweet_unique_hashtags,fileName_train_hashtag_histogram )

fileName_test_data = "../data/f_hashtag_prediction/test_data_raw.txt"
fileName_test_userid = "../data/f_hashtag_prediction/test_data_userid.txt"
fileName_test_tweets = "../data/f_hashtag_prediction/test_data_tweets.txt"
fileName_test_location = "../data/f_hashtag_prediction/test_data_location.txt"

split_dataset(fileName_test_data, fileName_test_userid, fileName_test_tweets, fileName_test_location)

fileName_train_tweet_all_hashtags = "../data/f_hashtag_prediction/test_data_all_hashtags.txt"

extract_tags(fileName_test_tweets, fileName_train_tweet_all_hashtags)


sys.exit(0)

with open("hashtag_histogram.txt") as f:
    data=[tuple(line) for line in csv.reader(f, delimiter =' ')]
histogram_plot(data)

print("--- %s seconds ---" % (time.time() - start_time))