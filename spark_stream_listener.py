from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.ml import PipelineModel
from pyspark.sql.functions import col
from pyspark.sql import Row
from pyspark.sql.types import *

# from pyspark.sql.functions import desc

#sc = SparkContext("local[2]", "Tweet Streaming App")



def array_to_string(my_list):
    return '[' + ','.join([str(elem) for elem in my_list]) + ']'


#ssc = StreamingContext(sc, 10)
#sqlContext = SQLContext(sc)
#ssc.checkpoint( "/Users/nikhilkamath/Downloads/checkpoint")
#
#socket_stream = ssc.socketTextStream("127.0.0.1", 5556) # Internal ip of  the tweepy streamer


spark = SparkSession \
    .builder \
    .appName("Tweet Streaming App") \
    .getOrCreate()

socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "127.0.0.1") \
    .option("port", 5556) \
    .load()

socketDF.printSchema()    # Returns True for DataFrames that have streaming sources


#lines = socket_stream.window(20)
##
#lines.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()
##
#

oldColumns = socketDF.schema.names
newColumns = ["_c5"]

df = reduce(lambda socketDF, idx: socketDF.withColumnRenamed(oldColumns[idx], newColumns[idx]), xrange(len(oldColumns)), socketDF)
#df.printSchema()
#File_save2 = df.writeStream.format("console").start()#print (result)


#
## If we want to filter hashtags only
## .filter( lambda word: word.lower().startswith("#") )
#words = lines.flatMap( lambda twit: twit.split(" ") )
#pairs = words.map( lambda word: ( word.lower(), 1 ) )
#wordCounts = pairs.reduceByKey( lambda a, b: a + b ) #.transform(lambda rdd:rdd.sortBy(lambda x:-x[1]))
#wordCounts.pprint()
#
##test = sqlContext.createDataFrame(words).toDF("tweets")
##
##
rf = PipelineModel.load("/usr/local/Cellar/apache-spark/2.3.1/libexec/bin/logreg.model")
#
prediction = rf.transform(df)
#
File_save2 = prediction.writeStream.format("console").start()
#
#prediction.select([col(c).cast("string") for c in prediction.columns])
#pred = prediction.drop("words", "filtered", "features", "rawPrediction", "probability")
#pred.printSchema()
#
##File_save = prediction.writeStream.format("console").start()#print (result)
##File_save.awaitTermination()
#
#
#File_save2=pred.writeStream.format("parquet").option("checkpointLocation", "/Users/nikhilkamath/Downloads/checkpoint").option("path", "tweet_output").outputMode("append").start()
##prediction.writeStream.format("parquet").option("checkpointLocation", "/Users/nikhilkamath/Downloads/checkpoint").start("tweet_output.csv")#print (result)
File_save2.awaitTermination()


#prediction.drop("words", "filtered", "features", "rawPrediction", "probability").toPandas().to_csv("tweet_output.csv")

#ssc.start()
#
#ssc.awaitTerminationOrTimeout(10)

#prediction.writeStream.format("csv").option("checkpointLocation", "/Users/nikhilkamath/Downloads/checkpoint").outputMode("append").option("header", "true").start("tweet_output.csv")