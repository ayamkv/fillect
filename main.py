import requests, tweepy
from config import *
from pystyle import Colors, Colorate, Add, Center
import urllib.request, random, os, time
from PIL import Image
# or
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


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
def tweetID(api):
    tweet = api.user_timeline(
        id = api.verify_credentials().screen_name, 
        count = 1, 
        tweet_mode="extended", 
        include_entities=True 
        )[0]
    print(tweet.id)
    return tweet.id

try:
    api.verify_credentials()
    print(Colorate.Color(Colors.cyan, 'Successful Authentication', True))
    print ("Authenticated as: %s" % api.verify_credentials().screen_name)
except:
    print(Colors.red + 'Failed authentication')
    
random_number = random.randint(1, 9000)
arcURL = "https://archillect.mhsattarian.workers.dev/{}/img".format(random_number)
# imgURL = "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg"

print(random_number)
# api.update_status(random_number)
filename = '{}.jpg'.format(random_number)
# 
print(filename)
# r = requests.get(arcURL, allow_redirects=True)
# open(filename, 'wb').write(r.content)
os.system('wget --output-document={}.jpg {}'.format(random_number, arcURL))
time.sleep(1)
tweet = str(random_number) + "\n #fillect"
api.update_status_with_media(tweet, filename)
getStatus = 'https://twitter.com/twitter/statuses/{}'.format(tweetID(api))
print(getStatus)
os.system("termux-open-url {}".format(getStatus))
time.sleep(5)
os.system('rm -rf {}'.format(filename))
# os.system('ls')
# urllib.request.urlretrieve(arcURL, "{}.jpg".format(random_number))
# os.startfile("{}.jpg".format(random_number))
# print('Auth success')
# print ("Authenticated as: %s" % api.me().screen_name)
