import tweepy
import socket
import requests
import time
import csv
import stat
import os
import socket
import json
import re

class TwitterStreamListener(tweepy.StreamListener):
        """ A listener handles tweets are the received from the stream.
        This is a basic listener that sends recieved tweets through a socket.
        """
        def __init__(self, sc):
                super(TwitterStreamListener, self).__init__()
                self.client_socket = sc

        def on_status(self, status):
                #print(status.text)
                tweet = self.get_tweet(status)
                #print(json.dumps(tweet).encode('utf-8'))
                self.client_socket.send((tweet[2]+"\n").encode('utf-8'))
                return True

        # Twitter error list : https://dev.twitter.com/overview/api/response-codes
        def on_error(self, status_code):
                print("Status code")
                print(status_code)
                if status_code == 403:
                        print("The request is understood, but the access is not allowed. Limit may be reached.")
                        return False

        def get_tweet(self,tweet):
                text = tweet.text
                if hasattr(tweet, 'extended_tweet'):
                        text = tweet.extended_tweet['full_text']
                return [str(tweet.user.id),tweet.user.screen_name,self.clean_str(text)]

        def clean_str(self, string):
                """
                Tokenization/string cleaning.
                """
                string = re.sub(r"\n|\t", " ", string)
                return string

if __name__ == '__main__':
        # Authentication
        consumer_key = "DSaMQVLUbCMCNACL9cNGPBFhL"
        consumer_secret = "NKdMDnPfdxO99G0smWtA8GHBrAJHnP6DVoikP0UFyiloSKkgEP"
        access_token = "1000039197753868291-TGOXH3jWGfOK9g5oWznKWbF5D1NYQd"
        access_token_secret = "T1nOwu1yc0RMcFMZjFkpNJCnUlU4KTr2zPuyK4GRjtxTg"

        # Local connection
        host = "127.0.0.1"          # Get local machine name (copy internal address from EC2 instance).
        port = 5559                 # Reserve a port for your service.

        s = socket.socket()         # Create a socket object.
        s.bind((host, port))        # Bind to the port.

        print("Listening on port: %s" % str(port))

        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()        # Establish connection with client.

        print("Received request from: " + str(addr))
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.secure = True
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)

        streamListener = TwitterStreamListener(c)
        myStream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
        myStream.filter(track=['movie','movies'], async=True)
