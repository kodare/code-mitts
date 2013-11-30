from mongoengine import *
from datetime import datetime

# These models are for now only examples, feel free to change them when needed

# TODO: Check if https://github.com/litl/rauth or https://github.com/omab/python-social-auth could
#       be used to authenticate via GitHub and automatically create a user the first time that user
#       authenticates

class User(Document):
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(required=True, unique=True)
