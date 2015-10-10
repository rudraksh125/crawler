import tweepy
import time
import settings
import settings_skk
import Queue
import networkx as nx

auth = tweepy.auth.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=120, timeout= 120, parser=tweepy.parsers.JSONParser())

auth2=tweepy.auth.OAuthHandler(settings_skk.consumer_key, settings_skk.consumer_secret)
auth2.set_access_token(settings_skk.access_token, settings_skk.access_secret)
api2=tweepy.API(auth2,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=120, timeout= 120, parser=tweepy.parsers.JSONParser())


if(api.verify_credentials):
    print 'We sucessfully logged in api1'

if(api2.verify_credentials):
    print 'We sucessfully logged in api2'

me = api.me()
print "me: " + str(me["id"])
results = api.rate_limit_status()
results2 = api2.rate_limit_status()


def crawl():
    file = open('bfs_nodes_final.txt','w')
    q = Queue.Queue()
    q.put(me["id"])
    samplefile = open('samples_final.txt','w')
    edgeList = open('edgeList_final.txt','w')
    file.write(str(me["id"]) + ","+ str(0) + '\n')

    def bfs():
        visited_node_count =1
        while not q.empty() and visited_node_count < 1000:
            id = q.get()
            print ("visiting " + str(id))
            try:
                # nodeFriends = (1,2)
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
                            time.sleep(60 * 1)
                print "fetching friends ids.."
                nodeFriends = use_api.friends_ids(id)
                print ("which has " + str(len(nodeFriends["ids"])) + " friends")
                if len(nodeFriends['ids'])>1000:
                    samplefile.write(str(id) + ","+ str(visited_node_count) + "," + str(len(nodeFriends["ids"]))+'\n')
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
                time.sleep(60 * 15)
                lines = [line.rstrip('\n') for line in
         open('/Users/kvivekanandan/Desktop/ASU/CSE_598_Social_Media_Mining/Project/1_Submission/crawler/queueBackup.txt')]
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

def readEdgeListFromFile():
    lines = [line.rstrip('\n') for line in
         open('/Users/kvivekanandan/Desktop/ASU/CSE_598_Social_Media_Mining/Project/1_Submission/crawler/edgeList_final.txt')]
    return lines

def createGraphFromEdgeList(lines):
    G = nx.parse_edgelist(lines, delimiter=',', nodetype=int)
    return G

#main

crawl()
# lines = readEdgeListFromFile()
# G = createGraphFromEdgeList(lines)
# nodes = G.nodes()
# print len(nodes[1189:len(nodes)])
# getUserNames(nodes)



