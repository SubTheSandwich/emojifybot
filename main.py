import tweepy
import random
import emoji

consumer_key = "" 
consumer_secret = "" 
access_token = "" 
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

screen_name = ""

mentions = api.mentions_timeline(count=1)
replies = open('replied-to.txt', 'r')

text = "EMOJIFY"
file = open('replied-to.txt', 'r+')
b = file.readlines()
b = str(b)
b = b.replace("['", "").replace("']", "")
print(b)
def main():
    for mention in mentions:
        print(mention.in_reply_to_status_id_str)
        if (str(b) != mention.in_reply_to_status_id_str):
            if (text.lower() in mention.text.lower()):
                if mention.in_reply_to_status_id is not None:
                    tweet = api.get_status(mention.in_reply_to_status_id)
                    tweettext = tweet.text

                    new_reply = ""
                    for word in tweettext.split():
                        lines = open('emojis.txt', encoding="utf8").read().splitlines()
                        actual_reply = random.choice(lines)
                        new_reply = new_reply + actual_reply + word

                    with open("replied-to.txt", 'r+') as h:
                        for line in b:
                            if line.strip("\n") != "never will be this so clear":
                              h.write(line)
                    h = open('replied-to.txt', 'r+')
                    h.write(mention.in_reply_to_status_id_str)
                    print("New mention, replied!")
                    api.update_status(status = new_reply, in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True)
                else:
                    with open("replied-to.txt", 'r+') as h:
                        for line in b:
                            if line.strip("\n") != "never will be this so clear":
                                h.write(line)
                    h = open('replied-to.txt', 'r+')
                    h.write(api.in_reply_to_status_id_str)
                    print("Didnt @ in thread but put in because no.")
                    
            else:
                print (mention.text.lower() == "@_subfn " + text.lower())
                print (mention.text)
                print (mention.id)
                print (text.lower())
                print (mention.user.screen_name)
                print (mention.in_reply_to_status_id)
                return
                
             
        else:
            print("Already in, ignoring...")
        
           


if __name__ == "__main__":
    main()
