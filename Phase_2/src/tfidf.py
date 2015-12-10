from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
import time
import joblib

start_time = time.time()

joblib.dump("test","test.o")
a = joblib.load("test.o")
print a

import itertools
ab = itertools.chain(['aa','aa'], ['bed'], ['cat'])
print set(list(ab))

def test():
    truncated_train_svd = joblib.load("truncated_train_svd.o")
    truncated_test_svd = joblib.load("truncated_test_svd.o")
    row_index = 1001
    with open("../data/f_hashtag_prediction/test_data_tweets_processed_2K.txt") as ftest:
        test_set = ftest.read().splitlines()
        with open("prediction_result_2K_unique.txt","w") as output_prediction:
            with open("../data/f_hashtag_prediction/train_data_all_hashtags.txt") as ftrain:
                with open("../data/f_hashtag_prediction/test_data_all_hashtags.txt") as ftest:
                    test_set_hashtags = ftest.read().splitlines()
                    train_set_hashtags = ftrain.read().splitlines()
                    begin_index = 1001
                    for row in truncated_test_svd[begin_index:]:
                        if row_index > 2000:
                            break
                        print "TEST TWEET (row: " + str(row_index) + ") : " + test_set[row_index]
                        cosine = cosine_similarity(truncated_test_svd[row_index], truncated_train_svd)
                        m = max(cosine[0])
                        mindex = [i for i, j in enumerate(cosine[0]) if j == m]
                        train_tags = set()
                        test_tags = set()
                        for num_line in mindex:
                            train_tags.update(train_set_hashtags[num_line].split(","))
                        test_tags.update(test_set_hashtags[row_index].split(","))

                        utr = set(list(itertools.chain(train_tags)))
                        ut = set(list(itertools.chain(test_tags)))
                        test_tweet = "TEST TWEET (row: " + str(row_index) + ") : " + str(test_set[row_index])
                        print "TRAIN TAGS: " + str(utr)
                        print "TEST TAGS:" + str(ut)
                        print "*****"
                        output_prediction.write("*****\n"+test_tweet +"\n" + "TRAIN TAGS: " + str(utr) + "\n" + "TEST TAGS:" + str(ut) + "\n" + "*****")

                        row_index += 1

def retest(trainsvd):
    truncated_train_svd = joblib.load("truncated_train_svd_" + str(trainsvd)+".o")
    truncated_test_svd = joblib.load("truncated_test_svd_" + str(trainsvd)+".o")
    row_index = 0
    with open("../data/f_hashtag_prediction/test_data_tweets_processed_2K.txt") as ftest:
        test_set = ftest.read().splitlines()
        with open("prediction_result_1K_unique_"+ str(trainsvd)+".txt","w") as output_prediction:
            with open("../data/f_hashtag_prediction/train_data_all_hashtags.txt") as ftrain:
                with open("../data/f_hashtag_prediction/test_data_all_hashtags.txt") as ftest:
                    test_set_hashtags = ftest.read().splitlines()
                    train_set_hashtags = ftrain.read().splitlines()
                    begin_index = 0
                    for row in truncated_test_svd[begin_index:]:
                        if row_index > 1000:
                            break
                        print "TEST TWEET (row: " + str(row_index) + ") : " + test_set[row_index]
                        cosine = cosine_similarity(truncated_test_svd[row_index], truncated_train_svd)
                        m = max(cosine[0])
                        mindex = [i for i, j in enumerate(cosine[0]) if j == m]
                        train_tags = set()
                        test_tags = set()
                        for num_line in mindex:
                            train_tags.update(train_set_hashtags[num_line].split(","))
                        test_tags.update(test_set_hashtags[row_index].split(","))

                        utr = set(list(itertools.chain(train_tags)))
                        ut = set(list(itertools.chain(test_tags)))
                        test_tweet = "TEST TWEET (row: " + str(row_index) + ") : " + str(test_set[row_index])
                        print "TRAIN TAGS: " + str(utr)
                        print "TEST TAGS:" + str(ut)
                        print "*****"
                        output_prediction.write("*****\n"+test_tweet +"\n" + "TRAIN TAGS: " + str(utr) + "\n" + "TEST TAGS:" + str(ut) + "\n" + "*****")

                        row_index += 1

def retrain(svdcomp):
            smatrix = joblib.load("test_tfidf_matrix.o")
            tfidf_matrix = joblib.load("train_tfidf_matrix.o")

            svd = TruncatedSVD(n_components=svdcomp, random_state=42)
            svd.fit(tfidf_matrix)
            truncated_train_svd = svd.transform(tfidf_matrix)
            truncated_test_svd = svd.transform(smatrix)

            print truncated_train_svd.shape
            print truncated_test_svd.shape

            joblib.dump(truncated_train_svd, "truncated_train_svd_" + str(svdcomp)+".o")
            joblib.dump(truncated_test_svd, "truncated_test_svd_" + str(svdcomp)+".o")

