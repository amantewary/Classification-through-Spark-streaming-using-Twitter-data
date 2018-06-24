## Classification-through-Apache-Spark-streaming-using-Twitter-data


</br>
### Table of Contents


#### [1. Task Description](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#1-task-description-1)

#### [2. Installation Notes](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#2-twitter-tweet-extraction-1)
#### [3. Twitter Tweet Extraction](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#2-twitter-tweet-extraction-1)
#### [4. Sentiment Analysis Algorithm](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#3-sentiment-analysis-1)
#### [5. Labelling training data](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#4-loading-data-into-elasticsearch)
#### [6. Feature selection:](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#5-etl-as-a-batch-process-bonus-1)
#### [7. Output:](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#6-licence)

</br>

### 1. Task Description

The task of this assignment was to perform sentiment analysis on stream of tweets using Apache spark and storing the results in CSV format. We were instructed to install Apache Spark on AWS however we installed it on Microsoft Azure. We are using python 2.7 for this assignment and Spark 2.3.1.

</br>

### 2. Installation Notes

* python 3 (if not present)
* pip3 (if not present)
* pandas
* tweepy
* Apache spark


#### Build Instructions:

1. To install python3 execute this command.

        sudo apt-get install -y python3-pip
        
2. Using pip you have to intall other libraries. To install tweepy execute this command.

        pip3 install tweepy
        
3. Install pandas next by executing this command.

        sudo -H pip3 install pandas
        
4. Install Apache Spark

</br>

### 3. Twitter Tweet Extraction

We are using **[tweepy](https://github.com/tweepy/tweepy)** to run a query and extract tweets. The tweets are fetched using Twitter Stream Listener. We are not cleaning the tweets and pushing it directly to the model. The model is trained using a training csv and then the model is fitted into the pipline.

</br>

### 4. Sentiment Analysis Algorithm

For this Assignment we have used **RandomForestClassifier** because from our analysis it gave us the maximum accuracy. We trained the model with 500 tweets and the accuracy is 57%. Despite our various attempts, we were not able to increase the accuracy of the model more than 57%. Since it is a classifcation problem, the model which was trainined had 3 labels, making it a 3 class classification problem.

</br>

### 5. Labelling training data
