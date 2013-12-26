from datetime import datetime
from mongoengine import Document, DateTimeField, StringField


class User(Document):
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    first_name = StringField(max_length=50, default="")
    last_name = StringField(max_length=50, default="")
    username = StringField()
    email = StringField(max_length=254, unique=True)
    gravatar_id = StringField(max_length=32, default="")

    meta = {
        'indexes': [
            {
                'fields': ['username'],
                'unique': True,
                'sparse': True
            }
        ]
    }

    def getGravatarURL(self, size):
        url = "http://www.gravatar.com/avatar/" + self.gravatar_id
        url = url + "?s=" + str(size)
        return url