def train_manual():
    with open("../data/f_hashtag_prediction/train_data_tweets_processed_0_to_500K.txt") as ftrain:
        with open("../data/f_hashtag_prediction/test_data_tagged_processed_manual.txt") as ftest:
            test_set = ftest.read().splitlines()
            train_set = ftrain.read().splitlines()
            # vectorizer = CountVectorizer()
            vectorizer = TfidfVectorizer(min_df=5, max_df=500, max_features=None,
                                         strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                                         ngram_range=(1, 4), use_idf=1, smooth_idf=1, sublinear_tf=1,
                                         stop_words='english')
            # vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(train_set)
            print tfidf_matrix.shape

            smatrix = vectorizer.transform(test_set)
            print smatrix.shape

            svd = TruncatedSVD(n_components=500, random_state=42)
            svd.fit(tfidf_matrix)
            truncated_train_svd = svd.transform(tfidf_matrix)
            truncated_test_svd = svd.transform(smatrix)

            print truncated_train_svd.shape
            print truncated_test_svd.shape

            cosine = cosine_similarity(truncated_test_svd[0], truncated_train_svd)
            print cosine

        print "TEST SET: "

def train():
    with open("../data/f_hashtag_prediction/train_data_tweets_processed_0_to_500K.txt") as ftrain:
        with open("../data/f_hashtag_prediction/test_data_tweets_processed_2K.txt") as ftest:
            test_set = ftest.read().splitlines()
            train_set = ftrain.read().splitlines()
            # vectorizer = CountVectorizer()
            vectorizer = TfidfVectorizer(min_df=5, max_df=500, max_features=None,
                                         strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                                         ngram_range=(1, 4), use_idf=1, smooth_idf=1, sublinear_tf=1,
                                         stop_words='english')
            # vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(train_set)
            print tfidf_matrix.shape
            # print tfidf_matrix
            # print vectorizer.fixed_vocabulary_
            smatrix = vectorizer.transform(test_set)
            print smatrix.shape

            joblib.dump(smatrix, "test_tfidf_matrix.o")
            joblib.dump(tfidf_matrix, "train_tfidf_matrix.o")

            svd = TruncatedSVD(n_components=500, random_state=42)
            svd.fit(tfidf_matrix)
            truncated_train_svd = svd.transform(tfidf_matrix)
            truncated_test_svd = svd.transform(smatrix)

            print truncated_train_svd.shape
            print truncated_test_svd.shape

            joblib.dump(truncated_train_svd, "truncated_train_svd.o")
            joblib.dump(truncated_test_svd, "truncated_test_svd.o")

        print "TEST SET: "
        test_index = 0
        # for t in test_set:
        # print "test tweet: " + t
        # cosine = cosine_similarity(smatrix[0:1], tfidf_matrix)

        # row_index = 0
        # with open("../data/f_hashtag_prediction/train_data_all_hashtags.txt") as ftrain:
        #     with open("../data/f_hashtag_prediction/test_data_all_hashtags.txt") as ftest:
        #         test_set_hashtags = ftest.read().splitlines()
        #         train_set_hashtags = ftrain.read().splitlines()
        #
        #         for row in truncated_test_svd:
        #             if row_index > 100:
        #                 break
        #             print "TEST TWEET (row: "+ str(row_index) + ") : "+  test_set[row_index]
        #             # cosine = cosine_similarity(smatrix[row_index], tfidf_matrix)
        #             cosine = cosine_similarity(truncated_test_svd[row_index], truncated_train_svd)
        #             m = max(cosine[0])
        #             # print m
        #             mindex = [i for i, j in enumerate(cosine[0]) if j == m]
        #             # print mindex
        #             # print "most similar tweets from training: "
        #             # for i in mindex:
        #             #     print train_set[i]
        #             # num_line = 0
        #             # test_num_line = 0
        #             train_tags = set()
        #             test_tags = set()  # for line in ftrain:
        #             for num_line in mindex:
        #                 # print "train hashtags (line_num: " + str(num_line) + "): " + line
        #                 train_tags.add(train_set_hashtags[num_line])
        #                 # for l in ftest:
        #                 #     if test_num_line == row_index:
        #                 #         # print "test set hashtags: " + l
        #             test_tags.add(test_set_hashtags[row_index])
        #             #             break
        #             #         test_num_line += 1
        #             # num_line += 1
        #             row_index += 1
        #
        #             print "TRAIN TAGS: " + str(train_tags)
        #             print "TEST TAGS:" + str(test_tags)
        #             print "*****************"

# test()
retrain(100)
retrain(250)
retrain(750)
retrain(1000)
retrain(1500)
retest(100)
retest(250)
retest(750)
retest(1000)
retest(1500)
# train_manual()

print("--- %s seconds ---" % (time.time() - start_time))