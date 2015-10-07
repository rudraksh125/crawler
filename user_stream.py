import tweepy
import time
import settings
import Queue

auth = tweepy.auth.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth,wait_on_rate_limit=False, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

if(api.verify_credentials):
    print 'We sucessfully logged in'

me = api.me()
print (me.id, me.screen_name)
print ("rate limit status: " + str(api.rate_limit_status()))

file = open('bfs_nodes.txt','w')
q = Queue.Queue()
q.put(me.id)
samplefile = open('samples.txt','w')
edgeList = open('edgeList.txt','w')
file.write(str(me.id) + ","+ str(0) + '\n')

def bfs():
    visited_node_count =1
    while not q.empty() and visited_node_count < 1000:
        id = q.get()
        print ("visiting " + str(id))
        try:
            # nodeFriends = (1,2)
            nodeFriends = api.friends_ids(id)
            print ("which has " + str(len(nodeFriends)) + " friends")
            if len(nodeFriends)>1000:
                samplefile.write(str(id) + ","+ str(visited_node_count) + "," + str(len(nodeFriends))+'\n')
            count = 0
            for f in nodeFriends:
                if count < 1000:
                    q.put(f)
                    file.write(str(f) + ","+ str(visited_node_count) +'\n')
                    edgeList.write(str(id)+","+str(f)+'\n')
                    count += 1
                    visited_node_count += 1
                    print ("visited count: "+str(visited_node_count) + "current queue size: " + str(q.qsize()))
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
bfs()
file.close()
samplefile.close()
edgeList.close()
    
