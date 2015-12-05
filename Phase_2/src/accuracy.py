import itertools as it

filename="prediction_result_1K_unique_1000.txt"

def accuracy(filename):
    with open(filename,'r') as fresults:
        count = 0
        total_precision = 0
        total_recall = 0
        for key,group in it.groupby(fresults,lambda line: line.startswith('**********')):
            if not key:
                count += 1
                group = list(group)
                predict_tags = str(group[1])
                test_tags = str(group[2])

                pt = predict_tags.replace("TRAIN TAGS: ","").replace("set([","").rsplit("])")[0].split(",")
                tt = test_tags.replace("TEST TAGS:","").replace("set([","").rsplit("])")[0].split(",")
                ptags = set()
                ttags = set()
                for i in pt:
                    ptags.add(i.replace("'","").strip())
                for i in tt:
                    ttags.add(i.replace("'","").strip())

                # print ptags
                # print ttags

                true_positives = ptags.intersection(ttags)
                false_positives = ptags - ttags
                precision  = (len(true_positives) * 1.0)/ (len(true_positives) + len(false_positives))

                false_negatives = ttags - ptags
                recall = (len(true_positives)* 1.0) / (len(true_positives) + len(false_negatives))

                total_precision += precision
                total_recall += recall

                # print "precision: " + str(precision)
                # print "recall: " + str(recall)
                # print "true positives: " +str(len(true_positives))
                # print "false positives: " +str(len(false_positives))
                # print "false negatives: " +str(len(false_negatives))

        # print total_precision
        # print total_recall
        # print count
        avg_precision = (total_precision / (1.0 * count)) * 100
        print "average precision %: " + str(avg_precision)

        avg_recall = (total_recall / (1.0 * count)) * 100
        print "average recall %: " + str(avg_recall)


accuracy("prediction_result_1K_unique_100.txt")
accuracy("prediction_result_1K_unique_250.txt")
accuracy("prediction_result_1K_unique_750.txt")
accuracy("prediction_result_1K_unique_1000.txt")