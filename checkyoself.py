import twint
import sys

if len(sys.argv) == 1:
    print('usage: checkyoself.py USERNAME')
    sys.exit(1)

username = str(sys.argv[1].replace('@', ''))

f = open('badwords.txt','r')
badwords = f.read().splitlines()

c = twint.Config()
c.Username = username
#c.Limit = 400
c.Hide_output = True
c.Store_object = True

twint.run.Search(c)
tweets = twint.output.tweets_list

for x in tweets:
    if any(words in x.tweet for words in badwords):
        try: print('https://twitter.com/' + username + '/status/' + str(x.id) + '\n' + x.tweet + '\n')
        except: pass
