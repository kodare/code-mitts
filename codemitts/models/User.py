from mongoengine import Document, DateTimeField, StringField
from datetime import datetime


class User(Document):
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField()
    email = StringField(max_length=254, unique=True)

    meta = {
        'indexes': [
            {
                'fields': ['username'],
                'unique': True,
                'sparse': True
            }
        ]
    }
