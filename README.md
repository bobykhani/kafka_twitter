# Twitter Kafka Postgres

<p align="center">
<img src="https://user-images.githubusercontent.com/30469278/190903697-7e00bb41-8559-471e-a160-0162ef2f4a86.png" width=70% height=70%>
</p>


## PubSub
Pub/Sub allows services to communicate asynchronously, with latencies on the order of 100 milliseconds. Pub/Sub is used for streaming analytics and data integration pipelines to ingest and distribute data.

The Pub Sub queue (or Pub/Sub) is a message pattern of message brokers and it is used to communicate between the various components of micro-services. It is used to provide program-to-program and asynchronous communication between the micro-services.

## Kafka
<p align="center">
<img src="https://user-images.githubusercontent.com/30469278/190903341-7043a70b-b553-46b6-a01e-46d4d08149bd.png" width=50% height=50%>
</p>

Kafka is primarily used to build real-time streaming data pipelines and applications that adapt to the data streams. It combines messaging, storage, and stream processing to allow storage and analysis of both historical and real-time data.

Kafka Streams lets you read data in real time from a topic, process that data (such as by filtering, grouping, or aggregating it) and then write the resulting data into another topic or to other systems of record.

## Data

<p align="center">
<img src="https://user-images.githubusercontent.com/30469278/190903535-caf17e2b-53fb-4ead-8451-511fca49bc0f.png" width=50% height=50%>
</p>

## Endpoint:
GET /2/tweets/sample/stream

### What we get?
Tweet ID, Tweet content

### More information:
https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/api-reference/get-tweets-sample-stream

## Database system

### Postgres

PostgreSQL provides a good stream-based data processing product, with a real-time computing capability up to 100,000 records per second on a single common X86 server.

PostgreSQL is the most professional of the relational Open Source databases and was awarded “Database System Of The Year” several times. It is a highly reliable, stable, scalable and secure system, and has been around for more than two decades now.

PostgreSQL is well known as the most advanced opensource database, and it helps you to manage your data no matter how big, small or different the dataset is, so you can use it to manage or analyze your big data, and of course, there are several ways to make this possible, e.g Apache Spark.

## How to run it?

````
git clone git@github.com:bobykhani/kafka_twitter.git
cd kafka_twitter
````

````
docker-compose -f docker_compose.yml up
````

## Connecting to database
After running the docker-compose command you also can directly connect to the docker container database and reach to data

localhost:5435\
maindb = postgres\
username = postgresuser\
password = posrgrespw


````
SELECT tweet_id, text
	FROM public.twitter_data;
````
