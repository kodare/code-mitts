from mongoengine import (EmbeddedDocument, StringField, EmbeddedDocumentField,
                         ListField)
from codemitts.models.Task import Task


class Quest(EmbeddedDocument):
    name = StringField()
    description = StringField()
    tasks = ListField(EmbeddedDocumentField(Task))
