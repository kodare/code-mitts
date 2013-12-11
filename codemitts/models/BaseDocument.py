from mongoengine import StringField
from codemitts.models.TraceableDocument import TraceableDocument

# These models are for now only examples, feel free to change them when needed


class BaseDocument(TraceableDocument):
    name = StringField()
    description = StringField()
    meta = {'allow_inheritance': True}
