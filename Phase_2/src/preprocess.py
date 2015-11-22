import csv
import time
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def extract_hashtags(s):
    return set(part[1:].lower().strip().rstrip(',') for part in s.split() if part.startswith('#'))

def read_dataset(fileName):
    list_all_hashtags = []
    with open("output_hashtags.csv", "wb") as output:
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
            with open("output_hashtags_unique.csv", "wb") as output_unique:
                output_unique.write("%s\n" % ",".join(unique_hashtags))

            print "Total number of tweets: " + str(num_total_tweets)
            print "Number of total hashtags: " + str(num_total_hashtags)
            print "Number of unique hashtags: " + str(len(unique_hashtags))
            print "Average number of hashtags per tweet : " + str(num_total_hashtags * 1.0 /num_total_tweets)

            dict_hashtag_counts = Counter(list_all_hashtags)
            with open("hashtag_histogram.txt","wb") as f:
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
#read_dataset("../data/f_hashtag_prediction/datastore.txt")

with open("hashtag_histogram.txt") as f:
    data=[tuple(line) for line in csv.reader(f, delimiter =' ')]
histogram_plot(data)

print("--- %s seconds ---" % (time.time() - start_time))