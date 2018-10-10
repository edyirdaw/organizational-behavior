# Tested on python2.7

from textblob import TextBlob
import re




def saintment():

    # text = '<@U6UH0PMV1> <@U04JNBU9W> possibly worth mentioning is @linas attempt <https://github.com/opencog/opencog/pull/1563>'
    # text_2 = 'possibly worth mentioning is @linas attempt'

    # text = '''*T*- working on the script that's going to be translated to Amharic to be recorded and incorporated to the demo'''
    text = '''1155'''
    text_2 = '''working on the script that's going to be translated to Amharic to be recorded and incorporated to the demo'''


    blob = TextBlob(text)
    blob_2 = TextBlob(text_2)

    print(blob.sentiment)
    print(blob_2.sentiment)

def reg():

    # text = 'he"9y'
    # text = 'hey'
    text = '''.... -- .'''
    # text = '?'
    text = re.sub('[^A-Za-z0-9]', '', text)
    if text == '':
        print(':(')
    else:
        print(text)

    print(True if text == '' else False)



def cont():

    # text = 'egele has joined the channel'
    # text = 'egele has joilned the channel'
    text = 'egele has left the channel'

    if 'has joined the channel' in text or 'has left the channel' in text:
        print('yikes')
    else:
        print(text)





__end__ = '__end__'


if __name__ == '__main__':


    # cont()
    reg()
    # saintment()

    pass