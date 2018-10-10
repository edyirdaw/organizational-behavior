# Tested on python2.7

import db_interface
from textblob import TextBlob
import logging
import re



class SentimentAnalysis:



    bad_texts = ['has joined the channel','has left the channel']

    def __init__(self,db):


        self.db = db
        self.non_alpha_counter = 0
        self.bad_texts_counter = 0



    def read_messages(self):

        d = db_interface.DbInterface(self.db)

        sentiments = []

        try:
            q = """SELECT * from message"""
            d.cursor.execute((q))
            rows = d.cursor.fetchall()
            for row in rows:
                if self.is_non_alpha_numeric(row['text']):
                    self.non_alpha_counter = self.non_alpha_counter + 1
                    continue
                if self.contains_x(row['text']):
                    self.bad_texts_counter = self.bad_texts_counter + 1
                    continue

                # sentiments.append(row['id'])



        except Exception as e:

            logging.exception("message")





    def create_sentiment(self):

        pass


    def is_non_alpha_numeric(self,text):

        text = re.sub('[^A-Za-z0-9]', '', text)
        return True if text == '' else False

    def contains_x(self,text):

        for bt in self.bad_texts:
            if bt in text:
                return True

        return False






def run_1():

    s = SentimentAnalysis('local')
    s.read_messages()











__end__ = '__end__'


if __name__ == '__main__':

    run_1()

    pass