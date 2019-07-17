from datetime import date
from datetime import datetime
import time

class TwitterUser:
    
    def getUserMail(self):
        return 'user@twitter.com'

    def getCountry(self):
        return 'UA'

    def getLastActiveTime(self):
        d = datetime.today().replace(minute=0)
        return d

class FacebookUser:
    
    def getEmail(self):
        return 'user@facebook.com'

    def getUserCountry(self):
        return 'UK'

    def getUserActiveTime(self):
        d = datetime.today().replace(minute=10)
        return d

class user(TwitterUser, FacebookUser):
    pass

class MessageSender:
    
    def send(self, text, user, country):
        usr = user()
        print(usr.isinstance())
        text = "1"
        return text

MS = MessageSender()
MS.send('1','1','1')