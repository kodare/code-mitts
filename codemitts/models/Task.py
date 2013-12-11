from mongoengine import ReferenceField
from codemitts.models.BaseDocument import BaseDocument
from codemitts.models.Feature import Feature


# These models are for now only examples, feel free to change them when needed

class Task(BaseDocument):
    feature = ReferenceField(Feature, required=True)
    meta = {'allow_inheritance': True}
