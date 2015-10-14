import tweepy
import time
import settings
import settings_skk
import Queue

auth = tweepy.auth.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=120, timeout= 120, parser=tweepy.parsers.JSONParser())

auth2=tweepy.auth.OAuthHandler(settings_skk.consumer_key, settings_skk.consumer_secret)
auth2.set_access_token(settings_skk.access_token, settings_skk.access_secret)
api2=tweepy.API(auth2,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=120, timeout= 120, parser=tweepy.parsers.JSONParser())


if(api.verify_credentials):
    print 'sucessfully logged in api1 to crawl'

if(api2.verify_credentials):
    print 'sucessfully logged in api2 to crawl'

me = api.me()
print "bfs root: " + str(me["id"])
results = api.rate_limit_status()
results2 = api2.rate_limit_status()

def crawl():
    file = open('P1_Deliverables/dataset_bfs_trace.txt','w')
    q = Queue.Queue()
    q.put(me["id"])
    samplefile = open('P1_Deliverables/3_sampled.txt','w')
    edgeList = open('P1_Deliverables/2_edgeList.txt','w')
    file.write(str(me["id"]) + ","+ str(0) + '\n')

    def bfs():
        visited_node_count =1
        while not q.empty() and visited_node_count < 1000:
            id = q.get()
            print ("visiting " + str(id))
            try:
                while True:
                    print "checking api1"
                    results = api.rate_limit_status()
                    remaining = results["resources"]["friends"]["/friends/ids"]["remaining"]
                    if remaining > 0:
                        use_api = api
                        print "using api1"
                        break
                    else:
                        print "checking api2"
                        results2 = api2.rate_limit_status()
                        remaining2 = results2["resources"]["friends"]["/friends/ids"]["remaining"]
                        if remaining2 > 0:
                            use_api = api2
                            print "using api2"
                            break
                        else:
                            print "going to sleep"
                            time.sleep(60 * 2)
                print "fetching friends ids.."
                nodeFriends = use_api.friends_ids(id)
                print ("which has " + str(len(nodeFriends["ids"])) + " friends")
                if len(nodeFriends['ids'])>1000:
                    samplefile.write(str(id) + "," + str(len(nodeFriends["ids"]))+'\n')
                count = 0
                for f in nodeFriends["ids"]:
                    if count < 1000:
                        q.put(f)
                        file.write(str(f) + ","+ str(visited_node_count) +'\n')
                        edgeList.write(str(id)+","+str(f)+'\n')
                        count += 1
                visited_node_count += 1
                print ("visited count: "+str(visited_node_count) + "current queue size: " + str(q.qsize()))
            except tweepy.TweepError:
                print "sleeping..."
                queueBackup = open('queueBackup.txt','w')
                while not q.empty():
                    queueBackup.write(str(q.get())+ '\n')
                queueBackup.close()
                time.sleep(60 * 2)
                lines = [line.rstrip('\n') for line in
         open('queueBackup.txt')]
                for line in lines:
                    q.put(line)
                continue
    bfs()
    file.close()
    samplefile.close()
    edgeList.close()

def getUserNames(nodeIDs):
    #users = api.lookup_users(user_ids=nodeIDs)
    for id in nodeIDs[1366:len(nodeIDs)]:
        getUserNameById(id)

def getUserNameById(id):
    user = api.get_user(id)
    print (str(id) + ", " + str(user.screen_name))

def anonymize_dataset_trace():
    lines = [line.strip('\n') for line in
         open('P1_Deliverables/dataset_bfs_trace.txt')]
    file_dataset = open('P1_Deliverables/1_dataset.txt','w')
    file_anonymized_dataset = open('P1_Deliverables/1_anonymized_dataset.txt','w')
    count = 1
    unique = set()
    for line in lines:
        line = line.split(',',1)[0]
        if line not in unique:
            unique.add(line)
            file_dataset.write(line + str('\n'))
            file_anonymized_dataset.write(line + "," + str(count) + str('\n'))
            count+=1
    file_dataset.close()
    file_anonymized_dataset.close()

def anonymize_dataset():
    lines = [line.strip('\n') for line in open('P1_Deliverables/1_anonymized_dataset.txt')]
    dict = {'key':'value'}
    for line in lines:
        line = line.split(',')
        key = line[0]
        value = line[1]
        dict[key] = value
    file_anonymized_sampled = open('P1_Deliverables/3_anonymized_sampled.txt','w')
    lines_sampled = [line.strip('\n') for line in open('P1_Deliverables/3_sampled.txt')]
    for line_sampled in lines_sampled:
        line_sampled_node = line_sampled.split(',')
        key_node = line_sampled_node[0]
        count = line_sampled_node[1]
        anon_node_value = dict[key_node]
        file_anonymized_sampled.write(str(anon_node_value) + "," + str(count)+ str('\n'))
    file_anonymized_sampled.close()
    anonymize_edgelist(dict)

def remove_trace_number():
    lines = [line.strip('\n') for line in open('bfs_nodes_all.txt')]
    file_bfs_trace = open('P1_Deliverables/dataset_bfs_trace.txt','w')
    for line in lines:
        line = line.split(',',1)[0]
        file_bfs_trace.write(str(line) + '\n')
    file_bfs_trace.close()

def anonymize_edgelist(dict):
    lines = [line.strip('\n') for line in open('P1_Deliverables/2_edgeList.txt')]
    file_anonymized_edgeList = open('P1_Deliverables/2_anonymized_edgeList.txt','w')
    for line in lines:
        line = line.split(',')
        key1 = line[0]
        key2 = line[1]
        file_anonymized_edgeList.write(str(dict[key1])+ "," + str(dict[key2]) + str('\n'))
    file_anonymized_edgeList.close()


#main

crawl()
anonymize_dataset_trace()
anonymize_dataset()




