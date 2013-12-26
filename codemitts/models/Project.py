from datetime import datetime
from mongoengine import (DateTimeField, EmbeddedDocumentField, ListField,
                         ReferenceField)
from codemitts.models.BaseDocument import BaseDocument
from codemitts.models.Feature import Feature
from codemitts.models.User import User


class Project(BaseDocument):
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    features = ListField(EmbeddedDocumentField(Feature))
    created_by = ReferenceField(User)
