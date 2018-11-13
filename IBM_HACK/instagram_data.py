import json
from InstagramAPI import InstagramAPI
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="hackathondb")

qry = mydb.cursor()
InstagramAPI = InstagramAPI("<username>", "<password>")
InstagramAPI.login()
InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
print(result)
feed=InstagramAPI.timelineFeed()  #getting feed
# Get All User Posts
import time
myposts=[]
has_more_posts = True
max_id=""

while has_more_posts:
    InstagramAPI.getSelfUserFeed(maxid=max_id)
    if InstagramAPI.LastJson['more_available'] is not True:
        has_more_posts = False #stop condition
        print ("stopped")
    
    max_id = InstagramAPI.LastJson.get('next_max_id','')
    myposts.extend(InstagramAPI.LastJson['items']) #merge lists
    time.sleep(0.1) # Slows the script down to avoid flooding the servers 
    
print(len(myposts))


with open('data.json', 'w') as outfile:
    json.dump(myposts, outfile)
with open('data.json') as file:
    data = json.load(file)
	
print(data[0]["caption"]["text"])
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sql = "INSERT INTO user_posts (u_id, post, time) VALUES (%s, %s, %s)"
values = (data[0]["caption"]["user_id"], data[0]["caption"]["text"], data[0]["caption"]["created_at"])
qry.execute(sql, values)

mydb.commit()

print("Row inserted.")
#print(myposts) # print all the posts

# link for the InstagramAPI setup
#  https://github.com/LevPasha/Instagram-API-python#egg=InstagramAPI




