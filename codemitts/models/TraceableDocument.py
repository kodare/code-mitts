from mongoengine import DateTimeField, Document, ReferenceField
from datetime import datetime
from codemitts.models.User import User

# These models are for now only examples, feel free to change them when needed


class TraceableDocument(Document):
    created_by = ReferenceField(User, required=False)
    created_at = DateTimeField(required=True, default=datetime.utcnow)
    updated_at = DateTimeField(required=True)
    meta = {'allow_inheritance': True}
