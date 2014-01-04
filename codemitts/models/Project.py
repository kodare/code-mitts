from datetime import datetime
from mongoengine import (DateTimeField, EmbeddedDocumentField, ListField,
                         ReferenceField)
from codemitts.models.BaseDocument import BaseDocument
from codemitts.models.Quest import Quest
from codemitts.models.User import User


class Project(BaseDocument):
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    quests = ListField(EmbeddedDocumentField(Quest))
    created_by = ReferenceField(User)
