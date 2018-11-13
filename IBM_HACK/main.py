import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions
import mysql.connector


mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="hackathondb")

qry = mydb.cursor()

data =  '{ "u_id":1, "post":"Hey! There", "time":"2018-08-02"}'
data = json.loads(data)

print(data["post"])

qry.execute("SELECT * FROM user_posts")

result = qry.fetchall()
y=[]


natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='9d214298-71ea-41e4-9b4f-d682c25e94a8',
    password='3ewnJMUKIgsG',
    version='2018-03-16')


for x in result:
  response = natural_language_understanding.analyze(
  text=x[2],
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2))).get_result()

  print(json.dumps(response, indent=2))
	
  y.append({ "u_id":x[0], "post":x[2]})
  js=json.dumps({'posts':y})
  print(js)
	


	
