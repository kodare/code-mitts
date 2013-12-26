from mongoengine import EmbeddedDocument, StringField


class Task(EmbeddedDocument):
    name = StringField()
    description = StringField()
    meta = {'allow_inheritance': True}
