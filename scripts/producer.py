from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime
import requests
from kafka.admin import KafkaAdminClient, NewTopic



headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIS5hAEAAAAAyIdrfl4ZFXOQ4wc%2FJLpM9myVLqM%3DwxeIruDyTVjoHexTQHYFz8nkVWzE7YBS5Dh12ixeyauHVvxj43'}
producer = KafkaProducer(bootstrap_servers=['kafka:9092'],api_version=(0,10,1))


producer.send('trump', b'Hello, Kafka')

def get_stream(url,header):
    s = requests.Session()

    with s.get(url, headers=header, stream=True) as resp:
        resp.encoding = 'ISO-8859-1'
        for line in resp.iter_lines():
            if line:
                producer.send('trump', line)
                line = line.decode('utf8')
                print(line)

url = 'https://api.twitter.com/2/tweets/sample/stream?tweet.fields=text'
get_stream(url,headers)