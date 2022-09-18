from kafka import KafkaConsumer
from json import loads
import json
import psycopg2

def connect():
    conn = psycopg2.connect(host='postgres',
                            port=5432,
                            user="postgresuser",
                            password="postgrespw",
                            database="postgres")
    return conn

def insert(conn,tweet):
    tweet_id = tweet['id']
    tweet_text = tweet['text']
    tweet_text = tweet_text.replace("'","''")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS public.twitter_data (Tweet_Id text, Text text)')
    conn.commit()
    cursor.execute('INSERT INTO public.twitter_data(Tweet_Id,Text) VALUES(\''+tweet_id+'\',\''+tweet_text+'\')')
    conn.commit()

print('start_________________________________________________________________________________')
consumer = KafkaConsumer('trump', bootstrap_servers=['kafka:9092'],api_version=(0,10))
print('consumer_________________________________________________________________________________')

for message in consumer:
        out = json.loads(message.value.decode('utf8'))["data"]
        conn = connect()
        print( out)
        insert(conn,out)
#        print("text: " + out["text"])