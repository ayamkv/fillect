import os
# os.system('pip install -r requirements.txt')
import requests, tweepy, webbrowser
from config import *
from pystyle import Colors, Colorate, Add, Center
import urllib.request, random, time
from PIL import Image
# or
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

if randomize == True:
   print('Randomize is set to true')
   time.sleep(2) 
   random_number = random.randint(1, 299999)
elif randomize == False:
   print('Randomize is set to False')
   random_number = input('num : ')
else:
   print('Randomize is set to None, setting it to True..')
   time.sleep(2)
   randomize = True


print(random_number)
auth = tweepy.OAuthHandler(apikey, apikey_secret)
auth_url = auth.get_authorization_url()
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)


clearConsole()
banner1 = '''
 _____         
|     | __  __ 
|   __||  ||  |
|  |_  |__||__|
|   _]  __  __ 
|  |   |  ||  |
|__|   |__||__|    
                          
 '''
text1 = 'fillect '
print(Colorate.Horizontal(Colors.blue_to_purple, Add.Add(banner1, text1, 4)))
print('\n')
# print(Colorate.Horizontal(Colors.blue_to_purple, text1, 2))
# 
arcURL = "https://archillect.mhsattarian.workers.dev/{}/img".format(random_number)
filename = '{}.jpg'.format(random_number)
def tweetID(api):
    tweet = api.user_timeline(
        user_id = api.verify_credentials().screen_name, 
        count = 1, 
        tweet_mode="extended" 
       # include_entities=True
        )[0]
    # print(tweet.id)
    return tweet.id
  
def tweetAuth():
    try:  # auth
      api.verify_credentials()
      print(Colorate.Color(Colors.cyan, 'Successful Authentication', True))
      print ("Authenticated as: %s" % api.verify_credentials().screen_name)
    except:
      print(Colors.red + 'Failed authentication')
      

def deleteImage(fn):
  filename = fn
  os.system('rm -rf {}'.format(filename)) # delete the image file to reduce space 
  print('image file deleted')


def postTweet(num, url):
  num = num
  url = url
  os.system('wget -nv --output-document={}.jpg {}'.format(num, url))
  tweet = str(random_number) + "\n #fillect"
  api.update_status_with_media(tweet, filename)


# try using webbrowser to open the tweet if it cant itll run a termux command if it cant too it will pass
def launchURL(url):
    url = url
    try:
      webbrowser.open(url)
      # print('webbrowser')
    except:
      os.system("termux-open-url {}".format(url))
      # print('termux')
    else:
      print('Done')

def getStatus():
    stUrl = 'https://twitter.com/twitter/statuses/{}'.format(tweetID(api))
   

    return stUrl

statusUrl = getStatus()

def job():
      tweetAuth()
      postTweet(random_number, arcURL)
      print(Colorate.Horizontal(Colors.blue_to_purple,statusUrl))
      launchURL(statusUrl)
      deleteImage(filename)

if __name__ == '__main__':
  if loop == True:
    print('Loop = True')
    while True:
      job()
      print(str(sleeptime) + ' ' + str(hours))
      time.sleep(sleeptime) 
  else:
    print('Loop = False')
    job()
    time.sleep(2)
