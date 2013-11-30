from mongoengine import *
from codemitts.models.BaseDocument import BaseDocument
from codemitts.models.Project import Project

# These models are for now only examples, feel free to change them when needed

class Feature(BaseDocument):
    project = ReferenceField(Project, required=True)
