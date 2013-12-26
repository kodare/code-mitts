from mongoengine import (EmbeddedDocument, StringField, EmbeddedDocumentField,
                         ListField)
from codemitts.models.Task import Task


class Feature(EmbeddedDocument):
    name = StringField()
    description = StringField()
    tasks = ListField(EmbeddedDocumentField(Task))
