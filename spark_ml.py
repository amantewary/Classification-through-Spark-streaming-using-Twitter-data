from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.functions import col
from pyspark.sql import Row

from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import RandomForestClassifier


from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler

from pyspark.ml.evaluation import BinaryClassificationEvaluator,MulticlassClassificationEvaluator

#from pyspark.ml import PipelineModel

sc =SparkContext()
sqlContext = SQLContext(sc)
data = sqlContext.read.format('com.databricks.spark.csv').options(header='false', inferschema='true').load('/Users/nikhilkamath/Downloads/sample_code/testdata.csv')

#drop_list = ['tweet_id', 'airline_sentiment_confidence', 'negativereason', 'negativereason_confidence', 'airline', 'airline_sentiment_gold', 'name', 'negativereason_gold', 'retweet_count', 'tweet_coord','tweet_created', 'tweet_location', 'user_timezone']
#data = data.select([column for column in data.columns if column not in drop_list])
data.show(10)
#
#data.printSchema()

data.groupBy("_c0") \
    .count() \
    .orderBy(col("count").desc()) \
    .distinct() \
    .show()

#data.groupBy("SentimentText") \
#    .count() \
#    .orderBy(col("count").desc()) \
#    .show()

# set seed for reproducibility
(trainingData, testData) = data.randomSplit([0.7, 0.3], seed = 100)
print("Training Dataset Count: " + str(trainingData.count()))
print("Test Dataset Count: " + str(testData.count()))
#
## regular expression tokenizer
regexTokenizer = RegexTokenizer(inputCol="_c5", outputCol="words", pattern="\\W")
#
## stop words
add_stopwords = ["http","https","amp","rt","t","c","the","@"]
stopwordsRemover = StopWordsRemover(inputCol="words", outputCol="filtered").setStopWords(add_stopwords)
#
## bag of words count
countVectors = CountVectorizer(inputCol="filtered", outputCol="features", vocabSize=10000, minDF=5)
#
## convert string labels to indexes
label_stringIdx = StringIndexer(inputCol = "_c0", outputCol = "label")
#
#print (label_stringIdx)

rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=100, seed=100)
##lrModel = lr.fit(trainingData)
#
#
## build the pipeline
pipeline = Pipeline(stages=[regexTokenizer, stopwordsRemover, countVectors, label_stringIdx, rf])
#pipeline = Pipeline(stages=[regexTokenizer, stopwordsRemover, countVectors, lr])


#
## Fit the pipeline to training documents.
pipelineFit = pipeline.fit(trainingData)
predictions = pipelineFit.transform(testData)

predictions.select("_c5","_c0","probability","label","prediction") \
    .orderBy("probability", ascending=False) \
    .show(n = 30, truncate = 40)
#predictions.filter(predictions['prediction'] == 0.0) \
#    .select("_c5","_c0","probability","label","prediction") \
#    .orderBy("probability", ascending=False) \
#    .show(n = 10, truncate = 30)
#
#predictions.filter(predictions['prediction'] == 1.0) \
#    .select("_c5","_c0","probability","label","prediction") \
#    .orderBy("probability", ascending=False) \
#    .show(n = 10, truncate = 30)
#    
#predictions.filter(predictions['prediction'] == 2.0) \
#    .select("_c5","_c0","probability","label","prediction") \
#    .orderBy("probability", ascending=False) \
#    .show(n = 10, truncate = 30)    

# Evaluate, metricName=[accuracy | f1]default f1 measure
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
print("Accuracy: %g" % (evaluator.evaluate(predictions)))

# save the trained model for future use
pipelineFit.save("logreg.model")

# PipelineModel.load("logreg.model")
