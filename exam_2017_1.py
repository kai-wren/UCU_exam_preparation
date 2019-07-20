from datetime import date
from datetime import datetime
from datetime import timedelta
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

class user_class:
    
    def __init__(self, class_obj):
        self.user_inst = class_obj

    def getUserEmailGeneric(self):
        if isinstance(self.user_inst, TwitterUser) == True:
            return self.user_inst.getUserMail()
        if isinstance(self.user_inst, FacebookUser) == True:
            return self.user_inst.getEmail()
    
    def getCountryGeneric(self):
        if isinstance(self.user_inst, TwitterUser) == True:
            return self.user_inst.getCountry()
        if isinstance(self.user_inst, FacebookUser) == True:
            return self.user_inst.getUserCountry()

    def getLastActive(self):
        if isinstance(self.user_inst, TwitterUser) == True:
            return self.user_inst.getLastActiveTime()
        if isinstance(self.user_inst, FacebookUser) == True:
            return self.user_inst.getUserActiveTime()
        

class MessageSender:
    
    def send(self, text, user, country):
        
        u = user_class(user)
        ret = None
        currentTime = datetime.today()
        if (u.getCountryGeneric() == country) & (currentTime - u.getLastActive() < timedelta (minutes = 60)):
            ret = u.getUserEmailGeneric()    
        return ret

MS = MessageSender()

text = 'Message text!'
# loggedUsr = TwitterUser()
# country = 'UA'
loggedUsr = FacebookUser()
country = 'UK'

print('Message:', text, 'sent to user', MS.send(text, loggedUsr, country))