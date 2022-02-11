# import pre save signals
# tell us that anything we use in pre save is gonna go into 
# our models and will listen to a moel to save and we can fire off 
# an action before that model finishes that save process
from django.db.models.signals import pre_save
# import User model because we want to fire off an action 
# anytime our user model is creared or updated
from django.contrib.auth.models import User


def updateUser(sender, instance, **kwargs):
    user = instance
    # check if email is not empty, take email and update user and pass in user email
    if user.email != '':
        user.username = user.email


# connect this signa to the user model
# everyrtime user model is saved, pre_save fire this function off
pre_save.connect(updateUser, sender=User)